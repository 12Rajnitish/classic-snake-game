from turtle import Turtle

# Initial snake setup
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]  # Positions for the starting snake
MOVE_DISTANCE = 20  # Distance moved per step
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

# Snake class to manage the snake's behavior
class Snake:

    def __init__(self):
        self.segments = []  # List to store snake body segments
        self.border()  # Draw the border
        self.create_snake()  # Create the snake body
        self.head = self.segments[0]  # The head is the first segment

    def create_snake(self):
        # Create initial snake segments from the starting positions
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        # Add a segment to the snake at the given position
        new_segment = Turtle(shape='square')  # Square shape for snake body
        new_segment.color('red')  # Color of the snake
        new_segment.penup()  # Don't draw lines
        new_segment.goto(position)  # Move to the specified position
        self.segments.append(new_segment)  # Add to the snake's body

    def extend(self):
        # Add a new segment to the snake's body
        self.add_segment(self.segments[-1].position())

    def move(self):
        # Move the snake by updating the positions of the segments
        for seg_num in range(len(self.segments) - 1, 0, -1):  # Start from the last segment
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)  # Move the head forward by the set distance

    def up(self):
        # Change the direction to UP if not already moving down
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        # Change the direction to DOWN if not already moving up
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        # Change the direction to LEFT if not already moving right
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        # Change the direction to RIGHT if not already moving left
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def border(self):
        # Draw the border of the game area
        tim = Turtle()
        tim.ht()  # Hide the turtle (cursor)
        tim.penup()
        tim.color('cyan')
        tim.goto(290, -290)  # Starting point of the border
        tim.down()
        tim.goto(290, 290)
        tim.goto(-290, 290)
        tim.goto(-290, -290)
        tim.goto(290, -290)
        tim.penup()
