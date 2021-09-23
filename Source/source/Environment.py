"""
Altruism Simulator version 1.0
"""
class Environment:

    """
    class for regulating access for all Aleels and everything
    """

    typen = ["NormalAleel", "GreenBeardAleel"]

    def __init__(self, normal_aleels=[], green_beard_aleels=[],\
                food_resources=[], homes=[]):
        #for all Aleels
        self.all_aleels = []
        self.all_aleels_count = 0
        #assigning the count
        self.normal_aleels_count = len(normal_aleels)
        self.normal_aleels = normal_aleels

        self.green_beard_aleels_count = len(green_beard_aleels)
        self.green_beard_aleels = green_beard_aleels


        #resources
        self.food_resources = food_resources
        #own homes
        self.homes = homes

    def kill_starving_aleels(self):
        pass

    def kill_all_aleels(self):
        pass

    def invoke_food_search_process(self):
        pass

    def invoke_food_action_process(self):
        pass

    def invoke_home_finding_process(self):
        pass

    def invoke_reproduction_resource(self):
        pass
