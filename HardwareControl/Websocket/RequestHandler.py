#!/usr/bin/python3
import http.server
import socketserver
import logging
from multiprocessing import Process
import json
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
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
    def do_HEAD(self):
        self._set_headers()
        
    # GET sends back a Hello world message
    def do_GET(self):
        self._set_headers()
        self.wfile.write(json.dumps({'hello': 'world', 'received': 'ok'}).encode())
        
    # POST echoes the message adding a JSON field
    def do_POST(self):
        ctype, pdict = cgi.parse_header(self.headers.get('content-type'))
        
        # refuse to receive non-json content
        if ctype != 'application/json':
            self.send_response(400)
            self.end_headers()
            return
            
        # read the message and convert it into a python dictionary
        length = int(self.headers.get('content-length'))
        message = json.loads(self.rfile.read(length))
        
        # add a property to the object, just to mess with data
        message['received'] = 'ok'
        
        # send the message back
        self._set_headers()
        self.wfile.write(json.dumps(message).encode())

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



