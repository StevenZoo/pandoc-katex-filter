#!/usr/bin/env python3

import socket
import sys
from typing import Optional

from pandocfilters import RawInline, toJSONFilter

HOST = "localhost"
PORT = 7000

NUM_BYTES_META = 1

ENCODING = "UTF-8"

# Primary method for Pandoc filter.
def katex(key, value, format, meta):
    if key != "Math" or len(value) < 2:
        return None

    formatter, tex = value
    display = formatter['t'] == 'DisplayMath'

    html = render(tex, display)

    if html is not None:
        return RawInline('html', html)

# Sends TeX input to a server that renders into HTML.
def render(tex: str, display: bool, host=HOST, port=PORT) -> Optional[str]:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as katex_socket:
        connect(host, port, katex_socket)

        display_byte = '\x01' if display else '\x00'
        input_message = tex + display_byte

        output, has_error = send_message(input_message, katex_socket)
        if has_error:
            log_error(tex, output)
            return None

        return output


def connect(host: str, port: int, sock):
    try:
        sock.connect((host, port))
    except socket.error as msg:
        print(msg, file=sys.stderr)
        sys.exit(1)


def send_message(input_message: str, sock) -> tuple:
    request = input_message.encode(ENCODING)
    sock.sendall(request)
    sock.shutdown(socket.SHUT_WR)

    response = poll(sock)

    return unpack(response)


def poll(sock) -> bytearray:
    chunks = bytearray()
    while True:
        chunk = sock.recv(1024)
        if not chunk:
            return chunks

        chunks.extend(chunk)


def unpack(response: bytearray) -> tuple:
    data = response[:len(response) - NUM_BYTES_META]
    has_error = response[-1] == 1

    output = data.decode(ENCODING)
    return output, has_error


def log_error(input: str, error_message: str):
    print(f'Input: {input}\t{error_message}', file=sys.stderr)


if __name__ == '__main__':
    toJSONFilter(katex)
