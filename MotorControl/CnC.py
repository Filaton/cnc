#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
from stepHAL import stepper
from MotorHal import motor


class CnC(object):
    '''
        Klasse, die deine gesamte Cocktailmaschine repäsentiert
    '''

    def __init__(self,stepper1: stepper,stepper2: stepper,motor_pusher: motor, pump1: motor, pump2: motor, pump3: motor, pump4: motor, pump5: motor, pump6: motor, pump7: motor):
        self.motor_vertical = stepper1
        self.motor_horizontal = stepper2
        self.motor_getränk = motor_pusher
        self.pumps = [pump1, pump2, pump3, pump4, pump5, pump6, pump7]
        self.driveToStart()  
        self.HOEHE = 100
        self.BREITE = 100
  

    def __del__(self):
        GPIO.cleanup()

    def driveToStart(self):
        self.motor_vertical.spin_duration("Backward",40)
        self.motor_horizontal.spin_duration("Backward",40)
        self.currentPos = 0

    def driveTo(self, target):
        '''
        Funktion um zu einer Flasche zu fahren
        
        Parameter:
            target: Ziel Position
                Mögliche Werte: Ganze Zahl zwischen 0 und 15
        Return Values:
            0: Success
            1: Target out of Bounce
        '''
        if self.currentPos == target:
            return 0
        if target < 0 or target > 15:
            return 1
        target_vert = target%4
        target_hori = target/4
        currentPos_vert = self.currentPos%4
        currentPos_hori = self.currentPos/4
        if(target_vert > currentPos_vert):
            drive_vert = target_vert-currentPos_vert
            drive_vert = (self.HOEHE/4) * drive_vert
            self.motor_vertical.spin_HalfTurns("Forward", drive_vert/2)
        elif(target_vert < currentPos_vert):
            drive_vert = currentPos_vert-target_vert
            drive_vert = (self.HOEHE/4) * drive_vert
            self.motor_vertical.spin_HalfTurns("Backward", drive_vert/2)
        if(target_hori > currentPos_hori):
            drive_hori = target_hori-currentPos_hori
            drive_hori = (self.HOEHE/4) * drive_hori
            self.motor_horizontal.spin_HalfTurns("Forward", drive_hori/2)
        elif(target_hori < currentPos_hori):
            drive_hori = currentPos_hori-target_hori
            drive_hori = (self.HOEHE/4) * drive_hori
            self.motor_horizontal.spin_HalfTurns("Backward", drive_hori/2)
        self.currentPos = target
        return 0

    def getDrink_Bottle(self):
        '''
        Funtkion um den Augießer zu leeren

        Return Values:
            0: success
        '''
        self.motor_getränk.run("Forward")
        time.sleep(5)
        self.motor_getränk.run("Backward")
        return 0

    def getDrink_Kanister(self, number, duration):
        '''
        Funktion um die Pumpen zu aktivieren

        Parameter:
            number: nummer der Pumpe (aus der Config)
                Mögliche Werte: ganze Zahlen größer null
            duration: Dauer in ganzen Sekunden
                Mögliche Werte: ganze Zahlen größer null
            Return Values:
                0: success
                2: keine valide Duration
        '''
        return self.pumps[number].run("Forward", duration)