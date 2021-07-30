from http.server import HTTPServer
from http.server import SimpleHTTPRequestHandler
import socketserver
import logging
from multiprocessing import Process

logging.basicConfig(filename="./log.log", format='%(asctime)s %(message)s', level=logging.INFO)
logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
socketserver.TCPServer.allow_reuse_address = True

def standard_func():
    return "0"

CommandList = {
    "null": standard_func
}



class ServerHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        logging.debug("PostRequestHandler - Start")
        global CommandList
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        post_data = self.rfile.read(content_length) # <--- Gets the data itself
        post_data = post_data.decode("utf-8")
        post_data = post_data.split(';')
        func = CommandList.get(post_data[0])
        ret_data = func(post_data[1])
        self.wfile.write(ret_data.encode("utf-8"))
        logging.debug("Post Request Handled - RETURNING")

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

def test():
    return "DONE"

tempCommand = {
    "test": test
}

if __name__ == "__main__":
    r = RequestHandler(tempCommand,True)
    r.join()



