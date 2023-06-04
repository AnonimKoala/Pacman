
import turtle as t
import time
from pacmanClass import Pacman
from enemiesClass import Enemy
from wallClass import Walls
from config import *
from importWalls import importWallsTab
from pointsClass import *


Walls.importWalls(importWallsTab)


pacman = Pacman()
Enemy.enemiesTab.append(Enemy('red',0))
Enemy.enemiesTab.append(Enemy("blue",1))
Enemy.enemiesTab.append(Enemy("pink",2))
Enemy.enemiesTab.append(Enemy("orange",3))


t.onkeypress(pacman.goUp, "Up")
t.onkeypress(pacman.goDown, "Down")
t.onkeypress(pacman.goLeft, "Left")
t.onkeypress(pacman.goRight, "Right")



Point(-240.0, 120.0)
Point(193.0, 271.0)
Point(-69.0, -331.0)
Point(-321.0, 330.0)
Point(134.0, 118.0)
Point(279.0, -228.0)

t.listen()

while True:
    window.update()
    pacman.move()


    pointShowFlag = False
    for point in Point.pointsTab:
        if pacman.distance(point.point) < 20 and point.getEaten() == False:
            point.packmanColission()


        if point.getEaten() == False:
            pointShowFlag = True

    if pointShowFlag == False:
        Point.showPoints()

    for enemy in Enemy.enemiesTab:
        enemy.move()  

    for wall in Walls.wallsTab:

        if pacman.pacman.pos()[0] < wall.wall.pos()[0] + wall.wall.width and pacman.pacman.pos()[0] + pacman.pacman.width > wall.wall.pos()[0] and pacman.pacman.pos()[1] < wall.wall.pos()[1] + wall.wall.height and pacman.pacman.pos()[1] + pacman.pacman.height > wall.wall.pos()[1]:
            pacman.wallColission()


        for enemy in Enemy.enemiesTab:
            if enemy.enemy.pos()[0] < wall.wall.pos()[0] + wall.wall.width and enemy.enemy.pos()[0] + enemy.enemy.width > wall.wall.pos()[0] and enemy.enemy.pos()[1] < wall.wall.pos()[1] + wall.wall.height and enemy.enemy.pos()[1] + enemy.enemy.height > wall.wall.pos()[1]:
                enemy.wallColission()

            if enemy.distance(pacman.pacman) < 40:
                updateScorebar()
                window.update()
                print("GAME OVER")
                time.sleep(2)
                window.bye()
                quit()
            



    

    time.sleep(0.01)
