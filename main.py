import turtle as tt
import random

# Screen setup
screen = tt.Screen()
tt.setup(800, 500)
tt.bgcolor("darkgrey")

SCORE = 0

# Player setup
class Player:
    def __init__(self):
        self.platform = tt.Turtle()
        self.platform.hideturtle()
        self.platform.speed(0)
        self.platform.color("white")
        self.platform.shape("square")
        self.platform.turtlesize(stretch_len=4)
        self.platform.penup()
        self.platform.sety(-180)
        self.platform.showturtle()

    def move_right(self):
        if self.platform.xcor() <= 350:
            self.platform.fd(10)
        else:
            pass

    def move_left(self):
        if self.platform.xcor() >= -350:
            self.platform.bk(10)
        else:
            pass


class Bars:
    def __init__(self, counter, y_offset):
        self.bar = tt.Turtle()
        self.bar.speed(0)
        self.bar.penup()
        self.bar.shape("square")
        self.bar.color("red")
        self.bar.turtlesize(stretch_len=3)
        self.bar.setpos(-300+(counter*100), 250+y_offset)


class Ball:
    def __init__(self):
        self.ball = tt.Turtle()
        self.ball.hideturtle()
        self.ball.color("white")
        self.ball.speed(0)
        self.ball.shape("circle")
        self.ball.left(90)
        self.ball.penup()
        self.ball.sety(-160)
        self.ball.shapesize(1)
        self.ball.showturtle()

        self.ball_speed = 8

        self.set_rotation()
        self.movement()

    def movement(self):
        if -380 <= self.ball.xcor() <= 380 and -240 <= self.ball.ycor() <= 240:
            if -180 < self.ball.ycor() < -160 and player.platform.xcor()-40 < self.ball.xcor() < player.platform.xcor()+40:
                self.ball.right(180)
                self.ball.fd(self.ball_speed)
                self.set_rotation()
            else:
                for x in bars:
                    if self.ball.distance(x.bar) < 30:
                        global SCORE
                        SCORE += 1
                        score_text.clear()
                        score_text.write(SCORE, move=False, align="center", font=("Arial", 16, "normal"))
                        x.bar.hideturtle()
                        bars.remove(x)
                        self.ball.right(180)
                        self.ball.fd(self.ball_speed)
                        self.set_rotation()
                self.ball.fd(self.ball_speed)

        elif self.ball.ycor() < -240 or bars == []:
            if not bars:
                print("You Win")
            else:
                print("Game Over")
            screen.bye()
        else:
            self.ball.right(180)
            self.ball.fd(self.ball_speed)
            self.set_rotation()

        screen.ontimer(self.movement, 10)

    def set_rotation(self):
        random_rot = random.randrange(-45, 45)
        self.ball.right(random_rot)


player = Player()

# Setup bars
bar_numb = 0
offset = 0
bars = []

for bar in range(0, 14):
    if bar % 7 == 0:
        offset -= 50
        bar_numb = 0
    bars.append(Bars(counter=bar_numb, y_offset=offset))
    bar_numb += 1

ball_sprite = Ball()

tt.onkeypress(player.move_left, "Left")
tt.onkeypress(player.move_right, "Right")

score_text = tt.Turtle()
score_text.hideturtle()
tt.listen()
tt.mainloop()
