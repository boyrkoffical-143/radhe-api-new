from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if "/api/number" in self.path:
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()

            response = {
                "status": "success",
                "name": "Radhe Gupta",
                "city": "Mithapur",
                "number": "9998887779"
            }

            self.wfile.write(str(response).encode())
        else:
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"API Running ✅")
