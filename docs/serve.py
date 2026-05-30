"""Local dev server for the generated site.

Differs from `python3 -m http.server` in one important way: when a path doesn't
match a file, it serves `docs/404.html` (with HTTP 404) instead of the default
plain-text error page. Mirrors how GitHub Pages behaves.

Usage:
    cd docs && python3 serve.py
"""
import os
import socket
import http.server
import socketserver

PORT = 8000
DOCS_DIR = os.path.dirname(os.path.abspath(__file__))
NOT_FOUND_PAGE = os.path.join(DOCS_DIR, "404.html")


class SiteHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DOCS_DIR, **kwargs)

    def send_error(self, code, message=None, explain=None):
        if code == 404 and os.path.isfile(NOT_FOUND_PAGE):
            try:
                with open(NOT_FOUND_PAGE, "rb") as f:
                    body = f.read()
            except OSError:
                return super().send_error(code, message, explain)
            self.send_response(404, message)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            if self.command != "HEAD":
                self.wfile.write(body)
            return
        super().send_error(code, message, explain)


class ReusableTCPServer(socketserver.TCPServer):
    allow_reuse_address = True


def main():
    hostname = socket.gethostname()
    try:
        ip = socket.gethostbyname(hostname)
    except socket.gaierror:
        ip = "127.0.0.1"
    with ReusableTCPServer(("", PORT), SiteHandler) as httpd:
        print(f"Serving {DOCS_DIR} on http://{ip}:{PORT} (404 -> 404.html)")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down serve.py...")


if __name__ == "__main__":
    main()
