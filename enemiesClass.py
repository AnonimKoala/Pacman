import turtle as t
import random
class Enemy:
    def __init__ (self):
        self.enemy = t.Turtle()
        self.colors = ["red", "blue", "pink", "orange"]
        self.enemy.shape("circle")
        self.enemy.color(random.choice(self.colors))
        self.enemy.penup()
        self.enemy.speed(0)
        self.enemy.goto(30,0)
        self.enemy.directions = ["up", "down", "left", "right"]
        self.enemy.direction = random.choice(self.enemy.directions)
        self.enemy.shapesize(2, 2)
        self.moveSpeed = 10

    def goDown(self):
        self.enemy.direction = "down"
    def goUp(self):
        self.enemy.direction = "up"
    def goLeft(self):
        self.enemy.direction = "left"
    def goRight(self):
        self.enemy.direction = "right"

    def move(self):
        if self.enemy.direction == "up":
            y = self.enemy.ycor()
            self.enemy.sety(y + 4)
        elif self.enemy.direction == "down":
            y = self.enemy.ycor()
            self.enemy.sety(y - 4)
        elif self.enemy.direction == "left":
            x = self.enemy.xcor()
            self.enemy.setx(x - 4)
        elif self.enemy.direction == "right":
            x = self.enemy.xcor()
            self.enemy.setx(x + 4)
        

    def distance(self, object):
        return self.enemy.distance(object)
    
    def getDirection(self):
        return self.enemy.direction
    def setDirection(self, direction):
        self.enemy.direction = direction

    def setX(self, x):
        self.enemy.setx(x)
    def setY(self, y):
        self.enemy.sety(y)
    def getX(self):
        return self.enemy.xcor()
    def getY(self):
        return self.enemy.ycor()
    
    def wallColission(self):
        if self.getDirection() == "up":
            self.enemy.sety(self.enemy.ycor() - self.moveSpeed*1.3)
        elif self.getDirection() == "down":
            self.enemy.sety(self.enemy.ycor() + self.moveSpeed*1.3)
        elif self.getDirection() == "left":
            self.enemy.setx(self.enemy.xcor() + self.moveSpeed*1.3)
        elif self.getDirection() == "right":
            self.enemy.setx(self.enemy.xcor() - self.moveSpeed*1.3)
        
        self.enemy.direction = random.choice(self.enemy.directions)


    def upWall(self):
        self.enemy.sety(self.enemy.ycor() - 5)
    def downWall(self):
        self.enemy.sety(self.enemy.ycor() + 5)
    def leftWall(self):
        self.enemy.setx(self.enemy.xcor() + 5)
    def rightWall(self):
        self.enemy.setx(self.enemy.xcor() - 5)

