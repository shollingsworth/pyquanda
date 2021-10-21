#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""http echo server."""
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse


def print_to_screen(jdump: str):
    """print_to_screen.

    Args:
        jdump (str): jdump
    """
    print(json.dumps(json.loads(jdump), indent=4, separators=(",", " : ")))


class RequestHandler(BaseHTTPRequestHandler):
    """RequestHandler."""

    def do_GET(self):
        """do_GET."""
        parsed_path = urlparse(self.path)
        self.send_response(200)
        self.end_headers()
        jdump = json.dumps(
            {
                "method": self.command,
                "path": self.path,
                "real_path": parsed_path.query,
                "query": parsed_path.query,
                "request_version": self.request_version,
                "protocol_version": self.protocol_version,
            }
        )
        print_to_screen(jdump)
        self.wfile.write(jdump.encode())

    def do_POST(self):
        """do_POST."""
        content_len = int(self.headers.get("content-length"))
        post_body = self.rfile.read(content_len)
        data = json.loads(post_body)

        parsed_path = urlparse(self.path)
        self.send_response(200)
        self.end_headers()
        jdump = json.dumps(
            {
                "method": self.command,
                "path": self.path,
                "real_path": parsed_path.query,
                "query": parsed_path.query,
                "request_version": self.request_version,
                "protocol_version": self.protocol_version,
                "body": data,
            }
        )
        print_to_screen(jdump)
        self.wfile.write(jdump.encode())


if __name__ == "__main__":
    try:
        server = HTTPServer(("localhost", 8000), RequestHandler)
        print("Starting server at http://localhost:8000")
        server.serve_forever()
    except KeyboardInterrupt:
        print("Bye!")
