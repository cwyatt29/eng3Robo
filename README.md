# Engineering 3 DE Project 1 THE ROBOT ARM
Our robot arm is differnt than the traditional robotic arm. We will make a gantry/cartesain arm. We are doing this because we need the bot to lift a fair amount of weight.

## TOC

* [Phase 1, Design](##Phase_1,_Design)
* [Phase 2,Salvage](##Phase_2,_Salvage)
* [Phase 3, Proof of Concept](##Phase_3,_Proof_of_Concept)
* [Magnet assembly](##Magnet_assembly)
* [Structure assembly](##Structure_assembly)
* [Phase 4 Code](##Phase_4_Code)
* [Phase 5 Working Project](##Phase_5_Working_Project)
* [Consistant Issues](#consistantissues)
---
## Sources

* [*Mr. Electron*](https://www.youtube.com/channel/UCWFbPzBb7dCyCWuBA-DBrMA)
* [*ElectroBOOM*](https://www.youtube.com/channel/UCJ0-OtVpF0wOKEqT2Z1HEtA)
* [*Schematix*](https://www.youtube.com/c/schematix)
*

### Here is a link to our teams drive which includes our planning documents and progress pictures.
[Drive](https://drive.google.com/drive/folders/1I6fFhtFFOL1zxpiJaQFnsx5c7EQsh9a1)

---
## Phase_1,_Design

When designing our project we had two things in mind. The first was a scrap magnet, the magnet would be very important for picking up and dropping our metal objects. The second was a Shipping container crane, we were going to model our robot off of these cranes. Our goal was to pick up and transport metal objects, we would need both of these to acheive our goal.





---

## Phase_2,_Salvage

From our research we learned that the simplest way of creating an electro-magnet was to take a transformer out of a microwave and modify it, we go into more detail on how it works in  [Magnet assembly](##Magnet_assembly). I had had the skeleton of a 3d printer at my house which would work perfectly as the body of the robot. 

![Microwave Pics](https://github.com/cwyatt29/eng3Robo/blob/master/images/Microwave%20Pic%201.PNG)

![Transformer Pics](https://github.com/cwyatt29/eng3Robo/blob/master/images/Transformer%20Pic%201.PNG)

---

## Phase_3,_Proof_of_Concept 

We were able to get our POC done very quickly because we had gathered all the necessary parts to make both the magnet and robot within 2 weeks. I regcret rushing into making the magnet because I think that we couldve made a stronger and nicer looking magnet if we had more time.

![Proof Video](https://github.com/cwyatt29/eng3Robo/blob/master/images/Z%20motor%20Proof_Trim.mp4)

---

## Magnet_assembly

To make our magnet we referenced Schematix's [Video](https://www.youtube.com/watch?v=DT0QHsN3vcE) on converting transformers to elctromagnets. This video was the main video we used to build our magnet. In his video he connected his magnet to multiple different power sources but we needed a source that could be mobile. To solve this problem we used a 18v drill battery. We also learned when it comes to hold strenght the AMPS are what matter. One of our biggest issues was overheating which we expect came from a short in our transformer coils. The temperature would heat to 200 F in about 10 seconds.We never stopped the heating but we added a fan that may help the magnet cool down, we also had to upgrade the connection wire because they would burn out extremly fast. This didnt seem like a common issue so we think its something to do with the magnet itself or possibly the power source.

---

## Structure_assembly

The 3d printer was already in a shape that would work for us so we only needed to do some small modifications. We removed the print bed, nossle, electrtonics, and 2 of the stepper motors. We then mounted one of the stronger steppers to the Y axis because we knew it would have to lift a lot of weight.

---

## Phase_4_Code

```python

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
    #smoothvalue = smoothing.update(int(simpleio.map_range(pot.value,0,65535,0,5500)))
    #smoothvalue = int(simpleio.map_range(pot.value,0,65535,0,4500))
    

    smoothvalue = int(simpleio.map_range(smoothing.update(pot.value),0,65535,0,4500))
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






## Phase_5_Working_Project

```
---
## Consistant_Issues

* Power
* Motors
* Wiring
* Overheating


---

## Final Product


![Electro-Mag On](https://github.com/cwyatt29/eng3Robo/blob/master/images/Magnet%20Working%20Pic.jpg)
![Electro-Mag Off](https://github.com/cwyatt29/eng3Robo/blob/master/images/Electromag%20Robot%20Pic%201.jpg)



---


## Refelection 

