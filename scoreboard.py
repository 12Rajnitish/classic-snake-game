from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Comic Sans MS", 16, "normal")

# ScoreBoard class to manage score display
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0  # Initial score
        self.penup()
        self.ht()  # Hide the turtle (cursor)
        self.color('white')
        self.goto(x=0, y=290)  # Position the score at the top
        self.update_score()  # Display the score

    def update_score(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def gameover(self):
        self.goto(0, 0)  # Move to the center
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)  # Display game over message

    def increase_score(self):
        self.score += 1  # Increment score
        self.clear()  # Clear previous score
        self.update_score()  # Update the score display
