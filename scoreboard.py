from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Comic Sans MS", 16, "normal")

# ScoreBoard class to manage score display
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0  # Initial score
        with open("data.txt") as data:
                self.high_score = int(data.read())
        self.penup()
        self.ht()  # Hide the turtle (cursor)
        self.color('white')
        self.goto(x=0, y=290)  # Position the score at the top
        self.update_score()  # Display the score

    def update_score(self):
        self.clear()  # Clear previous score
        self.write(arg=f"Score: {self.score} High Score :{self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode='w') as data:
                data.write(f"{self.high_score}")
        self.score= 0
        self.update_score()

    def increase_score(self):
        self.score += 1  # Increment score
        self.update_score()  # Update the score display
