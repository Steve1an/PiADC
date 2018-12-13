import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO_TRIGGER = 18
GPIO_ECHO = 11

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def distance():
 GPIO.output(GPIO_TRIGGER, True)
 time.sleep(0.00001)
 GPIO.output(GPIO_TRIGGER, False)
 delay=0.00001
 time.sleep(delay)
 StartTime = time.time()
 StopTime = time.time()

 while GPIO.input(GPIO_ECHO) == 0:
  StartTime = time.time()

 while GPIO.input(GPIO_ECHO) == 1:
  StopTime = time.time()

 TimeElapsed = StopTime - StartTime
 distance = ((TimeElapsed - delay) * 34300)/2
 return distance

if __name__ == '__main__':
 try: 
  while True:
   dist = distance()
   print ("Measured Distance = %.1f cm" % dist)
   time.sleep(1)

 except KeyboardInterrupt:
  print("Measuremtn stopped by User")
  GPIO.cleanup()