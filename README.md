# Engineering 3 DE Project 1 THE ROBOT ARM
Our robot arm is differnt than the traditional robotic arm. We will make a gantry/cartesain arm. We are doing this because we need the bot to lift a fair amount of weight.

## TOC

* [Design](#design)
* [Salvage](#salvage)
* [Proof of Concept](#proofofconcept)
* [Magnet assembly](#magnetassembly)
* [Structure assembly](#structureassembly)
* [Code](#code)
* [Consistant Issues](#consistantissues)
* [Final Product](#finalproduct)
* [Reflection](#refelection)

---
## Sources

* [*Mr. Electron*](https://www.youtube.com/channel/UCWFbPzBb7dCyCWuBA-DBrMA)
* [*ElectroBOOM*](https://www.youtube.com/channel/UCJ0-OtVpF0wOKEqT2Z1HEtA)
* [*Schematix*](https://www.youtube.com/c/schematix)
*

### Here is a link to our teams drive which includes our planning documents and progress pictures.
[Drive](https://drive.google.com/drive/folders/1I6fFhtFFOL1zxpiJaQFnsx5c7EQsh9a1)

---
## Design

When designing our project we had two things in mind. The first was a scrap magnet, the magnet would be very important for picking up and dropping our metal objects. The second was a Shipping container crane, we were going to model our robot off of these cranes. Our goal was to pick up and transport metal objects, we would need both of these to acheive our goal.

![Design Sketch](https://github.com/cwyatt29/eng3Robo/blob/master/images/Design%20Sketch.JPG)




---

## Salvage

From our research we learned that the simplest way of creating an electro-magnet was to take a transformer out of a microwave and modify it, we go into more detail on how it works in  [Magnet assembly](##Magnet_assembly). I had had the skeleton of a 3d printer at my house which would work perfectly as the body of the robot. 

![Microwave Pics](https://github.com/cwyatt29/eng3Robo/blob/master/images/Microwave%20Pic%201.PNG)

![Transformer Pics](https://github.com/cwyatt29/eng3Robo/blob/master/images/Transformer%20Pic%201.PNG)

---

## Proof_of_Concept 

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
The code was arguably the hardest part of this project. I spent a large amount of time fixing small bugs that were constantly appearing in my code. To start I was simply mapping a potentiometer and sending it's values to a stepper that was matching those values with it's steps. This was a simple solution that may have worked if the potentiometers were perfect. However, they are far from perfect. The potentiometers have too many values in a small range of motion so that they never settle to one specific value. This caused the stepper motor that we were using to shake back and forth uncontrollably. To stop this I found an online library called Smoothing.py. In a nutshell this library when implemented with a range of values took an average of a select few of those values and then rounded them to make them even. With a little bit of tweaking this "smoothed" the values and allowed them to settle on a whole number. This stopped the shaking in the stepper and allowed us to move it up and down smoothly. We could not have done this without the smoothing function in place to stop the shaking that would have inevitably burnt out the motor. 

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
## Consistent_Issues

* *Power*

We had many power issues throughout the project not only with the arduino but also with the magnet. The magnets issues were pretty quick to solve because all it needed was a battery that could put out enough amps. With the arduino many batteries kept dying because the stepper drew so much current. We decided to uses rechargeable lithium-ion batteries.


* *Motors*

About halfway through January we realized we werent going to be able to complete the drive motors because we were having so many issues with the code. So we decided to scrap the drive motors and opt for caster wheels. These wheels were simple to mount and havent given us any issue so far.

* *Wiring*

Because we were constantly changing the plans the wiring would change more than once a week which was not ideal becasuse it was easy to forget to plug something in then we would spend the whole class trying to figure out why it wouldnt move which was not an effeiceint use of our time. Near the end of our allocated assembly time we agreed on a wiring set up that we wouldnt change.
* *Overheating* 

Our magnet had another issue, overheating. We used a thermal camera to get a reading a our magnet was heating up to 220F in about ten seconds when it was powered. This was not ideal because the idea was to be able to carry heavy metal parts over small distances. We knew that without some counter measures the magnet would eventually become unsafe to use. We werent able to fully stop the over heating but we did add a small fan to cool it and we upgraded our wires so they could handle more current without melting.


---

## Final_Product


![Electro-Mag On](https://github.com/cwyatt29/eng3Robo/blob/master/images/MAGNET%20ON%202.jpg)
This picture shows that our robot was able to pic up and hold ten lbs of weight with no issue.
![Electro-Mag Off](https://github.com/cwyatt29/eng3Robo/blob/master/images/MAGNET%20OFF%201.jpg) Here is one last look at our project. It is more than 3 feet tall, weights 15 lbs, and is run off 36 Volts of power from 3 different batteries.



---


## Refelection 

Our design changed probally five or six times over the course of the whole project. I wish that we wouldve just stuck with one specific design. I think that at the start we thought that the code wouldnt be very challenging but nobody in our group had worked with steppers so it took us much longer to get our project running. By the time we did we didnt have time to make two more steppers run. Next time I will just use motors and make a gear box when I need more torque. I was very happy that we were able to reuse many parts from the 3d printer and use the motors that were already on there. In hindsight I definently regret not spending more time carefully removing the transformer and modifying it. I feel we couldve gotten a much stronger magnet if we had been more careful to not damage it. Even though the magnet could've been stronger it was still able to lift 6 lbs.
