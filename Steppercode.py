# SPDX-FileCopyrightText: 2018 Anne Barela for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import time
from adafruit_motor import stepper 
import board
from analogio import AnalogIn
import digitalio
import pwmio
import simpleio
import lib.smoothing
 

pot = AnalogIn(board.A0)
STEPS = 200 
limit = digitalio.DigitalInOut(board.D8) 
limit.direction = digitalio.Direction.INPUT 
limit.pull = digitalio.Pull.UP 

coils = (
    digitalio.DigitalInOut(board.D12),  # A1
    digitalio.DigitalInOut(board.D11),  # A2
    digitalio.DigitalInOut(board.D9),  # B1
    digitalio.DigitalInOut(board.D10),  # B2
)


for coil in coils:
    coil.direction = digitalio.Direction.OUTPUT

smoothing = lib.smoothing.Smoothing()
Steps= 0 
motor = stepper.StepperMotor(coils[0], coils[1], coils[2], coils[3], microsteps=None)


while True:
    smoothvalue = smoothing.update(int(simpleio.map_range(pot.value,0,65535,0,5500)))
    #smoothvalue = int(simpleio.map_range(pot.value,0,65535,0,4500))
    

    #smoothvalue = int(simpleio.map_range(smoothing.update(pot.value),0,65535,0,4500))
    print(smoothvalue, Steps) 
    #print(limit.value) 
    
    
    if abs(smoothvalue - Steps) >4 and limit.value == True:
        #print(smoothvalue, Steps) 
        
        if smoothvalue > Steps :
           motor.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
           Steps = Steps +1       
        time.sleep(.001)  


        if smoothvalue < Steps: 
           motor.onestep(style=stepper.DOUBLE, direction= stepper.FORWARD)
           Steps = Steps -1          
        time.sleep(.001) 
    
    if limit.value == False:
        Steps = 4500 

     
 
     
#while target != steps
    #if target is > steps
        #move stepper up one step and add 1 to steps 