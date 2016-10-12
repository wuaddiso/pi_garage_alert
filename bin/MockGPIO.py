import SocketServer
import json

class GPIOServer(SocketServer.ThreadingTCPServer):
    allow_reuse_address = True
    

class GPIOServerHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        try:

            # self.rfile is a file-like object created by the handler;
	        # we can now use e.g. readline() instead of raw recv() calls
	        self.data = self.rfile.readline().strip()
	        # print "{} wrote:".format(self.client_address[0])
	        # print self.data
	        # Likewise, self.wfile is a file-like object used to write back
	        # to the client
	        self.wfile.write(self.data.upper())
        except Exception, e:
            print "Exception wile receiving message: ", e


class MockGPIO(object):
	
	def __init__(self):
		self.state = dict()
		self.board = 0
		self.IN = 0
		self.OUT = 1
		self.LOW = 0
		self.HIGH = 1
		self.PUD_DOWN = 0
		self.PUD_UP = 1

	def input(self,pin):
		return self.state[pin]

	#set PIN
	def output(self,pin,p2,pull_up_down=1):
		pass

	def setmode(self,board):
		pass

	def cleanup():
		pass


# if __name__=='__main__':
#  # server = MyTCPServer(('127.0.0.1', 13373), MyTCPServerHandler)
#  # server.serve_forever()
#  # print 'blah'
# 	