from turtle import Screen
from scoreboard import ScoreBoard
from snake import Snake
import time
from food import Food
import scoreboard

# Set up the game screen
screen = Screen()
screen.setup(width=640, height=640)
screen.bgcolor('black')
screen.title("Classic Snake Game")
screen.tracer(0)  # Disable automatic updates for smoother animation

# Create a snake, food, and scoreboard
snake = Snake()
food = Food()
score = ScoreBoard()

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()  # Update screen after each movement
    time.sleep(0.1)  # Slow down the loop for controllable snake speed
    snake.move()  # Move the snake

    # Check for collision with the snake's body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:  # If snake's head touches body
            score.gameover()  # End the game
            game_is_on = False

    # Check for collision with food
    if snake.head.distance(food) < 15:  # If snake's head touches food
        score.increase_score()  # Increase score
        snake.extend()  # Grow the snake
        food.relocate()  # Move the food to a new location

    # Check for collision with the wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        score.gameover()  # End the game if snake hits the wall
        game_is_on = False

    # Control snake's movement with keyboard
    screen.listen()
    screen.onkey(fun=snake.up, key='Up')
    screen.onkey(fun=snake.down, key='Down')
    screen.onkey(fun=snake.left, key='Left')
    screen.onkey(fun=snake.right, key='Right')

# Close the screen when clicked
screen.exitonclick()
