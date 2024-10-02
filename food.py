
from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self, pixel_size):
        super().__init__()
        self.pixel_size = pixel_size
        x = random.randint(-14,14)*self.pixel_size
        y = random.randint(-14,14)*self.pixel_size
        self.food_position = (x, y)
        self.color("red")
        self.shape("square")
        self.penup()
        self.goto(self.food_position)
        self.speed(0)  