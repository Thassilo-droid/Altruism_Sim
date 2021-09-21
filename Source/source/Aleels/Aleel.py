"""
V 1.0

Class Aleel
"""
from abc import ABC, abstractmethod

class Aleel(ABC):

    """

    Aleel is the superclass for all living entities in the Environment
    """

    def __init__(self, identity, strength, fertability, \
                cowardness, hp, fed_scale,):
