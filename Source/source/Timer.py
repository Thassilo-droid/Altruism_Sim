"""
Timer for drawing instances
"""

import time

class Timer:

    def __init__(self, timeout):
        #setting frequency
        self.frequency = timeout
        #bool for pulse is set
        self.time_puls = False
        #setting times
        self.last_time = time.perf_counter()
        self.current_time = time.perf_counter()

    def clock_pulse(self):
        """
        Method for calculating puls
        """
        #getting new time
        self.current_time = time.perf_counter()
        #checking if timelimit has passes
        if self.current_time-self.last_time >= self.frequency:
            #true:
            self.time_puls = True
            #resetting time
            self.last_time = self.current_time
        else:
            self.time_puls = False

    def time_pulse_set(self):
        #just for giving time puls
        return self.time_puls
