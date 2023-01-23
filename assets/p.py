from NeuroPy import NeuroPy 
from gpiozero import LED 
from time import sleep 
import time 
import os
from gpiozero import LED
from gpiozero import AngularServo 
from aiy.pins import PIN_A 
from aiy.pins import PIN_B 
from aiy.pins import PIN_C
from aiy.pins import PIN_D 
from aiy.pins import LED_1

neuropy = Neuropy()
neuropy.start()
led = LED(LED_1)
servo1 = AngularServo(PIN_A, min_angle=0, max_angle=180, min_pulse_width=.0005)
servo2 = AngularServo(PIN_B, min_angle=0, max_angle=180, min_pulse_width=.0005)
servo3 = AngularServo(PIN_C, min_angle=0, max_angle=180, min_pulse_width=.0005)
servo4 = AngularServo(PIN_D, min_angle=0, max_angle=180, min_pulse_width=.0005)
start_time = 0
blinked = False #11 blink is detected
last_blink_time = 0
double_blink = False
triple_blink = False
servoselect = 0
while True:
#print ("meditation="+str (neuropy.meditation))
    print ("atteb="+str (neuropy.attention))
    if neuropy.attention > 60:
        if servoselect == 1:
        servol.angle=170
        print ("moving robot arm finger 1")
        if servoselect == 2:
        servo2.angle=170
        print ("moving robot arm finger 2")
        if servoselect == 3:
        servo3.angle=170
        print ("Moving robot wrist")
        11 servoselect == 4:
        print ("Moving robot thumb")
        servo4.angle=170
        11 neuropy.attention < 60:
        1 servoselect == 1:
        servo1. angle=0
        print ("moving robot arm finger 1 position" )
        if servoselect == 2:
        servo2.angle=0
        print ("moving robot arm finger 2 position")
        if servoselect == 3:
        servo3. angle=0
        print ("Moving robot wrist position" )
        if servoselect == 4:
print ("Moving robot thumb Position")
servo4. angle=0
#print ("rawvalue="+str (neuropy.rawvalue))
#print ("blinkstrength="+ str (neuropy.blinkStrength))
value = neuropy.rawValue
if value > 100: #if the raw level gets above 200, which indicates a spike,
start_time = time.clock()
if start_time:
1f value < -100: #1f the spike in brain activity is over
total_time = time.clock() - start_time #how long the spike was
print ("blink")
start time = 0
1 0.01 < total_time > 0.040:
print ("Servo select signal. servoselect=servoselect+1
I
print (servoselect)
1f (servoselect >= 5):
servoselect=0
sleep(0.2)