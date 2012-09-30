import os as os
import time as time
import RPi.GPIO as GPIO
from flask import Flask
from flask import json
from flask import request
from flask import render_template

app = Flask(__name__)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.output(7, False)

def blink(count):
	print 'count = ' + str(count) + '\r\n'
	for i in range(3):
		GPIO.output(7, True)
		time.sleep(.25)
		GPIO.output(7, False)
		time.sleep(.25)
		print 'i = ' + str(i) + '\r\n'

def ding():
	os.system('mpg123 /home/pi/work/ding.mp3')
	

@app.route('/', methods=['GET', 'POST'])
def root():

	if request.method == 'POST':

		method = request.form['method']

		if method == 'blink':
			count = int(request.form['count'])
			blink(count)

		if method == 'ding':
			ding()

		return render_template('index.html')

	if request.method == 'GET':

		return render_template('index.html') 

if __name__ == '__main__':
	app.debug = True
	app.run('0.0.0.0')
