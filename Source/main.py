"""
Altruism Simulator v1.0
"""
from source.MAIN import MAIN
import keyboard
import os

p = False

main = MAIN()

while not p:
    p = keyboard.is_pressed("q")
    main.callback()

os.system("cls")
