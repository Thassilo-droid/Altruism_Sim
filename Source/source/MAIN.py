"""
defines class for management
"""
#import dependencies
from source.Loopback import Loopback
from source.Timer import Timer


class MAIN:

    """
    superclass for management that performs all actions in indiviudal steps

    modes: [0, 1, 2]: #0: full simulation; 1 iterable simulation; 2stopabble simulation
    """

    def __init__(self):
        #getting environments
        self.envs = []
        #loopback for drawing

        #setting timer
        self.timer = Timer(0.4)
        self.loopback = Loopback()

        #mode for init
        self.mode = 0


    def draw(self):
        #calls loopback.draw
        if self.timer.time_pulse_set():
            self.loopback.draw()

    def callback(self):
        #checking go on on screen
        if self.loopback.current_screen.go_on_method():
            self.loopback.go_on()
        #getting and setting clock pulse
        self.timer.clock_pulse()
        if self.timer.time_pulse_set():
            self.draw()
