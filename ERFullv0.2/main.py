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
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.slider import Slider
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

arduino = serial.Serial('/dev/ttyACM0', baudrate=9600)
Config.set('input', 'hid_%(name)s',  'probesysfs,provider=hidinput,param=rotation=270,param=invert_y=1')
Config.write()

swState = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
rbswState = [0,0,0,0,0]
pulState = [0,0,0,0]

speed = 7

out21Pin  = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(out21Pin, GPIO.OUT)
GPIO.output(out21Pin, True)

out22Pin  = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(out22Pin, GPIO.OUT)
GPIO.output(out22Pin, True)

out23Pin  = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(out23Pin, GPIO.OUT)
GPIO.output(out23Pin, True)

out24Pin  = 23
GPIO.setmode(GPIO.BCM)
GPIO.setup(out24Pin, GPIO.OUT)
GPIO.output(out24Pin, True)

arduinoPin = 12 
GPIO.setmode(GPIO.BCM)
GPIO.setup(arduinoPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
pulsador1 =16
GPIO.setmode(GPIO.BCM)
GPIO.setup(pulsador1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
pulsador2 =  20
GPIO.setmode(GPIO.BCM)
GPIO.setup(pulsador2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
pulsador3 =  21
GPIO.setmode(GPIO.BCM)
GPIO.setup(pulsador3, GPIO.IN, pull_up_down=GPIO.PUD_UP)

sw1Pin = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(sw1Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
sw2Pin =19
GPIO.setmode(GPIO.BCM)
GPIO.setup(sw2Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
sw3Pin =  13
GPIO.setmode(GPIO.BCM)
GPIO.setup(sw3Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
sw4Pin =  6
GPIO.setmode(GPIO.BCM)
GPIO.setup(sw4Pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

button1 = ToggleButton(text="button1")
button2 = ToggleButton(text="button2")
button3 = ToggleButton(text="button3")
button4 = ToggleButton(text="button4")
button5 = ToggleButton(text="button5")
button6 = ToggleButton(text="button6")
button7 = ToggleButton(text="button7")
button8 = ToggleButton(text="button8")
button9 = ToggleButton(text="button9")
button10 = ToggleButton(text="button10")
button11 = ToggleButton(text="button11")
button12 = ToggleButton(text="button12")
button13 = ToggleButton(text="button13")
button14 = ToggleButton(text="button14")
button15 = ToggleButton(text="button15")
button16 = ToggleButton(text="button16")
button17 = ToggleButton(text="button17")
button18 = ToggleButton(text="button18")
button19 = ToggleButton(text="button19")
button20 = ToggleButton(text="button20")
button21 = ToggleButton(text="button21")
button22 = ToggleButton(text="button22")
button23 = ToggleButton(text="button23")
button24 = ToggleButton(text="button24")



lay1 = BoxLayout(spacing=10)

def update_speed(obj, value):
	global speed
	n = int (obj.value)
	print("Updating speed to:" + str(n))
	label1.text = str(n)

slider1 = Slider(orientation='horizontal', min=7, max=15, value=7,step=1,value_track=True, value_track_color=[0,128,128,0.7], size_hint=(.8,1))
slider1.bind(on_touch_down=update_speed, on_touch_move=update_speed)
label1 = Label(size_hint=(.2,1))


lay1.add_widget(label1)
lay1.add_widget(slider1)

popup = Popup(title='Button Popup', content=lay1, size_hint=(None,None), size=(800,200))

def press_callback(obj):
	
	if obj.text == 'button1':				
		global speed
		if(swState[1] == 0):
			obj.state = "normal"
			popup.dismiss()
		elif(swState[1] == 1):
			if(obj.state == "normal"):
				print ("button 1 off")
				print (swState)
				arduino.write('2')
				popup.dismiss()
			elif(obj.state == "down"):
				print ("button 1 on")
				print (swState)
				arduino.write('1')
				popup.open()

	if obj.text == 'button2':		
		if(swState[2] == 0):
			obj.state = "normal"
		elif(swState[2] == 1):
			if(obj.state == "normal"):
				print ("button 2 off")
				print (swState)
				arduino.write('4')
			elif(obj.state == "down"):
				print ("button 2 on")
				print (swState)
				arduino.write('3')
	
	if obj.text == 'button3':		
		if(swState[3] == 0):
			obj.state = "normal"
		elif(swState[3] == 1):
			if(obj.state == "normal"):
				print ("button 3 off")
				print (swState)
				arduino.write('6')
			elif(obj.state == "down"):
				print ("button 3 on")
				print (swState)
				arduino.write('5')

	if obj.text == 'button4':		
		if(swState[4] == 0):
			obj.state = "normal"
		elif(swState[4] == 1):
			if(obj.state == "normal"):
				print ("button 4 off")
				print (swState)
				arduino.write('8')
			elif(obj.state == "down"):
				print ("button 4 on")
				print (swState)
				arduino.write('7')

	if obj.text == 'button5':		
		if(swState[5] == 0):
			obj.state = "normal"
		elif(swState[5] == 1):
			if(obj.state == "normal"):
				print ("button 5 off")
				print (swState)
				arduino.write('10')
			elif(obj.state == "down"):
				print ("button 5 on")
				print (swState)
				arduino.write('9')

	if obj.text == 'button6':		
		if(swState[6] == 0):
			obj.state = "normal"
		elif(swState[6] == 1):
			if(obj.state == "normal"):
				print ("button 6 off")
				print (swState)
				arduino.write('12')
			elif(obj.state == "down"):
				print ("button 6 on")
				print (swState)
				arduino.write('11')

	if obj.text == 'button7':		
		if(swState[7] == 0):
			obj.state = "normal"
		elif(swState[7] == 1):
			if(obj.state == "normal"):
				print ("button 7 off")
				print (swState)
				arduino.write('14')
			elif(obj.state == "down"):
				print ("button 7 on")
				print (swState)
				arduino.write('13')

	if obj.text == 'button8':		
		if(swState[8] == 0):
			obj.state = "normal"
		elif(swState[8] == 1):
			if(obj.state == "normal"):
				print ("button 8 off")
				print (swState)
				arduino.write('16')
			elif(obj.state == "down"):
				print ("button 8 on")
				print (swState)
				arduino.write('15')

	if obj.text == 'button9':		
		if(swState[9] == 0):
			obj.state = "normal"
		elif(swState[9] == 1):
			if(obj.state == "normal"):
				print ("button 9 off")
				print (swState)
				arduino.write('18')
			elif(obj.state == "down"):
				print ("button 9 on")
				print (swState)
				arduino.write('17')

	if obj.text == 'button10':		
		if(swState[10] == 0):
			obj.state = "normal"
		elif(swState[10] == 1):
			if(obj.state == "normal"):
				print ("button 10 off")
				print (swState)
				arduino.write('20')
			elif(obj.state == "down"):
				print ("button 10 on")
				print (swState)
				arduino.write('19')

	if obj.text == 'button11':		
		if(swState[11] == 0):
			obj.state = "normal"
		elif(swState[11] == 1):
			if(obj.state == "normal"):
				print ("button 11 off")
				print (swState)
				arduino.write('22')
			elif(obj.state == "down"):
				print ("button 11 on")
				print (swState)
				arduino.write('21')

	if obj.text == 'button12':		
		if(swState[12] == 0):
			obj.state = "normal"
		elif(swState[12] == 1):
			if(obj.state == "normal"):
				print ("button 12 off")
				print (swState)
				arduino.write('24')
			elif(obj.state == "down"):
				print ("button 12 on")
				print (swState)
				arduino.write('23')
	
	if obj.text == 'button13':		
		if(swState[13] == 0):
			obj.state = "normal"
		elif(swState[13] == 1):
			if(obj.state == "normal"):
				print ("button 13 off")
				print (swState)
				arduino.write('26')
			elif(obj.state == "down"):
				print ("button 13 on")
				print (swState)
				arduino.write('25')

	if obj.text == 'button14':		
		if(swState[14] == 0):
			obj.state = "normal"
		elif(swState[14] == 1):
			if(obj.state == "normal"):
				print ("button 14 off")
				print (swState)
				arduino.write('28')
			elif(obj.state == "down"):
				print ("button 14 on")
				print (swState)
				arduino.write('27')

	if obj.text == 'button15':		
		if(swState[15] == 0):
			obj.state = "normal"
		elif(swState[15] == 1):
			if(obj.state == "normal"):
				print ("button 15 off")
				print (swState)
				arduino.write('30')
			elif(obj.state == "down"):
				print ("button 15 on")
				print (swState)
				arduino.write('29')

	if obj.text == 'button16':		
		if(swState[16] == 0):
			obj.state = "normal"
		elif(swState[16] == 1):
			if(obj.state == "normal"):
				print ("button 16 off")
				print (swState)
				arduino.write('32')
			elif(obj.state == "down"):
				print ("button 16 on")
				print (swState)
				arduino.write('31')

	if obj.text == 'button17':		
		if(swState[17] == 0):
			obj.state = "normal"
		elif(swState[17] == 1):
			if(obj.state == "normal"):
				print ("button 17 off")
				print (swState)
				arduino.write('34')
			elif(obj.state == "down"):
				print ("button 17 on")
				print (swState)
				arduino.write('33')

	if obj.text == 'button18':		
		if(swState[18] == 0):
			obj.state = "normal"
		elif(swState[18] == 1):
			if(obj.state == "normal"):
				print ("button 18 off")
				print (swState)
				arduino.write('36')
			elif(obj.state == "down"):
				print ("button 18 on")
				print (swState)
				arduino.write('35')

	if obj.text == 'button19':		
		if(swState[19] == 0):
			obj.state = "normal"
		elif(swState[19] == 1):
			if(obj.state == "normal"):
				print ("button 19 off")
				print (swState)
				arduino.write('38')
			elif(obj.state == "down"):
				print ("button 19 on")
				print (swState)
				arduino.write('37')

	if obj.text == 'button20':	
		if(swState[20] == 0):
			obj.state = "normal"
		elif(swState[20] == 1):
			if(obj.state == "normal"):
				print ("button 20 off")
				print (swState)
				arduino.write('40')
			elif(obj.state == "down"):
				print ("button 20 on")
				print (swState)
				arduino.write('39')

	if obj.text == 'button21':
		if(rbswState[1] == 0):
			obj.state = 'normal'
		elif(rbswState[1] == 1):
			if(obj.state == "normal"):
				print ("button 21 off")
				GPIO.output(out21Pin, True)
			elif(obj.state == "down"):
				print ("button 21 on")
				GPIO.output(out21Pin, False)

	if obj.text == 'button22':
		if(rbswState[2] == 0):
			obj.state = 'normal'
		elif(rbswState[2] == 1):
			if(obj.state == "normal"):
				print ("button 22 off")
				GPIO.output(out22Pin, True)
			elif(obj.state == "down"):
				print ("button 22 on")
				GPIO.output(out22Pin, False)

	if obj.text == 'button23':
		if(rbswState[3] == 0):
			obj.state = 'normal'
		elif(rbswState[3] == 1):
			if(obj.state == "normal"):
				print ("button 23 off")
				GPIO.output(out23Pin, True)
			elif(obj.state == "down"):
				print ("button 23 on")
				GPIO.output(out23Pin, False)

	if obj.text == 'button24':
		if(rbswState[4] == 0):
			obj.state = 'normal'
		elif(rbswState[4] == 1):
			if(obj.state == "normal"):
				print ("button 24 off")
				GPIO.output(out24Pin, True)
			elif(obj.state == "down"):
				print ("button 24 on")
				GPIO.output(out24Pin, False)



class InputButton1(Button):
    def update(self, dt):
		if GPIO.input(pulsador1) == True:
			self.state = 'normal'
		else:
			self.state = 'down'

class InputButton2(Button):
    def update(self, dt):
		if GPIO.input(pulsador2) == True:
			self.state = 'normal'
		else:
			self.state = 'down'

class InputButton3(Button):
    def update(self, dt):
		if GPIO.input(pulsador3) == True:
			self.state = 'normal'
		else:
			self.state = 'down'

class InputSW1(Button):
    def update(self, dt):
		if GPIO.input(sw1Pin) == True:
			global button21
			button21.state = "normal"
			rbswState [1] = 0
			GPIO.output(out21Pin, True)
		else:
			rbswState [1] = 1
			#GPIO.output(out21Pin, False)
	
class InputSW2(Button):
    def update(self, dt):
		if GPIO.input(sw2Pin) == True:
			global button22
			button22.state = "normal"
			rbswState [2] = 0
			GPIO.output(out22Pin, True)
		else:
			rbswState [2] = 1

class InputSW3(Button):
    def update(self, dt):
		if GPIO.input(sw3Pin) == True:			
			global button23
			button23.state = "normal"
			rbswState [3] = 0
			GPIO.output(out23Pin, True)	
		else:
			rbswState [3] = 1


class InputSW4(Button):
    def update(self, dt):
		if GPIO.input(sw4Pin) == True:
			global button24
			button24.state = "normal"
			rbswState [4] = 0
			GPIO.output(out24Pin, True)
		else:
			rbswState [4] = 1

class InputArduino(Button):
    def update(self, dt):

		if GPIO.input(arduinoPin) == True:
			self.state = 'normal'
		else:
			self.state = 'down'
			arduino.write('99')
			time.sleep(0.1)
			index = 0
			ini = 0
			c = '?' 
			while ( arduino.inWaiting()>0) :
				c = arduino.read(1)
				if (c == '#'):
					ini = 1;
					index = 0
				if ((ini == 1)and(c != '#')):
					if (c != '*'):
						global swState	
						swState[index] = int (c)
						index = index +1
					else:	
						ini = 0
						index = 0
			print (swState)

			global button1
			global button2
			global button3
			global button4
			global button5
			global button6
			global button7
			global button8
			global button9
			global button10
			global button11
			global button12
			global button13
			global button14
			global button15
			global button16
			global button17
			global button18
			global button19
			global button20

			if(swState[1] == 0):
			 	button1.state = "normal"
				global popup				
				popup.dismiss()
			if(swState[2] == 0):
			 	button2.state = "normal"
			if(swState[3] == 0):
			 	button3.state = "normal"
			if(swState[4] == 0):
			 	button4.state = "normal"
			if(swState[5] == 0):
			 	button5.state = "normal"
			if(swState[6] == 0):
			 	button6.state = "normal"
			if(swState[7] == 0):
			 	button7.state = "normal"
			if(swState[8] == 0):
			 	button8.state = "normal"
			if(swState[9] == 0):
			 	button9.state = "normal"
			if(swState[10] == 0):
			 	button10.state = "normal"
			if(swState[11] == 0):
			 	button11.state = "normal"
			if(swState[12] == 0):
			 	button12.state = "normal"
			if(swState[13] == 0):
			 	button13.state = "normal"
			if(swState[14] == 0):
			 	button14.state = "normal"
			if(swState[15] == 0):
			 	button15.state = "normal"
			if(swState[16] == 0):
			 	button16.state = "normal"
			if(swState[17] == 0):
			 	button17.state = "normal"
			if(swState[18] == 0):
			 	button18.state = "normal"
			if(swState[19] == 0):
			 	button19.state = "normal"
			if(swState[20] == 0):
			 	button20.state = "normal"

class MyApp(App):		
	def build(self):
		megalayout = BoxLayout(orientation='vertical',spacing=10)
		with megalayout.canvas.before:
			Color(.2,.2,.2,1)
			self.rect = Rectangle(size=(1024,600), pos=megalayout.pos)
			
			titlelayout = BoxLayout(orientation='horizontal',size_hint=(1,.2),spacing=10  )
			with titlelayout.canvas.before:
				title1 = BoxLayout(orientation='horizontal',size_hint=(.3,1))
				with title1.canvas.before:
					labo= Label(text='Generadoras')
					title1.add_widget(labo)
				title2 = BoxLayout(orientation='horizontal',size_hint=(.4,1))
				with title2.canvas.before:
					pullayout = BoxLayout(orientation='horizontal',size_hint=(1,1),spacing=10  )
					with pullayout.canvas.before:
						pullayout1 = BoxLayout(orientation='horizontal',size_hint=(.33,1))
						with pullayout1.canvas.before:
							pul1 = InputButton1(text="pulsador1")
							Clock.schedule_interval(pul1.update, 1.0/10.0)
							pullayout1.add_widget(pul1)
						pullayout2 = BoxLayout(orientation='horizontal',size_hint=(.33,1))
						with pullayout2.canvas.before:
							pul2 = InputButton2(text="pulsador2")
							Clock.schedule_interval(pul2.update, 1.0/10.0)
							pullayout2.add_widget(pul2)
						pullayout3 = BoxLayout(orientation='horizontal',size_hint=(.33,1))
						with pullayout3.canvas.before:
							pul3 = InputButton3(text="pulsador3")
							Clock.schedule_interval(pul3.update, 1.0/10.0)
							pullayout3.add_widget(pul3)
					pullayout.add_widget(pullayout1)
					pullayout.add_widget(pullayout2)
					pullayout.add_widget(pullayout3)

				title2.add_widget(pullayout)

				title3 = BoxLayout(orientation='horizontal',size_hint=(.3,1))
				with title3.canvas.before:
					labo2= Label(text='Consumidoras')
					title3.add_widget(labo2)

			#superlayout = GridLayout(cols=2,spacing=20,padding=40,rows=1)
			titlelayout.add_widget(title1)
			titlelayout.add_widget(title2)
			titlelayout.add_widget(title3)
			superlayout = BoxLayout(orientation='horizontal', spacing=10, size_hint=(1,.8) )
			with superlayout.canvas.before:
				layout1 = GridLayout(cols=3,rows=4, size_hint=(.42,1))
				with layout1.canvas.before:

					button1.bind(on_press=press_callback)
					button2.bind(on_press=press_callback)
					button3.bind(on_press=press_callback)
					button4.bind(on_press=press_callback)
					button5.bind(on_press=press_callback)
					button6.bind(on_press=press_callback)
					button7.bind(on_press=press_callback)
					button8.bind(on_press=press_callback)
					button9.bind(on_press=press_callback)

					layout1.add_widget(button1)
					layout1.add_widget(button2)
					layout1.add_widget(button3)
					layout1.add_widget(button4)
					layout1.add_widget(button5)
					layout1.add_widget(button6)
					layout1.add_widget(button7)
					layout1.add_widget(button8)
					layout1.add_widget(button9)

				layout2 = BoxLayout(orientation='vertical',size_hint=(.16,1) )
				#layout2 = BoxLayout(orientation='horizontal')
				with layout2.canvas.before:

					button21.bind(on_press=press_callback)
					button22.bind(on_press=press_callback)
					button23.bind(on_press=press_callback)
					button24.bind(on_press=press_callback)

					layout2.add_widget(button21)
					layout2.add_widget(button22)
					layout2.add_widget(button23)
					layout2.add_widget(button24)

				layout3 = GridLayout(cols=3,rows=4,size_hint=(.42,1))
				#layout2 = BoxLayout(orientation='horizontal')
				with layout3.canvas.before:

					button11.bind(on_press=press_callback)
					button12.bind(on_press=press_callback)
					button13.bind(on_press=press_callback)
					button14.bind(on_press=press_callback)
					button15.bind(on_press=press_callback)
					button16.bind(on_press=press_callback)
					button17.bind(on_press=press_callback)
					button18.bind(on_press=press_callback)
					button19.bind(on_press=press_callback)
					button20.bind(on_press=press_callback)

					layout3.add_widget(button11)
					layout3.add_widget(button12)
					layout3.add_widget(button13)
					layout3.add_widget(button14)
					layout3.add_widget(button15)
					layout3.add_widget(button16)
					layout3.add_widget(button17)
					layout3.add_widget(button18)
					layout3.add_widget(button19)
					layout3.add_widget(button20)

			inArduino = InputArduino()
			Clock.schedule_interval(inArduino.update, 1.0/10.0)

			superlayout.add_widget(layout1)
			superlayout.add_widget(layout2)
			superlayout.add_widget(layout3)

		megalayout.add_widget(titlelayout)
		megalayout.add_widget(superlayout)

		return megalayout
if __name__ == '__main__':

	MyApp().run()
