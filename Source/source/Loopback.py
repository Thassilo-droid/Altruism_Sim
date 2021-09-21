"""
class for periodic drawing
"""
from source.Timer import Timer
import keyboard
import os

class Loopback:

    def __init__(self):
        pass


    def draw(self):
        self.environment_draw(None)


    def environment_draw(self, env):
        #not yet defined
        self.write_table(["Altruism Simulator v1.0", "press q to exit"])


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



    def clear_screen(self):
        """
        clears screen
        """
        os.system("cls")
