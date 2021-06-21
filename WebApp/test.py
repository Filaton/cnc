import socketserver
from http.server import HTTPServer, SimpleHTTPRequestHandler


class ServerHandler(SimpleHTTPRequestHandler):
    # Server Handler, der im Server die Post-Requests empfängt und verarbeitet

    def do_GET(self):
        self.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        post_data = post_data.decode("utf-8")
        print(post_data)

    def _html(self, message):
        """This just generates an HTML document that includes `message`
        in the body. Override, or re-write this do do more interesting stuff.
        """
        content = f"<html><body><h1>{message}</h1></body></html>"
        return content.encode("utf8")  # NOTE: must return a bytes object!

if __name__ == "__main__":
            handler = ServerHandler
            myServer = socketserver.TCPServer(("", 50000), handler)
            print("starting...")
            myServer.serve_forever()