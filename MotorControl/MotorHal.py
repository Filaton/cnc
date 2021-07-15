#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

<<<<<<< HEAD:MotorHal.py
class Motor(object):
=======
class motor(object):
>>>>>>> 17bd87c1d3328f3af8da960bd2d5905f343900a2:MotorControl/MotorHal.py
    def __init__(self, IN1_Pin, IN2_Pin, EN_Pin):
        self.IN1_Pin = IN1_Pin
        self.IN2_Pin = IN2_Pin
        self.EN_Pin = EN_Pin
        #GPIO.setWarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.IN1_Pin, GPIO.OUT)
        GPIO.setup(self.IN2_Pin, GPIO.OUT)
        GPIO.setup(self.EN_Pin, GPIO.OUT)
        self.pwmHandle = GPIO.PWM(EN_Pin, 1000)
        self.pwmHandle.start(0)

    def __del__(self):
        GPIO.cleanup()

    def run(self, Direction, Duration = 5):
        '''
        Funktion um den Motor eine gewisse Dauer drehen zu lassen
        Blockende Funktion

        Parameter:
            Direction: Richtung in die der Motor drehen soll
                Mögliche Werte: "Forward" oder "Backward" als String
            Duration: Dauer, in ganzen Sekunden, die er sich drehen soll
                Default: 5
                Mögliche Werte: Positive ganze Zahlen
        Return Values:
            0: Success
            1: Keine valide Richtung angegeben (Evtl falsch geschrieben?)
        '''
        if(Direction == "Forward"):
            GPIO.output(self.IN1, GPIO.HIGH)
            GPIO.output(self.IN2, GPIO.LOW)
        elif(Direction == "Backward"):
            GPIO.output(self.IN1, GPIO.LOW)
            GPIO.output(self.IN2, GPIO.HIGH)
        else:
            print("no valid direction")
            return 1
        self.pwmHandle.changeDutyCycle(100)
        time.sleep(Duration)
        self.pwmHandle.changeDutyCycle(0)
        return 0

<<<<<<< HEAD:MotorHal.py
    def run_speed(self, Direction, Duration = 5, speed = 100):
        '''
        Funktion um den Motor eine gewisse Dauer drehen zu lassen
        Blockende Funktion
=======
        def run_speed(self, Direction, Duration = 5, speed = 100):
            '''
            Funktion um den Motor eine gewisse Dauer drehen zu lassen
            Blockende Funktion
>>>>>>> 17bd87c1d3328f3af8da960bd2d5905f343900a2:MotorControl/MotorHal.py

            Parameter:
                Direction: Richtung in die der Motor drehen soll
                    Mögliche Werte: "Forward" oder "Backward" als String
                Duration: Dauer, in ganzen Sekunden, die er sich drehen soll
                    Default: 5
                    Mögliche Werte: Positive ganze Zahlen
                speed: Geschwindigkeit mit der der Motor drehen soll
                    Default: 100
                    Mögliche Werte: 0-100
            Return Values:
                0: Success
                1: Keine valide Richtung angegeben (Evtl falsch geschrieben?)
                2: Keine zulässige Geschwindigkeit angegeben
            '''
        if(Direction == "Forward"):
            GPIO.output(self.IN1, GPIO.HIGH)
            GPIO.output(self.IN2, GPIO.LOW)
        elif(Direction == "Backward"):
            GPIO.output(self.IN1, GPIO.LOW)
            GPIO.output(self.IN2, GPIO.HIGH)
        else:
            print("no valid direction")
            return 1
        if(speed<0 or 100<speed):
            print("no valid speed param")
            return 2
        self.pwmHandle.changeDutyCycle(100)
        time.sleep(Duration)
        self.pwmHandle.changeDutyCycle(0)
        return 0