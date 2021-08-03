#!/usr/bin/python3
from Websocket.RequestHandler import ServerHandler
from MotorControl.CnC import cnc
import socketserver

list_Alk = ["test1_1","test1_2","test1_3","test1_4","test2_1","test2_2","test2_3","test2_4","test3_1","test3_2","test3_3","test3_4","test4_1","test4_2","kanister","test4_4"]
list_Kan = ["KAN1","KAN2","KAN3","KAN4","KAN5","KAN6"]
cnc = cnc(list_Alk,list_Kan,2,3,4,27,22,17,5,6,13)
class Handler(ServerHandler):
    def doAlk(self, ArrID, ID):
        list_Alk[ArrID] = ID
        cnc.setKonfig_Bottle(list_Alk)

    def doKan(self, ArrID, ID):
        list_Kan[ArrID] = ID
        cnc.setKonfig_Bottle(list_Kan)

    def order(self, AlkID, KanID):
        List = AlkID + KanID
        cnc.orderDrink(List)


if __name__ == "__main__":
    Server = socketserver.TCPServer(("",8000),ServerHandler)
    Server.serve_forever()
