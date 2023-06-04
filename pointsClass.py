import turtle as t
from enemiesClass import Enemy

window = t.Screen()
window.addshape('star.gif')

scorebar = t.Turtle()
scorebar.hideturtle()
scorebar.penup()
scorebar.speed(0)
scorebar.goto(0, 320)
scorebar.color("white")
scorebar.write("Score: 0", align="center", font=("Courier", 24, "normal"))

def updateScorebar(score = None):
    scorebar.clear()
    if score != None:
        scorebar.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))
    else:
        scorebar.write(f"GAME OVER", align="center", font=("Courier", 24, "normal"))




class Point:
    playerPoints = 0
    pointsTab = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.point = t.Turtle()
        
        self.point.shape('star.gif')
        
        self.point.penup()
        self.point.speed(0)
        self.point.goto(x, y)
        self.point.setheading(90)
        self.point.shapesize(0.8, 0.8)

        self.point.width = 20
        self.point.height = 20

        self.eaten = False
        self.timeout = 0

        Point.pointsTab.append(self)

    def decreaseTimeout(self):
        if self.timeout > 0:
            self.timeout -= 0.01
        else:
            self.timeout = 0
            self.drawPoint()
    
    def getTimeout(self):
        return self.timeout

    def getEaten(self):
        return self.eaten

    
    def drawPoint(self):
        self.point.showturtle()
        self.point.goto(self.x, self.y)
        self.eaten = False
    
    def packmanColission(self):
        self.point.hideturtle()
        self.point.goto(-1000, -1000)
        Point.playerPoints += 10
        self.eaten = True
        self.timeout = 10

        if Point.playerPoints %30 == 0:
            Enemy.summonEnemy()
        
        updateScorebar(Point.playerPoints)


    @staticmethod
    def getPlayerPoints():
        return Point.playerPoints
    
    @staticmethod
    def showPoints():
        for point in Point.pointsTab:
            point.drawPoint()

    
        




