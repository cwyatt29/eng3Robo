import time
from adafruit_motor import stepper 
import board
from analogio import AnalogIn
import digitalio
import pwmio
import simpleio
import lib.smoothing
 
pot2 = AnalogIn(board.A1) 
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
coils2 = (
    digitalio.DigitalInOut(board.D7),  # A1
    digitalio.DigitalInOut(board.D6),  # A2
    digitalio.DigitalInOut(board.D4),  # B1
    digitalio.DigitalInOut(board.D5),  # B2
)

for coil in coils:
    coil.direction = digitalio.Direction.OUTPUT
for coil in coils2: 
    coil.direction = digitalio.Direction.OUTPUT

smoothing = lib.smoothing.MovingAverage()
Steps= 0 
motor = stepper.StepperMotor(coils[0], coils[1], coils[2], coils[3], microsteps=None)
motor2 = stepper.StepperMotor(coils2[0], coils2[1], coils2[2], coils2[3], microsteps=None)

while True:
    smoothvalue = smoothing.update(int(simpleio.map_range(pot.value,0,65535,0,5000)))
    smoothvalue2 = smoothing.update(int(simpleio.map_range(pot2.value,0,65535,0,4800)))
    print(smoothvalue, Steps) 

    
    
    
    if abs(smoothvalue - Steps) >4 and limit.value == True:
        
         
        if smoothvalue > Steps :
           motor.onestep (direction=stepper.BACKWARD, style=stepper.DOUBLE)
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