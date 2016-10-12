import Tkinter
#interface with gui
BOARD = 0
IN = 0
OUT = 1
LOW = 0
HIGH = 1
PUD_DOWN = 0
PUD_UP = 1
def setmode(board):
	GPIO = MockGPIO()
	#spawn gui process here
	
def input(pin):
	return GPIO.input(pin)

def setup():
	pass

def output():
	pass


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
		self.top = Tkinter.Tk()

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
		b = Tkinter.Button(self.top,
						   text="toggle garage",
						   command = lambda:toggle(pin))
		b.pack()
	
	def output(self,pin,p2,pull_up_down=1):
		pass

	def setmode(self,board):
		#spawn a gui thread
		pass

	def cleanup():
		pass


# if __name__=='__main__':
#  # server = MyTCPServer(('127.0.0.1', 13373), MyTCPServerHandler)
#  # server.serve_forever()
#  # print 'blah'
# 	