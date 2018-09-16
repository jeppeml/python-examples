import RPi.GPIO as GPIO
import time
import thread
import sys


yellow = 18
green = 19
blue = 13
red = 12
btn = 21
btn_close = 16

waiting = 0.001

leds = {yellow, green, blue, red}

GPIO.setmode(GPIO.BCM)

is_running = False

for led in leds:
	GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW)

GPIO.setup(btn, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(btn_close, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def blinker(base_time, end_number):
	is_running = True;
	waitings = [base_time ** i for i in range(end_number)] # 2, 2**2,2**3,2**4, 2**5
	for n in waitings:
		print (n, 1.0/n)
		for i in range(1,n):
			sleep_time = 1.0/n
			for led in leds:
				GPIO.output(led, GPIO.HIGH)
				time.sleep(sleep_time)
				GPIO.output(led, GPIO.LOW)
				time.sleep(sleep_time)
	is_running=False

def pushbtn(channel):
    if not is_running:
		print("Button pressed")
		thread.start_new_thread(blinker,(2,5))
    else:
		print ("Hey, leds are already running!")
        
# starting event in new thread            
GPIO.add_event_detect(btn, GPIO.RISING, callback=pushbtn, bouncetime=300)

print ("Running...")
# main thread
while True:
	try:
		res = GPIO.wait_for_edge(btn_close, GPIO.RISING, timeout=50000)
		if res is None:
			print('Press green button to quit... ')
		else:
			print('Quitting')
			print "Bye"
			sys.exit()
	except KeyboardInterrupt:
		print "Bye"
		sys.exit()
	pass



	

