import turtle as t


class Pacman:
    def __init__(self):
        self.pacman = t.Turtle()
        self.pacman.shape("circle")
        self.pacman.color("yellow")
        self.pacman.penup()
        self.pacman.speed(0)
        self.pacman.goto(0, 100)
        self.pacman.direction = "stop"
        self.pacman.shapesize(2, 2)
        self.moveSpeed = 6

    def goDown(self):
        self.pacman.direction = "down"

    def goUp(self):
        self.pacman.direction = "up"

    def goLeft(self):
        self.pacman.direction = "left"

    def goRight(self):
        self.pacman.direction = "right"

    def move(self):
        if self.pacman.direction == "up":
            y = self.pacman.ycor()
            self.pacman.sety(y + self.moveSpeed)
        elif self.pacman.direction == "down":
            y = self.pacman.ycor()
            self.pacman.sety(y - self.moveSpeed)
        elif self.pacman.direction == "left":
            x = self.pacman.xcor()
            self.pacman.setx(x - self.moveSpeed)
        elif self.pacman.direction == "right":
            x = self.pacman.xcor()
            self.pacman.setx(x + self.moveSpeed)

    def distance(self, object):
        return self.pacman.distance(object)

    def getDirection(self):
        return self.pacman.direction

    def setDirection(self, direction):
        self.pacman.direction = direction

    def wallColission(self):
        # print(self.getDirection())
        if self.getDirection() == "up":
            self.pacman.sety(self.pacman.ycor() - self.moveSpeed*1.3)
        elif self.getDirection() == "down":
            self.pacman.sety(self.pacman.ycor() + self.moveSpeed*1.3)
        elif self.getDirection() == "left":
            self.pacman.setx(self.pacman.xcor() + self.moveSpeed*1.3)
        elif self.getDirection() == "right":
            self.pacman.setx(self.pacman.xcor() - self.moveSpeed*1.3)
        
        self.setDirection("stop")

