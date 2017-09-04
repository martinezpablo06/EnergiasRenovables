import serial
import time
import RPi.GPIO as GPIO
import kivy
kivy.require('1.0.6') # replace with your current kivy version !

from kivy.config import Config
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.slider import Slider
from kivy.clock import Clock
from kivy.graphics import Color, Rectangle

arduino = serial.Serial('/dev/ttyUSB0', baudrate=9600)
Config.set('input', 'hid_%(name)s',  'probesysfs,provider=hidinput,param=rotation=270,param=invert_y=1')
Config.write()
swState = "000"
buttonPin = 12 
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
button1 = ToggleButton(text="button1")
button2 = ToggleButton(text="button2")
button3 = ToggleButton(text="button3")

def press_callback(obj):
	if obj.text == 'button1':		
		if(swState[0] == '0'):
			obj.state = "normal"
		elif(swState[0] == '1'):
			if(obj.state == "normal"):
				print ("button 1 off")
				print (swState)
				arduino.write('2')
			elif(obj.state == "down"):
				print ("button 1 on")
				print (swState)
				arduino.write('1')

	if obj.text == 'button2':		
		if(swState[1] == '0'):
			obj.state = "normal"
		elif(swState[1] == '1'):
			if(obj.state == "normal"):
				print ("button 2 off")
				print (swState)
				arduino.write('12')
			elif(obj.state == "down"):
				print ("button 2 on")
				print (swState)
				arduino.write('11')
	
	if obj.text == 'button3':		
		if(swState[2] == '0'):
			obj.state = "normal"
		elif(swState[2] == '1'):
			if(obj.state == "normal"):
				print ("button 3 off")
				print (swState)
				arduino.write('48')
			elif(obj.state == "down"):
				print ("button 3 on")
				print (swState)
				arduino.write('47')

class InputButton(Button):
    def update(self, dt):
		global swState		
		if GPIO.input(buttonPin) == True:
			self.state = 'normal'
		else:
			self.state = 'down'
			arduino.write('99')
			auxswState = ""
			while arduino.inWaiting()>0:
				auxswState+=arduino.read(1)
			if (len(auxswState) >= 3):
				global swState
				swState = auxswState
				print (swState)
			time.sleep(0.1)
			arduino.write('99')
			auxswState = ""
			while arduino.inWaiting()>0:
				auxswState+=arduino.read(1)
			if (len(auxswState) >= 3):
				swState = auxswState
				print (swState)
			time.sleep(0.1)
			i = 0
			global button1
			global button2
			global button3
			if(swState[0] == '0'):
			 	button1.state = "normal"
			if(swState[1] == '0'):
			 	button2.state = "normal"
			if(swState[2] == '0'):
			 	button3.state = "normal"
			
class MyApp(App):

	def build(self):
		# Set up the layout:
		layout = GridLayout(cols=4, spacing=20, padding=40, rows=2)

		with layout.canvas.before:
			Color(.2,.2,.2,1)
			self.rect = Rectangle(size=(1920,1080), pos=layout.pos)
            
		button1.bind(on_press=press_callback)
		button2.bind(on_press=press_callback)
		button3.bind(on_press=press_callback)
		bti = InputButton(text="bti")

		Clock.schedule_interval(bti.update, 1.0/10.0)
		#layout.add_widget(bti)

		layout.add_widget(button1)
		layout.add_widget(button2)
		layout.add_widget(button3)

		return layout

if __name__ == '__main__':
	MyApp().run()
