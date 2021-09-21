"""
class for periodic drawing
"""
from source.Timer import Timer
import keyboard
import os

class Loopback:

    def __init__(self, timeout=0.6):
        #timeout defines time for Timer
        self.timeout = timeout
        #making timer instance
        self.timer = Timer(timeout)

    def draw(self):
        self.timer.clock_pulse()
        #if timer gives pulse
        if self.timer.time_pulse_set():
            #all drawing
            self.clear_screen()
            self.environment_draw(None)


    def environment_draw(self, env):
        #not yet defined
        print("Altruism Simulator v1.0")

    def clear_screen(self):
        """
        clears screen
        """
        os.system("cls")
