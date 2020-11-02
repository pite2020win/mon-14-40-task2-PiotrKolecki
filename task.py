#
#Flight simulator. 
#Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth). 
#The program should print out current orientation, and applied tilt correction.
# (Tilt is "Roll" in this diagram https://www.novatel.com/assets/Web-Phase-2-2012/Solution-Pages/AttitudePlane.png)
#The program should run in infinite loop, until user breaks the loop. 
#Assume that plane orientation in every new simulation step is changing with random angle with gaussian distribution (the planes is experiencing "turbuence"). 
# Hint: "random.gauss(0, 2*rate_of_correction)"
#With every simulation step the orentation should be corrected, correction should be applied and printed out.
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#Delete these comments before commit!
#
#Good luck.

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
