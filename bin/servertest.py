import SocketServer
import json

class MyTCPServer(SocketServer.ThreadingTCPServer):
    allow_reuse_address = True
    print 'MyTCPServer'

class MyTCPServerHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        try:

            #data = json.loads(self.request.recv(1024).strip())
            # process the data, i.e. print it:
            #print data
            # send some 'ok' back
            print 'MyTCPServerHandler'
            self.request.sendall(json.dumps({'return':'ok'}))
        except Exception, e:
            print "Exception wile receiving message: ", e
if __name__=='__main__':
 server = MyTCPServer(('127.0.0.1', 13373), MyTCPServerHandler)
 server.serve_forever()
 print 'blah'