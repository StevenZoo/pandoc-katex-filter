#!/usr/bin/env python3

import socket
import sys
from typing import Optional

from pandocfilters import RawInline, toJSONFilter

HOST = "localhost"
PORT = 7000

INLINE_BYTE = "\x00"
DISPLAY_BYTE = "\x01"

ENCODING = "UTF-8"


# Primary method for Pandoc filter.
def katex(key, value, format, meta):
    if key != "Math" or len(value) < 2:
        return None

    formatter, tex = value
    display_mode = formatter['t'] == 'DisplayMath'

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as katex_socket:
        error_code = connect(HOST, PORT, katex_socket)
        if error_code:
            return None

        html = render(tex, display_mode, katex_socket)

        if html is not None:
            return RawInline('html', html)


# Sends TeX input to a server that renders into HTML.
def render(tex: str, display_mode: bool, katex_socket) -> Optional[str]:
    send_message(tex, display_mode, katex_socket)
    data, has_error = get_response(katex_socket)

    if has_error:
        log_error(tex, data)
        return None

    return data


# Sends a TeX string, prefixed with a flag to set the display mode.
def send_message(tex: str, display_mode: bool, sock):
    display_setting = DISPLAY_BYTE if display_mode else INLINE_BYTE
    input_message = display_setting + tex

    request = input_message.encode(ENCODING)

    sock.sendall(request)
    sock.shutdown(socket.SHUT_WR)


def get_response(sock) -> tuple:
    response = poll(sock)

    # Deconstruct response into error flag and rendered HTML/error message, depending on success or error.
    has_error = response[0] == 1
    data = response[1:].decode(ENCODING)

    return data, has_error


def poll(sock) -> bytearray:
    chunks = bytearray()
    while True:
        chunk = sock.recv(1024)
        if not chunk:
            return chunks

        chunks.extend(chunk)


def connect(host: str, port: str, sock) -> int:
    try:
        katex_socket.connect((host, port))
        return 0
    except socket.error as error:
        log_error(error)
        return 1


def log_error(error: str):
    print(error, file=sys.stderr)


def log_error(input: str, error: str):
    log_error(f'Input: {input}\t{error}')


if __name__ == '__main__':
    toJSONFilter(katex)
