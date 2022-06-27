import socketserver
import http.server # Our http server handler for http requests
import socketserver # Establish the TCP Socket connections
from derivative import Derivative

class DispatchRequestHandler(http.server.BaseHTTPRequestHandler):

    def __init__(self, request: bytes, client_address: tuple[str, int], server: socketserver.BaseServer) -> None:
        self._derivative = object        # To be overriden
        super().__init__(request, client_address, server)

    # WE OVERRIDE THE HANDLING PROCESS TO CREATE A REDIRECT PROCESS DEPENDING ON THE ROUTES IN THE DERIVATIVE OBJECT

def EnableDerivative(handler = DispatchRequestHandler, PORT = 5259):
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print("Http Server Serving at port", PORT)
        httpd.serve_forever()
        return httpd

