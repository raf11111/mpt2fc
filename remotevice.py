import socket

def sendCommand(command):
    s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex(("localhost", 6510))
    s.send(command)
    print "monitor response: " + s.recv(100)
    s.close()
    if result > 0:
        print "problem with socket!"
    else:
        print "socket ok!"