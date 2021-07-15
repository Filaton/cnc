#!/usr/bin/python3

from MotorHal import Motor
from stepHal import stepper
import socketserver
import http.server

HEIGHT = 600
WIDTH = 400
DIFFROW = HEIGHT/4
DIFFCOL = WIDTH/4

class cnc(object):
    def __init__(self, reihenfolge_,_
    DIR_Pin_Row, ENA_Pin_Row, PUL_Pin_Row,_
    DIR_Pin_Col, ENA_Pin_Col, PUL_Pin_Col,_
    IN1_Pin_PUSH, IN2_Pin_PUSH, EN_Pin_PUSH):
        self.order = reihenfolge_
        self.rowMotor = stepper(DIR_Pin_Row, ENA_Pin_Row, PUL_Pin_Row)
        self.colMotor = stepper(DIR_Pin_Col, ENA_Pin_Col, PUL_Pin_Col)
        self.pusher =   Motor(IN1_Pin_PUSH, IN2_Pin_PUSH, EN_Pin_PUSH)
        self.currPosRow = 0
        self.currPosCol = 0


    #def __del__(self):

    def driveTo(bottle):
        row = self.order.index(bottle)/4
        col = self.order.index(bottle)%4

        #
        #   in die Reihe fahren
        #
        driveWay = Destination - self.currPosRow
        if(driveWay > 0):
            dir = "Forward"
        elif(driveWay < 0):
            dir = "Backward"
        driveWay = abs(driveWay)*DIFFROW
        self.rowMotor.spinHalfTurns(dir, (driveWay/2))

        #
        #   in die Spalte fahren
        #
        driveWay = Destination - self.currPosCol
        if(driveWay > 0):
            dir = "Forward"
        elif(driveWay < 0):
            dir = "Backward"
        else:
            return
        driveWay = abs(driveWay)*DIFFCOL
        self.colMotor.spinHalfTurns(dir, (driveWay/2))



    def orderDrink(self, bottles):
        for bottle in bottles:
            self.driveTo(bottle)
        
        



if __name__ == "__main__":

    ownCnC = cnc(ownlist)
    ownCnC.orderDrink()
    
    
