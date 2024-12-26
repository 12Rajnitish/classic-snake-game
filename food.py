from turtle import Turtle
import random as rd

# Food class to manage food generation
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.relocate()  # Position food at a random location
        self.shape('circle')  # Shape of the food
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)  # Resize the food
        self.color('blue')  # Color of the food
        self.speed('fastest')  # Set the food speed to the fastest

    def relocate(self):
        # Generate random x and y coordinates for food position
        random_x = rd.randint(-280, 280)
        random_y = rd.randint(-280, 280)
        self.goto(random_x, random_y)  # Move the food to the new location
