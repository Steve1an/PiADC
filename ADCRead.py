import RPi.GPIO as IO
import time
import numpy as np
IO.setwarnings(True)
IO.setmode (IO.BOARD)

IO.setup(40,IO.IN)
IO.setup(38,IO.IN)
IO.setup(37,IO.IN)
IO.setup(36,IO.IN)
IO.setup(35,IO.IN)
IO.setup(33,IO.IN)
IO.setup(32,IO.IN)
IO.setup(31,IO.IN)
IO.setup(29,IO.IN)
IO.setup(26,IO.IN)
IO.setup(24,IO.OUT)
IO.setup(23,IO.OUT)
IO.setup(22,IO.OUT)
IO.setup(21,IO.OUT)


IO.output(21,0) #to diable sleep mode of the ADC
IO.output(24,1) #SELECT
IO.output(23,0) #CHIP SELECT
IO.output(22,0) #CLOCK

D=np.arange(0,10)
sum=0
while 1:
 IO.output(22,1) #Rise the clock

 D=D*0
 if(IO.input(26) == True):
  D[9]=1
 if(IO.input(29) == True):
  D[8]=1
 if(IO.input(31) == True):
  D[7]=1
 if(IO.input(32) == True):
  D[6]=1
 if(IO.input(33) == True):
  D[5]=1
 if(IO.input(35) == True):
  D[4]=1
 if(IO.input(36) == True):
  D[3]=1
 if(IO.input(37) == True):
  D[2]=1
 if(IO.input(38) == True):
  D[1]=1
 if(IO.input(40) == True):
  D[0]=1
 time.sleep(0.01)
 IO.output(22,0) #Clock falling
 sum=D[9]*512+D[8]*256+D[7]*128+D[6]*64+D[5]*32+D[4]*16+D[3]*8+D[2]*4+D[1]*2+D[0]
 print(sum)
 print(D)
 time.sleep(0.01)
