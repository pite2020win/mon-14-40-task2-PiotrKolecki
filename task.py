from abc import ABC, abstractclassmethod
import sys
import random
import time
import math
import logging
import colorama

logging.basicConfig(
    format='%(levelname)s[%(asctime)s]: %(message)s',
    level=logging.INFO
)

colorama.init()


class bcolors:
    OKBLUE = '\033[94m'
    OKRED = '\033[91m'
    OKGREEN = '\033[92m'
    ENDC = '\033[0m'


class Plane:
    def __init__(
            self,
            roll_tolerance_point=2.5,
            roll_warning_point=5
            ):
        self.roll = 0  # +- 90 deg
        self.previous_roll = 0
        self.roll_tolerance_point = roll_tolerance_point
        self.roll_warning_point = roll_warning_point

    def __str__(self):
        roll_display_length = 51
        roll_display_percent = int(self.roll * roll_display_length / 180)
        out = "[{}0{}] : {:+}{}".format(
            (math.floor(roll_display_length/2)+roll_display_percent)*'-',
            (math.floor(roll_display_length/2)-roll_display_percent)*'-',
            plane.roll,
            bcolors.ENDC
        )
        if(abs(self.roll) > self.roll_warning_point):
            return "{}{}".format(bcolors.OKRED, out)
        else:
            return "{}{}".format(bcolors.OKGREEN, out)

    def correction(self):
        if(abs(self.roll) > self.roll_tolerance_point):
            self.roll += Correction(self.roll).adjust_roll(self.previous_roll)
        self.previous_roll = self.roll


def same_line_print(plane):
    sys.stdout.write(f"\r{plane}     ")


def random_generator(rate_of_correction):
    while True:
        n = random.gauss(0, 2*rate_of_correction)
        yield n


class Event(ABC):
    def __init__(self, roll):
        self.roll = roll

    @abstractclassmethod
    def adjust_roll(self):
        pass


class Correction(Event):
    def adjust_roll(self, previus_roll):
        if previus_roll > 0:
            return -abs(previus_roll - self.roll) * random.random()
        return abs(previus_roll - self.roll) * random.random()


class Turbulence(Event):
    def __init__(self, roll, wind):
        super().__init__(roll)
        self.roll += self.adjust_roll(wind)

    def adjust_roll(self, wind):
        return wind ** 2


class Environment:
    def __init__(self, rate_of_correction=1, wind=0.5):
        self.rate_of_correction = rate_of_correction
        self.gen = random_generator(self.rate_of_correction)
        self.wind = wind

    def turbuence(self, plane):
        plane.roll += Turbulence(next(self.gen), self.wind).roll


if __name__ == "__main__":
    plane = Plane()
    environment = Environment()

    try:
        while True:
            environment.turbuence(plane)
            plane.correction()
            logging.info(plane)
            # same_line_print(plane)
            time.sleep(0.1)
    except KeyboardInterrupt:
        logging.info(f"{bcolors.OKRED}# Keyboard Interrupt #{bcolors.ENDC}")
