import os
from http.server import BaseHTTPRequestHandler, HTTPServer


def get_port() -> int:
    """Берём порт из env PORT, по умолчанию 8000."""
    port_str = os.environ.get("PORT", "8000")
    try:
        port = int(port_str)
    except ValueError:
        raise ValueError(f"Invalid PORT value: {port_str!r}. Must be an integer.")
    if not (0 < port < 65536):
        raise ValueError(f"PORT out of range: {port}. Must be between 1 and 65535.")
    return port


class TodoRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(b"Not Found")

    # чтобы не спамить логами о каждом запросе, можно переопределить log_message
    def log_message(self, format, *args):
        return  # убираем стандартный шум в stderr / логах


def run():
    port = get_port()
    server_address = ("0.0.0.0", port)  # слушаем на всех интерфейсах
    httpd = HTTPServer(server_address, TodoRequestHandler)

    # Эта строка должна попасть в логи при старте
    print(f"Server started in port {port}", flush=True)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        httpd.server_close()


if __name__ == "__main__":
    run()
