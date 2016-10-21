import Tkinter
import threading


#actual object containing logic and data
class MockGPIO(object):
	
	def __init__(self):
		self.state = dict()
		self.type = dict()
		self.input_pins = []
		self.output_pins = []
		self.board = 0
		self.IN = 0
		self.OUT = 1
		self.LOW = 0
		self.HIGH = 1
		self.PUD_DOWN = 0
		self.PUD_UP = 1

	def input(self,pin):
		return self.state[pin]

	def toggle(self,pin):
		if self.state[pin] == self.HIGH:
			self.state[pin] = self.LOW
		else:
			self.state[pin] = self.HIGH
		return self.state[pin]

	#indiates what pin is what type
	def setup(self,pin,ptype):
		if ptype == self.IN:
			self.input_pins.append(pin)
		else:
			self.output_pins.append(pin)
		self.type[pin] = self.LOW

	
	def output(self,pin,p2,pull_up_down=1):
		pass

	def setmode(self,board):
		pass

	def cleanup(self):
		pass

BOARD = 0
IN = 0
OUT = 1
LOW = 0
HIGH = 1
PUD_DOWN = 0
PUD_UP = 1
INTERACTIVE = 1
AUTOMATED = 0
GPIO = MockGPIO()

def setmode(board,test_mode,cfg):
	#spawn gui process here
	if test_mode==INTERACTIVE:
		t = threading.Thread(target=display, args = (GPIO,cfg))
		# t.daemon = True
		t.start()
	else:
		#automated test code goes here
		pass

#naming clash with python's input
def input(pin):
	return GPIO.input(pin)

def toggle(pin):
	GPIO.toggle(pin)

def status(pin):
	ans = GPIO.input(pin)
	response=""
	if ans == HIGH:
		response="closed"
	else:
		response="open"
	return response

def setup(pin,ptype,pull_up_down=PUD_UP):
	GPIO.setup(pin,ptype)

def output(pin,p2,pull_up_down=PUD_UP):
	GPIO.output(pin,p2,pull_up_down)

def cleanup():
	GPIO.cleanup()

def display(GPIO,cfg):
	# root gui window
	top = Tkinter.Tk()
	for door in cfg.GARAGE_DOORS:
		pin = door['pin']
		b = Tkinter.Button(top, 
			text = str(door['name']+status(pin)), 
			command = lambda: updateButton(pin,b,door))
		b.pack()

	top.mainloop()

def updateButton(pin,button,door):
	toggle(pin)
	t = door['name']+" is "+status(pin)
	button.configure(text=t)   
