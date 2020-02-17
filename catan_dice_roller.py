#Catan Dice Roller v1
#FEB 16, 2020

import RPi.GPIO as GPIO
import time
from random import randrange
import os
import shutil
from decimal import *

#Global Variables
roll_count = [0]
d1_rolls = [0]
d2_rolls = [0]
total_rolls = [0]
roll_logs = [0]

#Maps
decoder1 = [40,38,37,36]
decoder2 = [35,33,32,31]
decoder3 = [29,22,18,16]
decoder4 = [15,13,12,11]
blank = [GPIO.LOW,GPIO.HIGH,GPIO.LOW,GPIO.HIGH]
num = {0: [GPIO.LOW,GPIO.LOW,GPIO.LOW,GPIO.LOW],
       1: [GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.LOW],
       2: [GPIO.LOW,GPIO.HIGH,GPIO.LOW,GPIO.LOW],
       3: [GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.LOW],
       4: [GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.LOW],
       5: [GPIO.HIGH,GPIO.LOW,GPIO.HIGH,GPIO.LOW],
       6: [GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW],
       7: [GPIO.HIGH,GPIO.HIGH,GPIO.HIGH,GPIO.LOW],
       8: [GPIO.LOW,GPIO.LOW,GPIO.LOW,GPIO.HIGH],
       9: [GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH]}

#Save Button Function
def save_button(channel):
    #Blank Displays
    for x in range(0,4):
        GPIO.output(decoder1[x],blank[x])
        GPIO.output(decoder2[x],blank[x])
        GPIO.output(decoder3[x],blank[x])
        GPIO.output(decoder4[x],blank[x])
    time.sleep(1)
    #Display all 8s to denote roll log save
    for x in range(0,4):
        GPIO.output(decoder1[x],num[8][x])
        GPIO.output(decoder2[x],num[8][x])
        GPIO.output(decoder3[x],num[8][x])
        GPIO.output(decoder4[x],num[8][x])
    #Save Roll Log
    logs = str(roll_logs.count(1))
    log = open(r"/home/pi/roll_logs/roll_log" + logs + ".txt","w+")
    count = roll_count.count(1) + 1
    for x in range(1,count):
        d1 = d1_rolls[x]
        d2 = d1_rolls[x]
        tot = total_rolls[x]
        line = ("\nRoll " + str(x) + "   Dice 1: " + str(d1) + "   Dice 2: " + str(d2) + "   Total Roll: " + str(tot))
        log.writelines(line)
    #Add Game Summary
    #Dice 1 Roll Totals
    line = ("\n\nDice 1 Roll Summary")
    log.writelines(line)
    for x in range(1,7):
        number = d1_rolls.count(x)
        getcontext().prec = 4
        dec = (Decimal(number)/Decimal(count))*100
        line = ("\n" + str(x) + ": " + str(number) + "   " + str(dec) + "%")
        log.writelines(line)
    #Dice 2 Roll Totals
    line = ("\n\nDice 2 Roll Summary")
    log.writelines(line)
    for x in range(1,7):
        number = d2_rolls.count(x)
        getcontext().prec = 4
        dec = (Decimal(number)/Decimal(count))*100
        line = ("\n" + str(x) + ": " + str(number) + "   " + str(dec) + "%")
        log.writelines(line)
    #Total Roll Totals
    line = ("\n\nTotal Roll Summary")
    log.writelines(line)
    for x in range(2,13):
        number = total_rolls.count(x)
        getcontext().prec = 4
        dec = (Decimal(number)/Decimal(count))*100
        line = ("\n" + str(x) + ": " + str(number) + "   " + str(dec) + "%")
        log.writelines(line)
    log.close()
    roll_count.clear()
    roll_count.append(0)
    d1_rolls.clear()
    d1_rolls.append(0)
    d2_rolls.clear()
    d2_rolls.append(0)
    total_rolls.clear()
    total_rolls.append(0)
    roll_logs.append(1)
    print("Roll Log Saved")  #for testing
    time.sleep(3)
    #Blank Displays
    for x in range(0,4):
        GPIO.output(decoder1[x],blank[x])
        GPIO.output(decoder2[x],blank[x])
        GPIO.output(decoder3[x],blank[x])
        GPIO.output(decoder4[x],blank[x])
    time.sleep(1)

