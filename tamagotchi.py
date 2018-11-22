from sense_hat import SenseHat
import time
import random

s = SenseHat()

red = 0
blue = 0
green = 255;
foreground = (red, green, blue)
background = (0, 0, 0)

timesFed = 0
timesExercised = 0
timesPooped = 0
timesPlayed = 0
timesWaited = 0

def clamp(n, smallest, largest): return max(smallest, min(n, largest))

def alive():
    global red
    global green
    global blue
    green = clamp((green - 1), 0, 255)
    red = clamp((red + 1), 0, 255)

def random_action():
    global red
    global green
    global blue
    global timesFed
    global timesExercised
    global timesWaited
    
    chance = random.randint(0, 99)
    if chance <= 1:
      if timesWaited < 3:
        timesWaited = timesWaited + 1
        timesFed = timesFed - 1
        red = 0
        green = 0
        blue = 255
      else:
        red = 255
        green = 0
        blue = 0
    
def feed():
    global red
    global green
    global blue
    global timesFed
    global timesExercised
    global timesWaited
    
    if timesFed < 6 and timesWaited > 0:
      green = 255
      red = 0
      blue = 0
      timesWaited = 0
      
    elif timesFed < 6 and timesWaited < 1:
      green = clamp((green + 50), 0, 255)
      red = clamp((red - 50), 0, 255)
      blue = 0
      timesFed = timesFed + 1
      if timesExercised > 0:
        timesExercised = timesExercised - 1
        
    else:
      green = 0
      blue = 0
      red = 255
    
def exercise():
    global red
    global green
    global blue
    global timesFed
    global timesExercised
    
    if timesExercised < 22:
      green = clamp((green + 50), 0, 255)
      red = clamp((red - 50), 0, 255)
      blue = 0
      timesExercised = timesExercised + 1
      if timesFed > 0:
        timesFed = timesFed - 1
        
    else:
      green = 0
      red = 255
      blue = 0
    
def doActions():
    for event in s.stick.get_events():
      if event.direction == 'up':
          exercise()
      elif event.direction == 'down':
          feed()

def tamagotchi_face():
    B = background
    F = foreground
    image = [ 
    B, B, B, B, B, B, B, B,
    B, F, F, B, B, F, F, B,
    B, B, F, B, B, F, B, B,
    B, B, B, B, B, B, B, B,
    B, F, B, F, F, B, F, B,
    B, F, B, B, B, B, F, B,
    B, B, F, F, F, F, B, B,
    B, B, B, B, B, B, B, B,
    ]
    return image

s.set_pixels(tamagotchi_face())

while True:
    alive()
    random_action()
    doActions()
    foreground= (red,green,blue)
    s.set_pixels(tamagotchi_face())
    time.sleep(0.5)
