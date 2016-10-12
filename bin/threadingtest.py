from servertest import MyTCPServer,MyTCPServerHandler
import threading
import time

# for u in theurls:
    # t = threading.Thread(target=get_url, args = (q,u))
#    t.daemon = True
    # t.start()

server = MyTCPServer(('127.0.0.1', 13373), MyTCPServerHandler)

t = threading.Thread(target = server.serve_forever)
t.start()
time.sleep(1000000)