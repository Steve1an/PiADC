import RPi.GPIO as IO
import time
import numpy as np
IO.setwarnings(True)
IO.setmode(IO.BOARD)

IO.setup(40,IO.IN)
IO.setup(38,IO.IN)
IO.setup(37,IO.OUT)
IO.setup(36,IO.IN)
IO.setup(35,IO.IN)
IO.setup(33,IO.IN)
IO.setup(32,IO.IN)
IO.setup(31,IO.IN)
IO.setup(29,IO.IN)
IO.setup(26,IO.OUT)
IO.setup(24,IO.OUT)
IO.setup(23,IO.IN)
IO.setup(22,IO.IN)
IO.setup(21,IO.IN)
IO.setup(19,IO.IN)
IO.setup(16,IO.IN)
IO.setup(15,IO.IN)
IO.setup(13,IO.IN)
IO.setup(12,IO.OUT)
IO.setup(11,IO.IN)
IO.setup(10,IO.OUT)
IO.setup(8,IO.IN)
IO.setup(7,IO.OUT)
IO.setup(5,IO.IN)
IO.setup(3,IO.IN)


IO.output(10,0) #SELECT
IO.output(7,0) #CLOCK

D=np.arange(0,12)
sum=0
while True:
 IO.output(7,1) #Rise the clock
 time.sleep(0.001)
 t1=time.time()
 D=D*0
 if(IO.input(3) == True):
  D[11]=1
 else:
  D[11]=0
 if(IO.input(5) == True):
  D[10]=1
 else:
  D[10]=0
 if(IO.input(8) == True):
  D[9]=1
 else:
  D[9]=0
 if(IO.input(11) == True):
  D[8]=1
 else:
  D[8]=0
 if(IO.input(13) == True):
  D[7]=1
 else:
  D[7]=0
 if(IO.input(15) == True):
  D[6]=1
 else:
  D[6]=0
 if(IO.input(19) == True):
  D[5]=1
 else:
  D[5]=0
 if(IO.input(21) == True):
  D[4]=1
 else:
  D[4]=0
 if(IO.input(23) == True):
  D[3]=1
 else:
  D[3]=0
 if(IO.input(29) == True):
  D[2]=1
 else:
  D[2]=0
 if(IO.input(31) == True):
  D[1]=1
 else:
  D[1]=0
 if(IO.input(33) == True):
  D[0]=1
 else:
  D[0]=0
 t2=time.time()
 Fs=1/(t2-t1)
 IO.output(7,0) #Clock falling
 sum=D[11]*2048+D[10]*1024+D[9]*512+D[8]*256+D[7]*128+D[6]*64+D[5]*32+D[4]*16+D[3]*8+D[2]*4+D[1]*2+D[0]
 print(sum)
 print(D)
 print(Fs)
 time.sleep(0.2)
