import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO_TRIGGER1 = 18
GPIO_ECHO1 = 11
GPIO_TRIGGER2 = 3
GPIO_ECHO2 = 7

GPIO.setup(GPIO_TRIGGER1, GPIO.OUT)
GPIO.setup(GPIO_ECHO1, GPIO.IN)
GPIO.setup(GPIO_TRIGGER2, GPIO.OUT)
GPIO.setup(GPIO_ECHO2, GPIO.IN)
GPIO.setup(10,GPIO.OUT)
def distance():
 GPIO.output(GPIO_TRIGGER1, True)
 time.sleep(0.00001)
 GPIO.output(GPIO_TRIGGER1, False)
 delay=0.00001
 time.sleep(delay)
 StartTime = time.time()
 StopTime = time.time()
 TimeOut1 = time.time()
 while GPIO.input(GPIO_ECHO1) == 0:
  StartTime = time.time()
  TimeOut2 = time.time()
  if TimeOut2-TimeOut1 > 0.01:
   break

 while GPIO.input(GPIO_ECHO1) == 1:
  StopTime = time.time()

 TimeElapsed = StopTime - StartTime
 distance = ((TimeElapsed - delay) * 34300)/2
 return distance

def distance2():
 GPIO.output(GPIO_TRIGGER2,True)
 time.sleep(0.00001)
 GPIO.output(GPIO_TRIGGER2, False)
 delay=0.00001
 time.sleep(delay)
 StartTime = time.time()
 StopTime = time.time()
 TimeOut1=time.time()
 while GPIO.input(GPIO_ECHO2) == 0:
  StarTime = time.time()
  TimeOut2= time.time()
  if TimeOut2-TimeOut1 > 0.01:
   break

 while GPIO.input(GPIO_ECHO2) == 1:
  StopTime = time.time()

 TimeElapsed = StopTime - StartTime
 distance = ((TimeElapsed - delay) * 34300)/2
 return distance

if __name__ == '__main__':
 try:
  while True:
   dist = distance()
   dist2 = 1000
   GPIO.output(10,False)
   if dist < 30 or dist2 < 25:
    GPIO.output(10,True)
   print ("Measured Distance1 = %.1f cm" % dist)
   print ("Measured Distance2 = %.1f cm" % dist2)
   time.sleep(0.1)

 except KeyboardInterrupt:
  print("Measuremtn stopped by User")
  GPIO.cleanup()
