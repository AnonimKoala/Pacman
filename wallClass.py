import turtle as t
from config import windowWidth, windowHigh
window = t.Screen()
window.addshape('block.gif')

class Walls:
    wallsTab = []
    wallSize = (2,2)
    
    def __init__(self, pos):
        self.wall = t.Turtle()
        self.wall.shape("block.gif")

        

        self.wall.color("#001a8f")
        self.wall.penup()
        self.wall.shapesize(stretch_len=Walls.wallSize[0], stretch_wid=Walls.wallSize[1])
        self.wall.goto(pos[0], pos[1])
        self.wall.width = 40
        self.wall.height = 40

    

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
        Walls.wallsTab.append(Walls((int(round(x/10)*10), int(round(y/10)*10))))
    
    @staticmethod
    def deleteWall(x, y):
        for wall in Walls.wallsTab:
            if wall.wall.pos()[0] < x+30 and wall.wall.pos()[0] > x-30 and wall.wall.pos()[1] < y+30 and wall.wall.pos()[1] > y-30:
                Walls.wallsTab.remove(wall)
                wall.wall.hideturtle()
                del wall
                break
    
    @staticmethod
    def importWalls(walls):
        for wall in walls:
            Walls.addWall(wall[0], wall[1])

    @staticmethod
    def printAllWalls():
        allWalls = []
        for wall in Walls.wallsTab:
            allWalls.append(wall.wall.pos())
        print("\n\nWalls: \n")
        print(allWalls)