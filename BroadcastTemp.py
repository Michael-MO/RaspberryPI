BROADCAST_TO_PORT = 12121
import time
import json
from socket import *
from datetime import datetime
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

r,g,b = 255, 0, 0

s = socket(AF_INET, SOCK_DGRAM)
#s.bind(('', 14593))     # (ip, port)
# no explicit bind: will bind to default IP + random port
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
while True:
	for x in range(0,8):
		temp = sense.get_temperature()

		jsonObj = {
		"time" : str(datetime.now()),
		"temperature" : temp
		}

		data = json.dumps(jsonObj)
		s.sendto(bytes(data, "UTF-8"), ('<broadcast>', BROADCAST_TO_PORT))
		print(data)

		if temp < 27.3:
			i = 7
		elif temp < 27.4:
			i = 6
		elif temp < 27.5:
			i = 5
		elif temp < 27.6:
			i = 4
		elif temp < 27.7:
			i = 3
		elif temp < 27.8:
			i = 2
		elif temp < 27.9:
			i = 1
		else:
			i = 0

		nextLine = x + 1

		if x == 7:
			nextLine = 0

		sense.set_pixel(x, 7, (r,g,b))
		sense.set_pixel(nextLine, 7, (0,0,0))

		for y in range(i,7):
			sense.set_pixel(x, y, (r,g,b))

		for z in range(0,8):
			sense.set_pixel(nextLine, z, (0,0,0))

		time.sleep(1)
		