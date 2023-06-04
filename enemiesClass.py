import turtle as t
import random

window = t.Screen()
window.addshape('enemies/blue.gif')
window.addshape('enemies/red.gif')
window.addshape('enemies/pink.gif')
window.addshape('enemies/orange.gif')
window.addshape('enemies/green.gif')
window.addshape('enemies/purple.gif')
window.addshape('enemies/white.gif')
window.addshape('enemies/brown.gif')



class Enemy:
    enemiesTab = []

    def __init__ (self, color, directionNum):
        self.enemy = t.Turtle()


        if color == 'blue':
            self.enemy.shape("enemies/blue.gif")
        elif color == 'red':
            self.enemy.shape("enemies/red.gif")
        elif color == 'pink':
            self.enemy.shape("enemies/pink.gif")
        elif color == 'orange':
            self.enemy.shape("enemies/orange.gif")
        elif color == 'green':
            self.enemy.shape("enemies/green.gif")
        elif color == 'purple':
            self.enemy.shape("enemies/purple.gif")
        elif color == 'white':
            self.enemy.shape("enemies/white.gif")
        elif color == 'brown':
            self.enemy.shape("enemies/brown.gif")
        else: 
            self.enemy.shape("circle")



        
        self.enemy.color(color)
        self.enemy.penup()
        self.enemy.speed(0)
        self.enemy.goto(70,0)
        self.enemy.directions = ["up", "down", "left", "right"]
        self.enemy.direction = self.enemy.directions[directionNum]
        self.enemy.shapesize(1.6,1.6)
        self.moveSpeed = 4
        self.enemy.width = 30
        self.enemy.height = 30

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
            self.enemy.sety(y + self.moveSpeed)
        elif self.enemy.direction == "down":
            y = self.enemy.ycor()
            self.enemy.sety(y - self.moveSpeed)
        elif self.enemy.direction == "left":
            x = self.enemy.xcor()
            self.enemy.setx(x - self.moveSpeed)
        elif self.enemy.direction == "right":
            x = self.enemy.xcor()
            self.enemy.setx(x + self.moveSpeed)
        

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


    @staticmethod
    def summonEnemy():
        colors = ["red", "blue", "green", "pink", "orange", "purple", "brown", "white"]
        Enemy.enemiesTab.append(Enemy(random.choice(colors), random.randint(0,3)))
        
