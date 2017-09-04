
import serial
import time
import RPi.GPIO as GPIO
import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.slider import Slider
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle



arduino = serial.Serial('/dev/ttyUSB0', baudrate=9600)
#arduino.open()

swState = "000"

# Define some helper functions:

# This callback will be bound to the LED toggle and Beep button:
def press_callback(obj):
	arduino.write('0')	
	arduino.flush()
        auxswState = ""
	time.sleep(0.1)
	while arduino.inWaiting()>0:
		auxswState+=arduino.read(1)
	swState = auxswState
	if obj.text == 'button1':		
		if(swState[0] == '0'):
			obj.state = "normal"
		elif(swState[0] == '1'):
			#obj.disabled = not obj.disabled 
			if(obj.state == "normal"):
				print ("button 1 off")
				print (swState)
				arduino.write('2')
				#GPIO.output(ledPin, GPIO.LOW)
			elif(obj.state == "down"):
				print ("button 1 on")
				print (swState)
				arduino.write('1')
				#GPIO.output(ledPin, GPIO.HIGH)

	if obj.text == 'button2':		
		if(swState[1] == '0'):
			obj.state = "normal"
		elif(swState[1] == '1'):
			#obj.disabled = not obj.disabled 
			if(obj.state == "normal"):
				print ("button 2 off")
				print (swState)
				arduino.write('12')
				#GPIO.output(ledPin, GPIO.LOW)
			elif(obj.state == "down"):
				print ("button 2 on")
				print (swState)
				arduino.write('11')
				#GPIO.output(ledPin, GPIO.HIGH)
	
	if obj.text == 'button3':		
		if(swState[2] == '0'):
			obj.state = "normal"
		elif(swState[2] == '1'):
			#obj.disabled = not obj.disabled 
			if(obj.state == "normal"):
				print ("button 3 off")
				print (swState)
				arduino.write('48')
				#GPIO.output(ledPin, GPIO.LOW)
			elif(obj.state == "down"):
				print ("button 3 on")
				print (swState)
				arduino.write('47')
				#GPIO.output(ledPin, GPIO.HIGH)

bti = InputButton(text="bti")
        Clock.schedule_interval(bti.update, 1.0/10.0)
        layout.add_widget(bti)

class InputButton(Button):
    def update(self, dt):
        if GPIO.input(buttonPin) == True:
            self.state = 'normal'
        else:
            self.state = 'down'

class MyApp(App):

	def build(self):
		# Set up the layout:
		layout = GridLayout(cols=4, spacing=20, padding=40, rows=2)

		# Make the background gray:
		with layout.canvas.before:
			Color(.2,.2,.2,1)
			self.rect = Rectangle(size=(1920,1080), pos=layout.pos)
            
            bti = InputButton(text="bti")
            Clock.schedule_interval(bti.update, 1.0/10.0)
            layout.add_widget(bti)

		button1 = ToggleButton(text="button1")
		button1.bind(on_press=press_callback)

		button2 = ToggleButton(text="button2")
		button2.bind(on_press=press_callback)

		button3 = ToggleButton(text="button3")
		button3.bind(on_press=press_callback)

		layout.add_widget(button1)
		layout.add_widget(button2)
		layout.add_widget(button3)

		return layout

if __name__ == '__main__':
	MyApp().run()
