import os
import RPi.GPIO as GPIO
import time

eight = [GPIO.LOW,GPIO.LOW,GPIO.LOW,GPIO.HIGH]
zero = [GPIO.LOW,GPIO.LOW,GPIO.LOW,GPIO.LOW]

decoder1 = [40,38,37,36]
decoder2 = [35,33,32,31]
decoder3 = [29,22,18,16]
decoder4 = [15,13,12,11]

GPIO.setup(7,GPIO.OUT)
GPIO.output(7,GPIO.LOW)
GPIO.output(7,GPIO.HIGH)

for x in range(0,4):
    GPIO.setup(decoder1[x],GPIO.OUT)
    GPIO.output(decoder1[x],GPIO.LOW)
    GPIO.setup(decoder2[x],GPIO.OUT)
    GPIO.output(decoder2[x],GPIO.LOW)
    GPIO.setup(decoder3[x],GPIO.OUT)
    GPIO.output(decoder3[x],GPIO.LOW)
    GPIO.setup(decoder4[x],GPIO.OUT)
    GPIO.output(decoder4[x],GPIO.LOW)

#Display all 8s
for x in range(0,4):
    GPIO.output(decoder1[x],eight[x])
    GPIO.output(decoder2[x],eight[x])
    GPIO.output(decoder3[x],eight[x])
    GPIO.output(decoder4[x],eight[x])
time.sleep(1)

#Display all 0s
for x in range(0,4):
    GPIO.output(decoder1[x],zero[x])
    GPIO.output(decoder2[x],zero[x])
    GPIO.output(decoder3[x],zero[x])
    GPIO.output(decoder4[x],zero[x])
time.sleep(1)

#Display all 8s
for x in range(0,4):
    GPIO.output(decoder1[x],eight[x])
    GPIO.output(decoder2[x],eight[x])
    GPIO.output(decoder3[x],eight[x])
    GPIO.output(decoder4[x],eight[x])
time.sleep(1)

os.system("sudo python3 /home/pi/catan_dice_roller/catan_dice_roller.py")
GPIO.cleanup()
