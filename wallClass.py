import turtle as t
from config import windowWidth, windowHigh

class Walls:
    wallsTab = []
    wallSize = (2,2)
    
    def __init__(self, pos):
        self.wall = t.Turtle()
        self.wall.shape("square")
        self.wall.color("#001a8f")
        self.wall.penup()
        self.wall.shapesize(stretch_len=Walls.wallSize[0], stretch_wid=Walls.wallSize[1])
        self.wall.goto(pos[0], pos[1])

    

    @staticmethod
    def drawWalls():
        for x in range(int((windowWidth/2 * -1) + Walls.wallSize[0]*10), int((windowWidth/2)), Walls.wallSize[0]*20):
            Walls.wallsTab.append(Walls((x, 380)))
            Walls.wallsTab.append(Walls((x, -380)))

        for y in range(int((windowHigh/2 * -1) + Walls.wallSize[1]*10), int((windowHigh/2)), Walls.wallSize[1]*20):
            Walls.wallsTab.append(Walls((380, y)))
            Walls.wallsTab.append(Walls((-380, y)))

    @staticmethod
    def addWall(x, y):
        Walls.wallsTab.append(Walls((x, y)))
    
    @staticmethod
    def deleteWall(x, y):
        for wall in Walls.wallsTab:
            if wall.wall.pos()[0] < x+30 and wall.wall.pos()[0] > x-30 and wall.wall.pos()[1] < y+30 and wall.wall.pos()[1] > y-30:
                Walls.wallsTab.remove(wall)
                wall.wall.hideturtle()
                del wall
                break