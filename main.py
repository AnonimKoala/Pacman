
import turtle as t
import time
from pacmanClass import Pacman

window = t.Screen()
window.setup(800, 800)
t.bgcolor("black")
window.tracer(0)


class Wall:
    def __init__(self, pos, size):
        self.wall = t.Turtle()
        self.wall.shape("square")
        self.wall.color("#001a8f")
        self.wall.penup()
        self.wall.shapesize(stretch_len=size[0], stretch_wid=size[1])
        self.wall.goto(pos[0], pos[1])



walls = []
walls.append(Wall((-350, -370), (2, 2)))
walls.append(Wall((0, 0), (2,2)))


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
            print(pacman.distance(wall.wall))
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
