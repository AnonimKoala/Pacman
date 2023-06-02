
import turtle as t
import time
from pacmanClass import Pacman
from enemiesClass import Enemy
from wallClass import Walls
from config import *
import json

jsonWrite = open("walls.json", "w")
jsonRead = open("walls.json", "r")












# Walls.drawWalls()
Walls.addWall(-380.00,260.00)



pacman = Pacman()
enemies = []
# enemies.append(Enemy('red',0))
# enemies.append(Enemy("blue",1))
# enemies.append(Enemy("pink",2))
# enemies.append(Enemy("orange",3))



t.onkeypress(pacman.goUp, "Up")
t.onkeypress(pacman.goDown, "Down")
t.onkeypress(pacman.goLeft, "Left")
t.onkeypress(pacman.goRight, "Right")





window.onclick(Walls.addWall)
window.onclick(Walls.deleteWall, 3)

def printAllWalls():
    allWalls = []
    for wall in Walls.wallsTab:
        allWalls.append(wall.wall.pos())
    print(allWalls)



# Clear all Walls
# Walls.wallsTab.clear()

t.onkeypress(printAllWalls, "p")

t.listen()
while True:
    window.update()
    pacman.move()
    for enemy in enemies:
        enemy.move()    


    for wall in Walls.wallsTab:
        if pacman.distance(wall.wall) < 45:
            pacman.wallColission()


        for enemy in enemies:
            if enemy.distance(wall.wall) < 45:
                enemy.wallColission()
            if enemy.distance(pacman.pacman) < 40:
                print("GAME OVER")
                time.sleep(1)
                window.bye()
                quit()
            





    time.sleep(0.05)
