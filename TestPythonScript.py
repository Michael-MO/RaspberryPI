from sense_hat import SenseHat
import time

sense = SenseHat()

sense.clear((0,0,0))

r = 175
g = 31
b = 159

for y in range(0,8):
        for x in range(0,8):
                temp = sense.get_temperature()
                print(temp)
                if temp < 27:
                        r=0
                        g=0
                        b=255
                elif temp>=27 and temp <= 28:
                        r=255
                        g=255
                        b=0
                elif temp >28:
                        r=255
                        g=0
                        b=0
                sense.set_pixel(x,y,(r,g,b))
                time.sleep(1)

time.sleep(5)
sense.clear()

#sense.set_pixel(2,2,(r,g,b))
#sense.set_pixel(5,2,(r,g,b))
#sense.set_pixel(1,4,(r,g,b))
#sense.set_pixel(6,4,(r,g,b))
#sense.set_pixel(2,5,(r,g,b))
#sense.set_pixel(3,5,(r,g,b))
#sense.set_pixel(4,5,(r,g,b))
#sense.set_pixel(5,5,(r,g,b))
