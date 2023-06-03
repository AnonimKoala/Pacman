
import turtle as t
import time
from pacmanClass import Pacman
from enemiesClass import Enemy
from wallClass import Walls
from config import *
from importWalls import importWallsTab

Walls.importWalls(importWallsTab)


pacman = Pacman()
enemies = []
enemies.append(Enemy('red',0))
enemies.append(Enemy("blue",1))
enemies.append(Enemy("pink",2))
enemies.append(Enemy("orange",3))


t.onkeypress(pacman.goUp, "Up")
t.onkeypress(pacman.goDown, "Down")
t.onkeypress(pacman.goLeft, "Left")
t.onkeypress(pacman.goRight, "Right")



window.onclick(Walls.addWall)
window.onclick(Walls.deleteWall, 3)







t.onkeypress(Walls.printAllWalls, "p")

t.listen()
while True:
    window.update()
    pacman.move()
    for enemy in enemies:
        enemy.move()  

    for wall in Walls.wallsTab:

        if pacman.pacman.pos()[0] < wall.wall.pos()[0] + wall.wall.width and pacman.pacman.pos()[0] + pacman.pacman.width > wall.wall.pos()[0] and pacman.pacman.pos()[1] < wall.wall.pos()[1] + wall.wall.height and pacman.pacman.pos()[1] + pacman.pacman.height > wall.wall.pos()[1]:
            pacman.wallColission()


        for enemy in enemies:
            if enemy.enemy.pos()[0] < wall.wall.pos()[0] + wall.wall.width and enemy.enemy.pos()[0] + enemy.enemy.width > wall.wall.pos()[0] and enemy.enemy.pos()[1] < wall.wall.pos()[1] + wall.wall.height and enemy.enemy.pos()[1] + enemy.enemy.height > wall.wall.pos()[1]:
                enemy.wallColission()

            if enemy.distance(pacman.pacman) < 40:
                print("GAME OVER")
                time.sleep(1)
                window.bye()
                quit()
            





    time.sleep(0.01)
