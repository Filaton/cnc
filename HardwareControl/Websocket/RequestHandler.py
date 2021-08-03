#!/usr/bin/python3
import http.server
from http import HTTPStatus
import socketserver
import logging
from multiprocessing import Process
import json

#logging.basicConfig(filename="./log.log", format='%(asctime)s %(message)s', level=logging.INFO)
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
socketserver.TCPServer.allow_reuse_address = True
CommandList = ["KONFIG_ALK", "KONFIG_KAN", "ORDER"]


class ServerHandler(http.server.BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(HTTPStatus.OK.value)
        self.send_header('Content-type', 'application/json')
        # Allow requests from any origin, so CORS policies don't
        # prevent local development.
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write(json.dumps({"Hello": "There!"}).encode('utf-8'))

    def doAlk(self, ArrID, ID):
        pass

    def doKan(self, ArrID, ID):
        pass

    def order(self, AlkID, KanID):
        pass

    def do_POST(self):
        length = int(self.headers.get('content-length'))
        message = json.loads(self.rfile.read(length))
        try:
            command = message["Befehl"]
            if not command in CommandList:
                raise KeyError
            if command is "KONFIG_ALK":
                self.doAlk(message["ArrID"], message["ID"])
            elif command is "KONFIG_KAN":
                self.doKan(message["ArrID"], message["ID"])
            elif command is "ORDER":
                self.order(message["Zutaten_Alk"], message["Zutaten_Kan"])
            
        
        except KeyError:
            logging.debug("no Valid CnC Command!")
            self._set_headers()
            self.wfile.write(json.dumps({'success': False, 'message': "no valid CnC-Command!"}).encode())
            return
        self._set_headers()
        self.wfile.write(json.dumps({'success': True}).encode('utf-8'))

    def do_OPTIONS(self):
        # Send allow-origin header for preflight POST XHRs.
        self.send_response(HTTPStatus.NO_CONTENT.value)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST')
        self.send_header('Access-Control-Allow-Headers', 'content-type')
        self.end_headers()

if __name__ == "__main__":
    Server = socketserver.TCPServer(("",8000),ServerHandler)
    Server.serve_forever()

    
    
    
    
    #r = RequestHandler(tempCommand,True)
    #
    #r.join()



