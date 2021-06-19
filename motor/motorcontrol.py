from time import sleep
import RPi.GPIO as GPIO

PUL = 17
DIR = 27
ENA = 22

GPIO.setmode(GPIO.BCM)
# GPIO.setmode(GPIO.BOARD) # Do NOT use GPIO.BOARD mode. Here for comparison only. 
#
GPIO.setup(PUL, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)

durationFwd = 5000 # This is the duration of the motor spinning. used for forward direction
durationBwd = 5000 # This is the duration of the motor spinning. used for reverse direction

delay = 0.0000001 # This is actualy a delay between PUL pulses - effectively sets the motor rotation speed.

