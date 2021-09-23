"""
class for periodic drawing
"""
from source.Timer import Timer
from source.Screen import Screen
import keyboard
import os

class Loopback:

    def __init__(self):
        #if screen should get cleared
        self.noclear = False
        #screens
        self.screens = [
        Screen(self.draw_first, lambda: keyboard.is_pressed("a"), False),
        Screen(lambda: print("Hallo"), lambda: 0, True)
        ]
        #current_screen
        self.current_screen = self.screens[0]


    def draw(self):
        if not self.noclear:
            self.current_screen.draw_method()



    def write_table(self, sentences, offset = 0):
        """
        writes sentences into a table
        """
        #most length for indentation
        most_length = 0
        #getting highest length
        for el in sentences:
            #if its the highest length
            if len(el) >= most_length:
                #setting
                most_length = len(el)
        #increasing for start
        most_length += 1
        #initializing table
        print(" "*offset+'-'*most_length)
        #printing table
        for el in sentences:
            #formatting
            print(" "*offset+"|", end="")
            print(el, end="")
            print(" "*(most_length-len(el)-1), end="")
            print("|")
            print(" "*offset+"-"*most_length)

    def draw_first(self):
        """
        Method for drawing first screen
        """
        self.clear_screen()
        self.write_table(["Altruism Simulator v1.0", "press q to exit"])

    def go_on(self):
        """
        goes on with screen
        """
        try:
            #switching current screen
            self.current_screen = self.screens[self.screens.index(self.current_screen)+1]
            #setting noclear
            self.noclear = self.current_screen.noclear
            #clearing and drawing
            self.clear_screen()
            self.current_screen.draw_method()
        except Exception:
            pass


    def clear_screen(self):
        """
        clears screen
        """
        os.system("cls")
