
import turtle as t
import time
from pacmanClass import Pacman


window = t.Screen()
window.title("Pacman")

windowHigh = 800
windowWidth = 800

window.setup(windowWidth, windowHigh)
t.bgcolor("black")
window.tracer(0)

wallSize = (2, 2)



class Wall:
    def __init__(self, pos, size):
        self.wall = t.Turtle()
        self.wall.shape("square")
        self.wall.color("#001a8f")
        self.wall.penup()
        self.wall.shapesize(stretch_len=size[0], stretch_wid=size[1])
        self.wall.goto(pos[0], pos[1])



walls = []




def drawWalls():
    for x in range(int((windowWidth/2 * -1) + wallSize[0]*10), int((windowWidth/2)), wallSize[0]*20):
        walls.append(Wall((x, 380), wallSize))
        walls.append(Wall((x, -380), wallSize))

    for y in range(int((windowHigh/2 * -1) + wallSize[1]*10), int((windowHigh/2)), wallSize[1]*20):
        walls.append(Wall((380, y), wallSize))
        walls.append(Wall((-380, y), wallSize))


drawWalls()



pacman = Pacman()
t.onkeypress(pacman.goUp, "Up")
t.onkeypress(pacman.goDown, "Down")
t.onkeypress(pacman.goLeft, "Left")
t.onkeypress(pacman.goRight, "Right")







t.listen()
while True:
    window.update()
    pacman.move()

    for wall in walls:
        if pacman.distance(wall.wall) < 45:
            if pacman.getDirection() == "up":
                pacman.pacman.sety(pacman.pacman.ycor() - 5)
            elif pacman.getDirection() == "down":
                pacman.pacman.sety(pacman.pacman.ycor() + 5)
            elif pacman.getDirection() == "left":
                pacman.pacman.setx(pacman.pacman.xcor() + 5)
            elif pacman.getDirection() == "right":
                pacman.pacman.setx(pacman.pacman.xcor() - 5)
                 
            pacman.setDirection("stop")





    time.sleep(0.1)
