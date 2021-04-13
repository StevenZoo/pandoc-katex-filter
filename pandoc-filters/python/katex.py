#!/usr/bin/env python3

import socket
import logging
from typing import Optional

from pandocfilters import RawInline, toJSONFilter

HOST = "localhost"
PORT = 7000

INLINE_BYTE = "\x00"
DISPLAY_BYTE = "\x01"
ERROR_PREFIX = "error:"

ENCODING = "UTF-8"

logger = logging.getLogger(__name__)


# Primary method for Pandoc filter.
def katex(key, value, format, meta):
    if key != "Math" or len(value) < 2:
        return None

    formatter, tex = value
    display = formatter['t'] == 'DisplayMath'

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as katex_socket:
        connect(HOST, PORT, katex_socket)

        html = render(tex, display, katex_socket)
        if html is not None:
            return RawInline('html', html)


# Renders TeX input to HTML
def render(tex: str, display: bool, katex_socket) -> Optional[str]:
    send_message(tex, display, katex_socket)
    data = get_response(katex_socket)

    if data.startswith(ERROR_PREFIX):
        # Log error message with source TeX input
        error_message = data[len(ERROR_PREFIX):]
        logger.error(f'Input: {tex}  {error_message}')
        return None

    return data


# Sends a TeX string, prefixed with the display mode, to the server.
def send_message(tex: str, display: bool, sock):
    request = build_request(tex, display)

    sock.sendall(request)
    sock.shutdown(socket.SHUT_WR)


def build_request(tex: str, display: bool) -> bytes:
    display_mode = DISPLAY_BYTE if display else INLINE_BYTE
    input_message = display_mode + tex

    return input_message.encode(ENCODING)


def get_response(sock) -> str:
    response = poll(sock)
    return response.decode(ENCODING)


def poll(sock) -> bytearray:
    chunks = bytearray()
    while True:
        chunk = sock.recv(1024)
        if not chunk:
            return chunks

        chunks.extend(chunk)


def connect(host: str, port: int, sock):
    try:
        sock.connect((host, port))
    except socket.error as error:
        logger.error("Could not connect to Node server.")
        raise SystemExit(error)


if __name__ == '__main__':
    toJSONFilter(katex)
