"""
Class Screen: provides draw methods and declares a draw_function
"""

class Screen:

    def __init__(self, method=None, go_on_method=None, noclear=False):

        """
        gets input
        """
        self.draw_method = method
        #if screen is finished
        self.noclear = noclear
        self.go_on_method = go_on_method
