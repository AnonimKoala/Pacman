import turtle as t


class Point:
    playerPoints = 0
    pointsTab = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.point = t.Turtle()
        self.point.shape("triangle")
        self.point.color("gold")
        self.point.penup()
        self.point.speed(0)
        self.point.goto(x, y)
        self.point.shapesize(0.5, 0.5)
        self.point.width = 10
        self.point.height = 10
        self.eaten = False
        self.timeout = 0

        Point.pointsTab.append(self)

    def decreaseTimeout(self):
        if self.timeout > 0:
            self.timeout -= 1
        else:
            self.timeout = 0
            self.drawPoint()

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

        print(Point.playerPoints)

    @staticmethod
    def getPlayerPoints():
        return Point.playerPoints

    
        


        