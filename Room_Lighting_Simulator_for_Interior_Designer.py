import math as mt

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import reportlab as rl
import streamlit as st

# required light, LUX standard, reflectance, number of lamps required, lumens of 1 light,
# window area, lamp kelvin, Daylight, desired lumens, outdoor light,


class Room:
    def __init__(self, length, width, height, reflection=0.7):
        self.set_data(length, width, height, reflection)
        self.print_data()

    def set_data(self, lenght, width, height, reflaction=0.7):
        self.lenght = lenght
        self.width = width
        self.height = height
        self.reflaction = reflaction
        self.area = lenght * width
        self.floor_area = self.area
        self.ceiling_area = self.area
        self.wall_area = 2 * (lenght + width) * height

    def print_data(self):
        pass


class Living_room(Room):
    pass


class Kitchen(Room):
    pass


class Bedroom(Room):
    pass


class Bathroom(Room):
    pass


class Office(Room):
    pass