#Reset Button Function
def reset_button(channel):
    #Blank Displays
    for x in range(0,4):
        GPIO.output(decoder1[x],blank[x])
        GPIO.output(decoder2[x],blank[x])
        GPIO.output(decoder3[x],blank[x])
        GPIO.output(decoder4[x],blank[x])
    time.sleep(1)
    #Display all 0s to denote roll log reset
    for x in range(0,4):
        GPIO.output(decoder1[x],num[0][x])
        GPIO.output(decoder2[x],num[0][x])
        GPIO.output(decoder3[x],num[0][x])
        GPIO.output(decoder4[x],num[0][x])
    #Reset Roll Logs
    shutil.rmtree(r"/home/pi/roll_logs")
    os.mkdir(r"/home/pi/roll_logs")
    roll_logs.clear()
    roll_logs.append(1)
    print("Values Reset")  #for testing
    time.sleep(3)
    #Blank Displays
    for x in range(0,4):
        GPIO.output(decoder1[x],blank[x])
        GPIO.output(decoder2[x],blank[x])
        GPIO.output(decoder3[x],blank[x])
        GPIO.output(decoder4[x],blank[x])
    time.sleep(1)

#Roll Button Function
def roll_button(channel):
    dice1 = randrange(1,7)
    dice2 = randrange(1,7)
    total = dice1 + dice2
    roll_count.append(1)
    roll = roll_count.count(1)
    d1_rolls.append(dice1)
    d2_rolls.append(dice2)
    total_rolls.append(total)
    #for testing
    print("Dice 1: " + str(dice1) + "   Dice 2: " + str(dice2) + "   Total Roll: " + str(total))
    print("Roll Nummber: " + str(roll))
    #Blank Displays
    for x in range(0,4):
        GPIO.output(decoder1[x],blank[x])
        GPIO.output(decoder2[x],blank[x])
        GPIO.output(decoder3[x],blank[x])
        GPIO.output(decoder4[x],blank[x])
    time.sleep(1)
    #Output Rolls
    if total < 10:
        for x in range(0,4):
            GPIO.output(decoder3[x],blank[x])
            GPIO.output(decoder1[x],num[dice1][x])
            GPIO.output(decoder2[x],num[dice2][x])
            GPIO.output(decoder4[x],num[total][x])
    else:
        dig1 = int(total / 10)
        dig2 = int(total % 10)
        for x in range(0,4):
            GPIO.output(decoder1[x],num[dice1][x])
            GPIO.output(decoder2[x],num[dice2][x])
            GPIO.output(decoder3[x],num[dig1][x])
            GPIO.output(decoder4[x],num[dig2][x])
    time.sleep(3)

#Turn Button Function
def turn_button(channel):
    turn_dice = randrange(1,7)
    #fr testing
    print("Turn Roll: " + str(turn_dice))
    #Blank Displays
    for x in range(0,4):
        GPIO.output(decoder1[x],blank[x])
        GPIO.output(decoder2[x],blank[x])
        GPIO.output(decoder3[x],blank[x])
        GPIO.output(decoder4[x],blank[x])
    time.sleep(1)
    #Output Turn Roll
    for x in range(0,4):
        GPIO.output(decoder4[x],num[turn_dice][x])
    time.sleep(3)

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(7,GPIO.OUT) #Blanking
GPIO.output(7,GPIO.HIGH)

#Set up decoders
for x in range(0,4):
    GPIO.setup(decoder1[x],GPIO.OUT)
    GPIO.output(decoder1[x],GPIO.LOW)
    GPIO.setup(decoder2[x],GPIO.OUT)
    GPIO.output(decoder2[x],GPIO.LOW)
    GPIO.setup(decoder3[x],GPIO.OUT)
    GPIO.output(decoder3[x],GPIO.LOW)
    GPIO.setup(decoder4[x],GPIO.OUT)
    GPIO.output(decoder4[x],GPIO.LOW)

#Blank Displays
for x in range(0,4):
    GPIO.output(decoder1[x],blank[x])
    GPIO.output(decoder2[x],blank[x])
    GPIO.output(decoder3[x],blank[x])
    GPIO.output(decoder4[x],blank[x])
time.sleep(3)  

#Set up Buttons
GPIO.setup(8,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #save
GPIO.setup(10,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #reset
GPIO.setup(19,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #roll
GPIO.setup(21,GPIO.IN,pull_up_down=GPIO.PUD_DOWN) #turn

#Butten Event Detection
GPIO.add_event_detect(8,GPIO.RISING,callback=save_button)
GPIO.add_event_detect(10,GPIO.RISING,callback=reset_button)
GPIO.add_event_detect(19,GPIO.RISING,callback=roll_button)
GPIO.add_event_detect(21,GPIO.RISING,callback=turn_button)

#TESTING
message = input("Enter to Quit\n\n")
GPIO.cleanup()
