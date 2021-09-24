from time import sleep
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW)


GPIO.output(GPIO.HIGH)
time.sleep(20)
GPIO.output(8, GPIO.LOW)
                   




