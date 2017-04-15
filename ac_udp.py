import socket
import subprocess

#tempc = subprocess.check_output(['temper-poll', '-f'])
tempc = "19.0"

UDP_IP = "192.168.2.104"
UDP_PORT = 44000
MESSAGE = "{\"f|temperature\":\"" + tempc + "\"}"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
