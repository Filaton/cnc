#!/usr/bin/python3
import RPi.GPIO as GPIO
import time

class stepper(object):
    '''
    Klasse um einen Steppermoter zu steuern
    Parameter:
        Genutzte PINS:
            Direction,
            Enable
            Puls
    Die GPIO-Nummerierung wird auf BCM geändert!
    Die gegebenen Pins werden auf Ausgang gesetzt
    '''
    def __init__(self, DIR_Pin, ENA_Pin, PUL_Pin):
        self.DIR_PIN = DIR_Pin
        self.ENA_PIN = ENA_Pin
        self.PUL_PIN = PUL_Pin
        #GPIO.setWarnings(False)
        GPIO.setmode(GPIO.BCM)          #BCM Nummerierung
        GPIO.setup(self.ENA_PIN, GPIO.OUT)    #PINS auf Ausgang setzen
        GPIO.setup(self.DIR_PIN, GPIO.OUT)       
        GPIO.setup(self.PUL_PIN, GPIO.OUT)

    def __del__(self):
        GPIO.cleanup()

    def spin_FullTurns(self, Direction, Turns = 1, Speed = 0.0006):
        '''
        Funktion um den Motor eine Anzahl Umdrehungen, Turns, vollführen zu lassen

        Parameter:
            Direction: Richtung in die der Motor drehen soll
                Mögliche Werte: "Forward" oder "Backward" als String
            Turns: Anzahl der zu drehenden Umdrehungen
                Default: 1
                Mögliche Werte: Positive ganze Zahlen
            Speed: Zeit die zwischen den Pulsen gewartet werden soll in Sekunden
                Default: 0.0006
                Mögliche Werte: alles > 0.0006 Bei großen werten natürlich fraglich wie sinnvoll
        Return Values:
            0: Success
            1: Keine valide Richtung angegeben (Evtl falsch geschrieben?)
            2: Keine valide Umdrehungszahl gegeben
            3: Zu schnelles Tempo angegeben
        '''
        GPIO.output(self.ENA_PIN, GPIO.LOW)
        if(Direction == "Forward"):
            GPIO.output(self.DIR_PIN, GPIO.LOW)
        elif(Direction == "Backward"):
            GPIO.output(self.DIR_PIN, GPIO.HIGH)
        else:
            print("No Valid Direction")
            return 1
        if(Turns < 0 or Turns%1 != 0):
            print("Cannot turn negativ")
            return 2
        if(Speed < 0.0006):
            print("Speed to fast")
            return 3
        turn = 0
        while turn != Turns:
            temp = 0
            while temp < 400:
                GPIO.output(self.PUL_PIN, GPIO.LOW)
                time.sleep(Speed)
                GPIO.output(self.PUL_PIN, GPIO.HIGH)
                time.sleep(Speed)
                temp = temp +1
            turn = turn + 1
        GPIO.output(self.ENA_PIN, GPIO.HIGH)
        return 0

    def spin_HalfTurns(self, Direction, Turns = 1, Speed = 0.0006):
        '''
        Funktion um den Motor eine Anzahl halber Umdrehungen, Turns, vollführen zu lassen

        Parameter:
            Direction: Richtung in die der Motor drehen soll
                Mögliche Werte: "Forward" oder "Backward" als String
            Turns: Anzahl der zu drehenden halben Umdrehungen
                Default: 1
                Mögliche Werte: Positive ganze Zahlen
            Speed: Zeit die zwischen den Pulsen gewartet werden soll in Sekunden
                Default: 0.0006
                Mögliche Werte: alles > 0.0006 Bei großen werten natürlich fraglich wie sinnvoll
        Return Values:
            0: Success
            1: Keine valide Richtung angegeben (Evtl falsch geschrieben?)
            2: Keine valide Umdrehungszahl gegeben
            3: Zu schnelles Tempo angegeben
        '''
        GPIO.output(self.ENA_PIN, GPIO.LOW)
        if(Direction == "Forward"):
            GPIO.output(self.DIR_PIN, GPIO.LOW)
        elif(Direction == "Backward"):
            GPIO.output(self.DIR_PIN, GPIO.HIGH)
        else:
            print("No Valid Direction")
            return 1
        if(Turns < 0 or Turns%1 != 0):
            print("Cannot turn negativ")
            return 2
        if(Speed < 0.0006):
            print("Speed to fast")
            return 3
        turn = 0
        while turn != Turns:
            temp = 0
            while temp < 200:
                GPIO.output(self.PUL_PIN, GPIO.LOW)
                time.sleep(Speed)
                GPIO.output(self.PUL_PIN, GPIO.HIGH)
                time.sleep(Speed)
                temp = temp +1
            turn = turn + 1
        GPIO.output(self.ENA_PIN, GPIO.HIGH)
        return 0

    def spin_duration(self, Direction, duration = 1, Speed = 0.0006):
        '''
        Funktion um den Motor eine vorgegebene Dauer rotieren zu lassen
        Parameter:
            Direction: Richtung in die der Motor drehen soll
                Mögliche Werte: "Forward" oder "Backward" als String
            duration: Dauer, in der er sich drehen soll in ganzen Sekunden
                Default: 1
                Mögliche Werte: Positive ganze Zahlen
            Speed: Zeit die zwischen den Pulsen gewartet werden soll in Sekunden
                Default: 0.0006
                Mögliche Werte: alles > 0.0006 Bei großen werten natürlich fraglich wie sinnvoll
        Return Values:
            0: Success
            1: Keine valide Richtung angegeben (Evtl falsch geschrieben?)
            2: Keine valide Umdrehungszahl gegeben
            3: Zu schnelles Tempo angegeben
        '''
        GPIO.output(self.ENA_PIN, GPIO.LOW)
        if(Direction == "Forward"):
            GPIO.output(self.DIR_PIN, GPIO.LOW)
        elif(Direction == "Backward"):
            GPIO.output(self.DIR_PIN, GPIO.HIGH)
        else:
            print("No Valid Direction")
            return 1
        if(duration < 0 or duration%1 != 0):
            print("Duration cannot be negative")
            return 2
        if(Speed < 0.0006):
            print("Speed to fast")
            return 3
        turn = 0
        start_time = time.perf_counter()
        stop_time = start_time + duration
        while time.perf_counter() < stop_time:
            GPIO.output(self.PUL_PIN, GPIO.LOW)
            time.sleep(Speed)
            GPIO.output(self.PUL_PIN, GPIO.HIGH)
            time.sleep(Speed)
        GPIO.output(self.ENA_PIN, GPIO.HIGH)
        return 0

if __name__ == "__main__":
    print("Als Default werden folgende Pins verwendet:")
    print("ENABLE = 2\nDIR = 4\nPULS = 3")
    Test = stepper(2,3,4)
    Test.spin_FullTurns("Backward",Turns = 300)
    