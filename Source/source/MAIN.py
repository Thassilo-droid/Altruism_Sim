"""
defines class for management
"""

class MAIN:

    """
    superclass for management that performs all actions in indiviudal steps

    modes: [0, 1, 2]: #0: full simulation; 1 iterable simulation; 2stopabble simulation
    """

    def __init__(self):
        #getting environments
        self.envs = []
        #loopback for drawing
        self.loopback = None
        #mode for init
        self.mode = 0

    def draw(self):
        #calls loopback.draw
        pass

    def callback(self):
        #not yet deined
        pass
