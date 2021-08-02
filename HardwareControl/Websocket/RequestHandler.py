#!/usr/bin/python3
import http.server
from http import HTTPStatus
import socketserver
import logging
from multiprocessing import Process
import json
import time
import cgi 

#logging.basicConfig(filename="./log.log", format='%(asctime)s %(message)s', level=logging.INFO)
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
socketserver.TCPServer.allow_reuse_address = True

def standard_func(input):
    return "0"

CommandList = {
    "null": standard_func
}



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

    def do_POST(self):
        length = int(self.headers.get('content-length'))
        message = json.loads(self.rfile.read(length))
        message['date_ms'] = int(time.time()) * 1000
        self._set_headers()
        self.wfile.write(json.dumps({'success': True}).encode('utf-8'))

    def do_OPTIONS(self):
        # Send allow-origin header for preflight POST XHRs.
        self.send_response(HTTPStatus.NO_CONTENT.value)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST')
        self.send_header('Access-Control-Allow-Headers', 'content-type')
        self.end_headers()

class RequestHandler(object):
    """
    RequestHandler HandlerClass for extended Abstraction

    Args:
        commandList_setter ([FunctionList]): [Contains a function-Dict, containing all possible CommandNames and used Functions]
    """
    def __init__(self,commandList_setter, start):
        global CommandList
        CommandList = commandList_setter
        Server = socketserver.TCPServer(("localhost",8000),ServerHandler)
        self.process = Process(target=Server.serve_forever())
        if ( start == True):
            self.start_server()
    
    def start_server(self):
        self.process.start()
    
    def join(self):
        self.process.join()

def test(input):
    logging.debug("in TEST")
    return "DONE"

tempCommand = {
    "test": test
}

if __name__ == "__main__":
    Server = socketserver.TCPServer(("",8000),ServerHandler)
    Server.serve_forever()

    
    
    
    
    #r = RequestHandler(tempCommand,True)
    #
    #r.join()



