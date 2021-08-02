#!/usr/bin/python3

from MotorHal import Motor
from stepHAL import stepper
import socketserver
import http.server
import math
import time

HEIGHT = 500
WIDTH = 500
DIFFROW = HEIGHT/4
DIFFCOL = WIDTH/4

class cnc(object):
    def __init__(self, reihenfolge_, reihenfolge_kan,
    DIR_Pin_Row, ENA_Pin_Row, PUL_Pin_Row,
    DIR_Pin_Col, ENA_Pin_Col, PUL_Pin_Col,
    IN1_Pin_PUSH, IN2_Pin_PUSH, EN_Pin_PUSH):
        self.order = reihenfolge_
        self.order_kan = reihenfolge_kan
        self.rowMotor = stepper(DIR_Pin_Row, ENA_Pin_Row, PUL_Pin_Row)
        self.colMotor = stepper(DIR_Pin_Col, ENA_Pin_Col, PUL_Pin_Col)
        self.pusher =   Motor(IN1_Pin_PUSH, IN2_Pin_PUSH, EN_Pin_PUSH)
        self.currPosRow = 0
        self.currPosCol = 0


    def __del__(self):
        self.rowMotor.__del__()
        self.colMotor.__del__()
        self.pusher.__del__()

    def driveTo(self, bottle):
        if(bottle in self.order_kan):
            bottle = "getränke"
        print(self.order.index(bottle))
        row = math.floor(self.order.index(bottle)/4)
        col = self.order.index(bottle)%4
        dir = "none"
        #
        #   in die Reihe fahren
        #
        driveWay = row - self.currPosRow
        if(driveWay > 0):
            dir = "Forward"
        elif(driveWay < 0):
            dir = "Backward"
        driveWay = abs(driveWay)*DIFFROW
        print(dir)
        print(driveWay)
        self.rowMotor.spin_HalfTurns(dir, math.floor(driveWay/2))
        self.currPosRow = row
        print("row driven")
        driveWay = col - self.currPosCol
        if(driveWay > 0):
            dir = "Forward"
        elif(driveWay < 0):
            dir = "Backward"
        driveWay = abs(driveWay)*DIFFCOL
        print(dir)
        print(driveWay)
        self.colMotor.spin_HalfTurns(dir, math.floor(driveWay/2))
        self.currPosCol = col
        print("col driven")

        self.pusher.run("Forward")
        input()
        time.sleep(10)
        self.pusher.run("Backward")
    
    def getDrink(self, bottle): #TODO Implement Function!
        if(bottle in order_kan):
            #Activate Pumps to get specified Ingredient
        elif(bottle in order):
            #Activate Pusher to get specified Ingredient
        else:
            return "1"

    def orderDrink(self, bottles):
        for bottle in bottles:
            print("driving to Bottle:" + bottle)
            self.driveTo(bottle)
            self.getDrink(bottle)
            print("driven to bottle")

    def setKonfig_Bottle(self, newOrder):
        self.order = newOrder

if __name__ == "__main__":
    ownlist = ["test1_1","test1_2","test1_3","test1_4","test2_1","test2_2","test2_3","test2_4","test3_1","test3_2","test3_3","test3_4","test4_1","test4_2","kanister","test4_4"]
    ownCnC = cnc(ownlist,["test","test2"]2,3,4,27,22,17,5,6,13)
    input()
    ownCnC.orderDrink(["test1_1", "test2"])