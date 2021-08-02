#!/usr/bin/python3
import http.server
import socketserver
import logging
from multiprocessing import Process

#logging.basicConfig(filename="./log.log", format='%(asctime)s %(message)s', level=logging.INFO)
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
socketserver.TCPServer.allow_reuse_address = True

def standard_func(input):
    return "0"

CommandList = {
    "null": standard_func
}



class ServerHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        logging.debug(self.version_string())
        logging.debug("PostRequestHandler - Start")
        global CommandList
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        self.data = self.rfile.read(content_length).strip() # <--- Gets the data itself
        logging.debug(self.data)
        #func = CommandList.get(post_data[0])
        #ret_data = func(post_data[1])
        self.wfile.write(self._html(self.data))
        logging.debug("Post Request Handled - RETURNING")

    def _html(self, message):
        """This just generates an HTML document that includes `message`
        in the body. Override, or re-write this do do more interesting stuff.
        """
        content = f"<html><body><h1>{message}</h1></body></html>"
        return content.encode("utf8")  # NOTE: must return a bytes object!

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



