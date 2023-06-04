import turtle as t

window = t.Screen()
window.addshape('pacman/right.gif')
window.addshape('pacman/left.gif')
window.addshape('pacman/up.gif')
window.addshape('pacman/down.gif')

class Pacman:
    def __init__(self):
        self.pacman = t.Turtle()
        self.pacman.shape("pacman/right.gif")
        self.pacman.color("yellow")
        self.pacman.penup()
        self.pacman.speed(0)
        self.pacman.goto(-25, 140)
        self.pacman.direction = "stop"
        self.pacman.shapesize(2, 2)
        self.moveSpeed = 6

        self.pacman.width = 35
        self.pacman.height = 35

    def goDown(self):
        self.pacman.direction = "down"
        self.pacman.shape("pacman/down.gif")

    def goUp(self):
        self.pacman.direction = "up"
        self.pacman.shape("pacman/up.gif")

    def goLeft(self):
        self.pacman.direction = "left"
        self.pacman.shape("pacman/left.gif")

    def goRight(self):
        self.pacman.direction = "right"
        self.pacman.shape("pacman/right.gif")

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

