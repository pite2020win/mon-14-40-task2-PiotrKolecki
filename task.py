
import sys
import random
import time

#pip install colorama
import colorama
colorama.init()

class bcolors:
        OKBLUE = '\033[94m'
        OKRED = '\033[91m'
        ENDC = '\033[0m'

class Plane:
  
  def __init__(self, roll_tolerance_point = 1, roll_adjust_value = 0.1):
    self.roll = 0 # +- 180deg
    self.roll_tolerance_point = roll_tolerance_point #deg
    self.roll_adjust_value = roll_adjust_value

  def adjust_roll(self):
    if(plane.roll > 0):
      plane.roll -= self.roll_adjust_value
    else:
      plane.roll += self.roll_adjust_value

  
if __name__ == "__main__":
  plane = Plane()
  rate_of_correction = 0.1
  try :
    while True:
      plane.roll += random.gauss(0, 2*rate_of_correction)
      if(abs(plane.roll) > 1):
        print("{} {} {}".format(bcolors.OKRED, plane.roll, bcolors.ENDC))
      else:
        print("{} {} {}".format(bcolors.OKBLUE, plane.roll, bcolors.ENDC))
      if(abs(plane.roll) > plane.roll_tolerance_point):
        plane.adjust_roll()
      time.sleep(0.1)
  except KeyboardInterrupt:
    pass
