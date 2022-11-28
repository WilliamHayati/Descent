import tkinter
from tkinter import *
import random

# RESOLUTION: 1366x768

def set_window_dimensions(w, h):
    window.title("Descent")
    res = str(w)+"x"+str(h)
    window.geometry(res)    

def move():
    global collisions, playerPos, m, pauseGame
    playerPos = canvas.coords(map["player"])
    # detects collisions
    collisions = canvas.find_overlapping(playerPos[0], playerPos[1], playerPos[2], playerPos[3])
    if m % 50 == 0:
        if pauseGame == False:
            projectile() # shoots bullet
    if len(collisions) == 1:
        if press == True and pauseGame == False:
            canvas.move(map["player"], x, y) # Moves player

    else:
        if collisions[1] == doorid:
            canvas.move(map["player"],x,y)
            nextRoom() # collision with door, takes player to next room
        elif (collisions[1] > (baseid + 11)) and (collisions[1] < (baseid + 12 + numOfEnemies)):
            if press == True and pauseGame == False:
                canvas.move(map["player"], x, y)

        elif (collisions[1] < (baseid + 12)) and pauseGame == False and press == True:
            # collision with walls and obstacles, moves player in opposing direction
            if direction == "left":
                canvas.move(map["player"], -x +1, 0)
            if direction == "right":
                canvas.move(map["player"], -x -1, 0)
            if direction == "up":
                canvas.move(map["player"], 0, -y + 1)
            if direction == "down":
                canvas.move(map["player"], 0, -y -1)
        else:
            if press == True and pauseGame == False:
                canvas.move(map["player"], x, y)
    m = m + 1
    
    window.after(10, move)

def keyPressed(event):
    global x, y, press, direction, coords, level, enemySpeed, enemyHealth, enemyDamage, power, health, leftKey, rightKey, upKey, downKey
    press = True
    x = 0
    y = 0
    if event.char == "H": # Cheat code that gives player more health
        health = health + 50
        healthDisplay.destroy()
        healthDisplay = Label(window, text=("Health: "+str(health)), bg = "purple", fg = "crimson", font=("Helvetica", 18),width = 20)
        healthDisplay.place(x = 100, y = 3)
        # updates health display text

    elif event.char == "p" and pauseGame == False:
        pause() # Pause game
    elif event.char == "]":
        global bossOpen
        if bossOpen == False:
            bossOpen = True
        else:
            bossOpen = False
        bossKey() # Boss key

    if len(collisions) > 0:
        #Determines direction based on key pressed
        if event.char == leftKey:
            x = left
            direction = "left"
        elif event.char == rightKey:
            x = right
            direction = "right"
        elif event.char == upKey:
            y = up
            direction = "up"
        elif event.char == downKey:
            y = down
            direction = "down"
    else:
        id = collisions[1]
        objectcoll = "wall"+str(id)
def keyReleased(event):
    # lets the program know that the player has released the key
    global press
    press = False

def projectile():
    global m, decay, bullx, bully
    # determines direction the bullet moves, this is the same direction as the player at that instance
    if direction == "left":
        map["bullet"] = canvas.create_oval(playerPos[0]-10, playerPos[1]+10,playerPos[0],playerPos[3]-10, fill="crimson")
        decay = 0
        bullx = x
        bully = y
        moveProjectile()
    if direction == "right":
        map["bullet"] = canvas.create_oval(playerPos[2], playerPos[1]+10,playerPos[2]+10,playerPos[3]-10, fill="crimson")
        decay = 0
        bullx = x
        bully = y
        moveProjectile()
    if direction == "up":
        map["bullet"] = canvas.create_oval(playerPos[0]+10, playerPos[1]-10,playerPos[0]+20,playerPos[1], fill="crimson")
        decay = 0
        bullx = x
        bully = y
        moveProjectile()
    if direction == "down":
        map["bullet"] = canvas.create_oval(playerPos[0]+10, playerPos[3],playerPos[0]+20,playerPos[3]+10, fill="crimson")
        decay = 0
        bullx = x
        bully = y
        moveProjectile()
          
def moveProjectile():
    global decay, projectilePos
    projectilePos = canvas.coords(map["bullet"])
    canvas.move(map["bullet"], bulletSpeed*bullx, bulletSpeed*bully)
    decay = decay + 1
    projectileColl = canvas.find_overlapping(projectilePos[0], projectilePos[1], projectilePos[2], projectilePos[3])
    # detects collisions with the bullet
    # variable decay gives the bullet a cooldown
    if len(projectileColl) > 0:

        if (projectileColl[0] < (baseid+12)) and (projectileColl[0] > (baseid+1)):
            decay = 50
        elif len(projectileColl) == 2:
            if (projectileColl[1] < (baseid+12)) and (projectileColl[1] > (baseid+1)):
                decay = 50
    if decay < 50:
        window.after(10,moveProjectile)


# Series of rooms that can be picked from every time the player goes through a door
def room1():
    # In each room there is a program that defines the coordinates that enemies should be able to spawn in
    global enemyCoords
    def enemyCoords(): 
        global ex, ey 
        ex = random.randint(100, width-100)
        ey = random.randint(100, height-100)
        while ey > 300 and ey < 468:
            ey = random.randint(100, height-100)
            
    # Creates the formation and obstacles for  this room
    map["wall2"] = canvas.create_rectangle((0, 0), (30, height), fill = "purple", width = 0)
    map["wall3"] = canvas.create_rectangle((0, 0), (width, 30), fill = "purple", width = 0)
    map["wall4"] = canvas.create_rectangle((0, height-30 ), (width, height ), fill = "purple", width = 0)
    map["wall5"] = canvas.create_rectangle((width-30, 0 ), (width, height ), fill = "purple", width = 0)

    map["wall6"] = canvas.create_rectangle((0, 0), (0, 0), fill = "purple", width = 0)
    map["wall7"] = canvas.create_rectangle((0, 0), (0, 0), fill = "purple", width = 0)
    map["wall8"] = canvas.create_rectangle((0, 0), (0, 0), fill = "purple", width = 0)
    map["wall9"] = canvas.create_rectangle((0, 0), (0, 0), fill = "purple", width = 0)
    map["wall10"] = canvas.create_rectangle((0, 0), (0, 0), fill = "purple", width = 0)
    map["wall11"] = canvas.create_rectangle((0, 0), (0, 0), fill = "purple", width = 0)
def room2():
    global enemyCoords
    def enemyCoords(): 
        global ex, ey 
        ey = random.randint(100, height-100)
        while ey > 300 and ey < 468:
            ey = random.randint(100, height-100)
        ex = random.randint(100, width - 100)
        while (ex > 180 and ex < 580) or (ex > 750 and ex <1210):
            ex = random.randint(100, height-100)

    map["wall2"] = canvas.create_rectangle((0, 0), (30, height), fill = "purple", width = 0)
    map["wall3"] = canvas.create_rectangle((0, 0), (width, 30), fill = "purple", width = 0)
    map["wall4"] = canvas.create_rectangle((0, height-30 ), (width, height ), fill = "purple", width = 0)
    map["wall5"] = canvas.create_rectangle((width-30, 0 ), (width, height ), fill = "purple", width = 0)

    map["wall6"] = canvas.create_rectangle((250, 0), (500, 600), fill = "purple", width = 0)
    map["wall7"] = canvas.create_rectangle((width - 500, height-600), (width - 250, height), fill = "purple", width = 0)

    map["wall8"] = canvas.create_rectangle((0, 0), (0, 0), fill = "purple", width = 0)
    map["wall9"] = canvas.create_rectangle((0, 0), (0, 0), fill = "purple", width = 0)
    map["wall10"] = canvas.create_rectangle((0, 0), (0, 0), fill = "purple", width = 0)
    map["wall11"] = canvas.create_rectangle((0, 0), (0, 0), fill = "purple", width = 0)
def room3():
    global enemyCoords
    def enemyCoords(): 
        global ex, ey 
        ex = random.randint(380, width-940)
        ey = random.randint(100, height-100)
        while ey > 300 and ey < 468:
            ey = random.randint(100, height-100)

    map["wall2"] = canvas.create_rectangle((0, 0), (30, height), fill = "purple", width = 0)
    map["wall3"] = canvas.create_rectangle((0, 0), (width, 30), fill = "purple", width = 0)
    map["wall4"] = canvas.create_rectangle((0, height-30 ), (width, height ), fill = "purple", width = 0)
    map["wall5"] = canvas.create_rectangle((width-30, 0 ), (width, height ), fill = "purple", width = 0)

    map["wall6"] = canvas.create_rectangle((0, 0), (300, height), fill = "purple", width = 0)
    map["wall7"] = canvas.create_rectangle((width-300, 0), (width, height), fill = "purple", width = 0)

    map["wall8"] = canvas.create_rectangle((0, 0), (0, 0), fill = "purple", width = 0)
    map["wall9"] = canvas.create_rectangle((0, 0), (0, 0), fill = "purple", width = 0)
    map["wall10"] = canvas.create_rectangle((0, 0), (0, 0), fill = "purple", width = 0)
    map["wall11"] = canvas.create_rectangle((0, 0), (0, 0), fill = "purple", width = 0)
def room4():
    global enemyCoords
    def enemyCoords(): 
        global ex, ey 
        ey = random.randint(270, height-270)
        ex = random.randint(100, width-100)
        while ex > 450 and ex < (width-450):
            ex = random.randint(100, width-100)

    map["wall2"] = canvas.create_rectangle((0, 0), (30, height), fill = "purple", width = 0)
    map["wall3"] = canvas.create_rectangle((0, 0), (width, 30), fill = "purple", width = 0)
    map["wall4"] = canvas.create_rectangle((0, height-30 ), (width, height ), fill = "purple", width = 0)
    map["wall5"] = canvas.create_rectangle((width-30, 0 ), (width, height ), fill = "purple", width = 0)

    map["wall6"] = canvas.create_rectangle((0, 0), (width, 200), fill = "purple", width = 0)
    map["wall7"] = canvas.create_rectangle((0, height - 200), (width, height), fill = "purple", width = 0)

    map["wall8"] = canvas.create_rectangle((0, 0), (0, 0), fill = "purple", width = 0)
    map["wall9"] = canvas.create_rectangle((0, 0), (0, 0), fill = "purple", width = 0)
    map["wall10"] = canvas.create_rectangle((0, 0), (0, 0), fill = "purple", width = 0)
    map["wall11"] = canvas.create_rectangle((0, 0), (0, 0), fill = "purple", width = 0)
def room5():
    global enemyCoords
    def enemyCoords(): 
        global ex, ey 
        ey = random.randint(100, height-100)
        ex = random.randint(100, width-100)
        while ex > 330 and ex < (width-330):
            ex = random.randint(100, width-100)

    map["wall2"] = canvas.create_rectangle((0, 0), (30, height), fill = "purple", width = 0)
    map["wall3"] = canvas.create_rectangle((0, 0), (width, 30), fill = "purple", width = 0)
    map["wall4"] = canvas.create_rectangle((0, height-30 ), (width, height ), fill = "purple", width = 0)
    map["wall5"] = canvas.create_rectangle((width-30, 0 ), (width, height ), fill = "purple", width = 0)

    map["wall6"] = canvas.create_rectangle((400, 0), (width - 400, 300), fill = "purple", width = 0)
    map["wall7"] = canvas.create_rectangle((400, height - 300), (width - 400, height), fill = "purple", width = 0)

    map["wall8"] = canvas.create_rectangle((0, 0), (0, 0), fill = "purple", width = 0)
    map["wall9"] = canvas.create_rectangle((0, 0), (0, 0), fill = "purple", width = 0)
    map["wall10"] = canvas.create_rectangle((0, 0), (0, 0), fill = "purple", width = 0)
    map["wall11"] = canvas.create_rectangle((0, 0), (0, 0), fill = "purple", width = 0)
def room6():
    global enemyCoords
    def enemyCoords(): 
        global ex, ey 
        ex = random.randint(100, width-100)
        ey = random.randint(100, height-100)
        while ey > 230 and ey < 550:
            ey = random.randint(100, height-100)

    map["wall2"] = canvas.create_rectangle((0, 0), (30, height), fill = "purple", width = 0)
    map["wall3"] = canvas.create_rectangle((0, 0), (width, 30), fill = "purple", width = 0)
    map["wall4"] = canvas.create_rectangle((0, height-30 ), (width, height ), fill = "purple", width = 0)
    map["wall5"] = canvas.create_rectangle((width-30, 0 ), (width, height ), fill = "purple", width = 0)

    map["wall6"] = canvas.create_rectangle((0, 300), (600, height-300), fill = "purple", width = 0)
    map["wall7"] = canvas.create_rectangle((width - 600, 300), (width, height-300), fill = "purple", width = 0)

    map["wall8"] = canvas.create_rectangle((0, 0), (0, 0), fill = "purple", width = 0)
    map["wall9"] = canvas.create_rectangle((0, 0), (0, 0), fill = "purple", width = 0)
    map["wall10"] = canvas.create_rectangle((0, 0), (0, 0), fill = "purple", width = 0)
    map["wall11"] = canvas.create_rectangle((0, 0), (0, 0), fill = "purple", width = 0)
def room7():
    global enemyCoords
    def enemyCoords(): 
        global ex, ey 
        ex = random.randint(100, width-100)
        while (ex > 230 and ex < 470) or (ex > 900 and ex < 1140):
            ex = random.randint(100, width-100)
        ey = random.randint(100, height-100)
        while ey > 230 and ey < 550:
            ey = random.randint(100, height-100)

    map["wall2"] = canvas.create_rectangle((0, 0), (30, height), fill = "purple", width = 0)
    map["wall3"] = canvas.create_rectangle((0, 0), (width, 30), fill = "purple", width = 0)
    map["wall4"] = canvas.create_rectangle((0, height-30 ), (width, height ), fill = "purple", width = 0)
    map["wall5"] = canvas.create_rectangle((width-30, 0 ), (width, height ), fill = "purple", width = 0)

    map["wall6"] = canvas.create_rectangle((0, 300), (600, height-300), fill = "purple", width = 0)
    map["wall7"] = canvas.create_rectangle((width - 600, 300), (width, height-300), fill = "purple", width = 0)
    map["wall8"] = canvas.create_rectangle((300, 0), (400, 200), fill = "purple", width = 0)
    map["wall9"] = canvas.create_rectangle((width-400, 0), (width-300, 200), fill = "purple", width = 0)
    map["wall10"] = canvas.create_rectangle((300, height-200), (400, height), fill = "purple", width = 0)
    map["wall11"] = canvas.create_rectangle((width-400, height-200), (width-300, height), fill = "purple", width = 0)
def room8():
    global enemyCoords
    def enemyCoords(): 
        global ex, ey 
        ex = random.randint(100, width-100)
        while (ex > 910 and ex < 1160):
            ex = random.randint(100, width-100)
        ey = random.randint(300, height-100)

    map["wall2"] = canvas.create_rectangle((0, 0), (30, height), fill = "purple", width = 0)
    map["wall3"] = canvas.create_rectangle((0, 0), (width, 30), fill = "purple", width = 0)
    map["wall4"] = canvas.create_rectangle((0, height-30 ), (width, height ), fill = "purple", width = 0)
    map["wall5"] = canvas.create_rectangle((width-30, 0 ), (width, height ), fill = "purple", width = 0)

    map["wall6"] = canvas.create_rectangle(((width/2)-300, (height/2)-250), ((width/2)+400, (height/2)-150), fill = "purple", width = 0)
    map["wall7"] = canvas.create_rectangle(((width/2)+300, (height/2)-250), ((width/2)+400, (height/2)+200), fill = "purple", width = 0)

    map["wall8"] = canvas.create_rectangle((0, 0), (0, 0), fill = "purple", width = 0)
    map["wall9"] = canvas.create_rectangle((0, 0), (0, 0), fill = "purple", width = 0)
    map["wall10"] = canvas.create_rectangle((0, 0), (0, 0), fill = "purple", width = 0)
    map["wall11"] = canvas.create_rectangle((0, 0), (0, 0), fill = "purple", width = 0)
def room9():
    global enemyCoords
    def enemyCoords(): 
        global ex, ey 
        ey = random.randint(100, height-100)
        ex = random.randint(100, width-100)
        while (ex > 170 and ex < 470) or (ex > 890 and ex < 1190):
            ex = random.randint(100, width-100)

    map["wall2"] = canvas.create_rectangle((0, 0), (30, height), fill = "purple", width = 0)
    map["wall3"] = canvas.create_rectangle((0, 0), (width, 30), fill = "purple", width = 0)
    map["wall4"] = canvas.create_rectangle((0, height-30 ), (width, height ), fill = "purple", width = 0)
    map["wall5"] = canvas.create_rectangle((width-30, 0 ), (width, height ), fill = "purple", width = 0)

    map["wall6"] = canvas.create_rectangle((200, (height/2)-200), (400, (height/2)+200), fill = "purple", width = 0)
    map["wall7"] = canvas.create_rectangle((width-400, (height/2)-200), (width-200, (height/2)+200), fill = "purple", width = 0)

    map["wall8"] = canvas.create_rectangle((0, 0), (0, 0), fill = "purple", width = 0)
    map["wall9"] = canvas.create_rectangle((0, 0), (0, 0), fill = "purple", width = 0)
    map["wall10"] = canvas.create_rectangle((0, 0), (0, 0), fill = "purple", width = 0)
    map["wall11"] = canvas.create_rectangle((0, 0), (0, 0), fill = "purple", width = 0)
def room10():
    global enemyCoords
    def enemyCoords(): 
        global ex, ey 
        ex = random.randint(100, width-100)
        ey = random.randint(100, height-100)
        if (ex < 570) or (ex > 800):
            while (ey < 320) or (ey > 430):
                ey = random.randint(100, height-100) 
        else:
            while ey > 300 and ey < 468:
                ey = random.randint(100, height-100)
          

    map["wall2"] = canvas.create_rectangle((0, 0), (30, height), fill = "purple", width = 0)
    map["wall3"] = canvas.create_rectangle((0, 0), (width, 30), fill = "purple", width = 0)
    map["wall4"] = canvas.create_rectangle((0, height-30 ), (width, height ), fill = "purple", width = 0)
    map["wall5"] = canvas.create_rectangle((width-30, 0 ), (width, height ), fill = "purple", width = 0)

    map["wall6"] = canvas.create_rectangle((0, 0), (500, 250), fill = "purple", width = 0)
    map["wall7"] = canvas.create_rectangle((width-500, 0), (width, 250), fill = "purple", width = 0)
    map["wall8"] = canvas.create_rectangle((0, height), (500, height-250), fill = "purple", width = 0)
    map["wall9"] = canvas.create_rectangle((width-500, height), (width, height-250), fill = "purple", width = 0)

    map["wall10"] = canvas.create_rectangle((0, 0), (0, 0), fill = "purple", width = 0)
    map["wall11"] = canvas.create_rectangle((0, 0), (0, 0), fill = "purple", width = 0)

def nextRoom():
    global baseid, enemiesDefeated, level, enemyHealth, enemySpeed, enemyDamage, levelDisplay
    enemiesDefeated = 0
    level = level + 1 # Next level
    # Make enemies more difficult by a factor of the level the player is on
    if level % 2 == 0:
        enemyHealth = enemyHealth +1
    enemySpeed = enemySpeed * 1.05
    enemyDamageFl = enemyDamage * 1.1
    enemyDamage = int(enemyDamageFl)

    canvas.delete("all") #Delete all items to recreate
    map["baseID"] = canvas.create_rectangle((0,0),(0,0), fill="steel blue")
    idcoords = canvas.coords(map["baseID"])
    baseid = canvas.find_overlapping(idcoords[0], idcoords[1], idcoords[2], idcoords[3])
    baseid = baseid[0] # determine the id of the first object for reference
    levelDisplay.destroy()
    # update text to display level
    levelDisplay = Label(window, text=("Floor: "+str(level)), bg = "purple", fg = "crimson", font=("Helvetica", 18))
    levelDisplay.place(x = 30, y = 3)
    # reinstantiate player
    map["player"] = canvas.create_rectangle((width/2,height/2),(width/2 + player_size,height/2 + player_size), fill=playerColour)
    # choose a random room from 1 to 10 and call its function
    roomnum = random.randint(1,10)
    roomfunc = globals()["room"+str(roomnum)]
    roomfunc()
    spawnEnemies()

def openSesame():
    global doorid
    # Spawn in the door
    map["door"] = canvas.create_image((width/2)-60,(height/2)+10,image=doorimg)
    doorcoords = canvas.coords(map["door"])
    # determine doors id
    doorid = canvas.find_overlapping(doorcoords[0], doorcoords[1], doorcoords[0]+1,doorcoords[1]+1)
    doorid = doorid[0]


        
def spawnEnemies():
    global numOfEnemy1, numOfEnemy2, numOfEnemy3, numOfEnemy4, numOfEnemy5
    numOfEnemy1 = 0
    numOfEnemy2 = 0
    numOfEnemy3 = 0
    numOfEnemy4 = 0
    numOfEnemy5 = 0
    global numOfEnemies
    numOfEnemies = random.randint(3,5) # randomly chooses number of enemies to be spawned
    for i in range(numOfEnemies):
        enemyNum = random.randint(1,5) # randomly chooses type of enemy to spawn in and calls that enemies function as well as generating its unique name
        if enemyNum == 1:
            numOfEnemy1 = numOfEnemy1 + 1
            enemyfunc = globals()["enemy"+str(enemyNum)+str(numOfEnemy1)]
        if enemyNum == 2:
            numOfEnemy2 = numOfEnemy2 + 1
            enemyfunc = globals()["enemy"+str(enemyNum)+str(numOfEnemy2)]
        if enemyNum == 3:
            numOfEnemy3 = numOfEnemy3 + 1
            enemyfunc = globals()["enemy"+str(enemyNum)+str(numOfEnemy3)]
        if enemyNum == 4:
            numOfEnemy4 = numOfEnemy4 + 1
            enemyfunc = globals()["enemy"+str(enemyNum)+str(numOfEnemy4)]
        if enemyNum == 5:
            numOfEnemy5 = numOfEnemy5 + 1
            enemyfunc = globals()["enemy"+str(enemyNum)+str(numOfEnemy5)]
        enemyfunc()

# there are 5 duplicates of each enemy type to allow for the maximum amount of enemies 5, to be instantiated

def enemy11():
    global numOfEnemy1,e11x,enemyName11,enemy11Health, enemy11Val
    e11x = enemySpeed 
    enemy11Health = enemyHealth
    enemyCoords()
    enemyName11 = "enemy1."+str(numOfEnemy1)
    map[enemyName11] = canvas.create_image(ex,ey,image=enemy1img) #instantiate enemy
    enemy11Val = map[enemyName11]
    enemy11Move()
def enemy11Move():
    # moves left and right, changing direction when colliding with wall
    global e11x, enemy11Health, projectileHit, enemiesDefeated
    if pauseGame == False:
        canvas.move(map[enemyName11], e11x , 0) #move
    enemy11Pos = canvas.coords(map[enemyName11])
    enemy11Coll = canvas.find_overlapping(enemy11Pos[0]-25, enemy11Pos[1]-25, enemy11Pos[0]+25, enemy11Pos[1]+25)
    # detect collisions with this enemy
    if pauseGame == False:
        if len(enemy11Coll) > 2:
            enemy11Health = enemy11Health - power # take damage
            if enemy11Health == 0:
                canvas.delete(map[enemyName11]) # enemy destroyed when it loses all its health
                enemiesDefeated = enemiesDefeated + 1
                if enemiesDefeated == numOfEnemies:
                    # if all enemies are defeated open the door
                    openSesame()
        if len(enemy11Coll) > 1:
            if enemy11Coll[0] != enemy11Val:
                if (enemy11Coll[0] > (baseid+1)) and (enemy11Coll[0] < (baseid+12)):
                    # collide with wall - change direction
                    e11x = -e11x
                elif enemy11Coll[0] == (baseid+1):
                    # collide with player, player takes damage
                    projectileHit = False
                    damagePlayer()
            else:
                if (enemy11Coll[1] > (baseid+12+numOfEnemies)):
                    # if hit by bullet, take damage
                    enemy11Health = enemy11Health - power
                    if enemy11Health == 0:
                        canvas.delete(map[enemyName11]) # enemy destroyed when it loses all its health
                        enemiesDefeated = enemiesDefeated + 1
                        if enemiesDefeated == numOfEnemies:
                            openSesame()
    window.after(10,enemy11Move)

def enemy12():
    global numOfEnemy1,e12x,enemyName12,enemy12Health, enemy12Val
    e12x = enemySpeed
    enemy12Health = enemyHealth
    enemyCoords()
    enemyName12 = "enemy1."+str(numOfEnemy1)
    map[enemyName12] = canvas.create_image(ex,ey,image=enemy1img)
    enemy12Val = map[enemyName12]
    enemy12Move()
def enemy12Move():
    # moves left and right, changing direction when colliding with wall
    global e12x, enemy12Health, projectileHit, enemiesDefeated
    if pauseGame == False:
        canvas.move(map[enemyName12], e12x , 0)
    enemy12Pos = canvas.coords(map[enemyName12])
    enemy12Coll = canvas.find_overlapping(enemy12Pos[0]-25, enemy12Pos[1]-25, enemy12Pos[0]+25, enemy12Pos[1]+25)
    if pauseGame == False:

        if len(enemy12Coll) > 2:
            enemy12Health = enemy12Health - power
            if enemy12Health == 0:
                canvas.delete(map[enemyName12])
                enemiesDefeated = enemiesDefeated + 1
                if enemiesDefeated == numOfEnemies:
                    openSesame()

        if len(enemy12Coll) > 1:
            if enemy12Coll[0] != enemy12Val:
                if (enemy12Coll[0] > (baseid+1)) and (enemy12Coll[0] < (baseid+12)):
                    e12x = -e12x
                elif enemy12Coll[0] == (baseid+1):
                    projectileHit = False
                    damagePlayer()
            else:
                if (enemy12Coll[1] > (baseid+12+numOfEnemies)):
                    enemy12Health = enemy12Health - power
                    if enemy12Health == 0:
                        canvas.delete(map[enemyName12])
                        enemiesDefeated = enemiesDefeated + 1
                        if enemiesDefeated == numOfEnemies:
                            openSesame()
    window.after(10,enemy12Move)

def enemy13():
    global numOfEnemy1,e13x,enemyName13,enemy13Health, enemy13Val
    e13x = enemySpeed
    enemy13Health = enemyHealth
    enemyCoords()
    enemyName13 = "enemy1."+str(numOfEnemy1)
    map[enemyName13] = canvas.create_image(ex,ey,image=enemy1img)
    enemy13Val = map[enemyName13]
    enemy13Move()
def enemy13Move():
    # moves left and right, changing direction when colliding with wall
    global e13x, enemy13Health, projectileHit, enemiesDefeated
    if pauseGame == False:
        canvas.move(map[enemyName13], e13x , 0)
    enemy13Pos = canvas.coords(map[enemyName13])
    enemy13Coll = canvas.find_overlapping(enemy13Pos[0]-25, enemy13Pos[1]-25, enemy13Pos[0]+25, enemy13Pos[1]+25)
    if pauseGame == False:

        if len(enemy13Coll) > 2:
            enemy13Health = enemy13Health - power
            if enemy13Health == 0:
                canvas.delete(map[enemyName13])
                enemiesDefeated = enemiesDefeated + 1
                if enemiesDefeated == numOfEnemies:
                    openSesame()

        if len(enemy13Coll) > 1:
            if enemy13Coll[0] != enemy13Val:
                if (enemy13Coll[0] > (baseid+1)) and (enemy13Coll[0] < (baseid+12)):
                    e13x = -e13x
                elif enemy13Coll[0] == (baseid+1):
                    projectileHit = False
                    damagePlayer()
            else:
                if (enemy13Coll[1] > (baseid+12+numOfEnemies)):
                    enemy13Health = enemy13Health - power
                    if enemy13Health == 0:
                        canvas.delete(map[enemyName13])
                        enemiesDefeated = enemiesDefeated + 1
                        if enemiesDefeated == numOfEnemies:
                            openSesame()
    window.after(10,enemy13Move)

def enemy14():
    global numOfEnemy1,e14x,enemyName14,enemy14Health, enemy14Val
    e14x = enemySpeed
    enemy14Health = enemyHealth
    enemyCoords()
    enemyName14 = "enemy1."+str(numOfEnemy1)
    map[enemyName14] = canvas.create_image(ex,ey,image=enemy1img)
    enemy14Val = map[enemyName14]
    enemy14Move()
def enemy14Move():
    # moves left and right, changing direction when colliding with wall
    global e14x, enemy14Health, projectileHit, enemiesDefeated
    if pauseGame == False:
        canvas.move(map[enemyName14], e14x , 0)
    enemy14Pos = canvas.coords(map[enemyName14])
    enemy14Coll = canvas.find_overlapping(enemy14Pos[0]-25, enemy14Pos[1]-25, enemy14Pos[0]+25, enemy14Pos[1]+25)
    if pauseGame == False:

        if len(enemy14Coll) > 2:
            enemy14Health = enemy14Health - power
            if enemy14Health == 0:
                canvas.delete(map[enemyName14])
                enemiesDefeated = enemiesDefeated + 1
                if enemiesDefeated == numOfEnemies:
                    openSesame()

        if len(enemy14Coll) > 1:
            if enemy14Coll[0] != enemy14Val:
                if (enemy14Coll[0] > (baseid+1)) and (enemy14Coll[0] < (baseid+12)):
                    e14x = -e14x
                elif enemy14Coll[0] == (baseid+1):
                    projectileHit = False
                    damagePlayer()
            else:
                if (enemy14Coll[1] > (baseid+12+numOfEnemies)):
                    enemy14Health = enemy14Health - power
                    if enemy14Health == 0:
                        canvas.delete(map[enemyName14])
                        enemiesDefeated = enemiesDefeated + 1
                        if enemiesDefeated == numOfEnemies:
                            openSesame()
    window.after(10,enemy14Move)

def enemy15():
    global numOfEnemy1,e15x,enemyName15,enemy15Health, enemy15Val
    e15x = enemySpeed
    enemy15Health = enemyHealth
    enemyCoords()
    enemyName15 = "enemy1."+str(numOfEnemy1)
    map[enemyName15] = canvas.create_image(ex,ey,image=enemy1img)
    enemy15Val = map[enemyName15]
    enemy15Move()
def enemy15Move():
    # moves left and right, changing direction when colliding with wall
    global e15x, enemy15Health, projectileHit, enemiesDefeated
    if pauseGame == False:
        canvas.move(map[enemyName15], e15x , 0)
    enemy15Pos = canvas.coords(map[enemyName15])
    enemy15Coll = canvas.find_overlapping(enemy15Pos[0]-25, enemy15Pos[1]-25, enemy15Pos[0]+25, enemy15Pos[1]+25)
    if pauseGame == False:

        if len(enemy15Coll) > 2:
            enemy15Health = enemy15Health - power
            if enemy15Health == 0:
                canvas.delete(map[enemyName15])
                enemiesDefeated = enemiesDefeated + 1
                if enemiesDefeated == numOfEnemies:
                    openSesame()

        if len(enemy15Coll) > 1:
            if enemy15Coll[0] != enemy15Val:
                if (enemy15Coll[0] > (baseid+1)) and (enemy15Coll[0] < (baseid+12)):
                    e15x = -e15x
                elif enemy15Coll[0] == (baseid+1):
                    projectileHit = False
                    damagePlayer()
            else:
                if (enemy15Coll[1] > (baseid+12+numOfEnemies)):
                    enemy15Health = enemy15Health - power
                    if enemy15Health == 0:
                        canvas.delete(map[enemyName15])
                        enemiesDefeated = enemiesDefeated + 1
                        if enemiesDefeated == numOfEnemies:
                            openSesame()
    window.after(10,enemy15Move)


def enemy21():
    global numOfEnemy2,e21y,enemyName21,enemy21Health, enemy21Val
    e21y = enemySpeed
    enemy21Health = enemyHealth
    enemyCoords()
    enemyName21 = "enemy2."+str(numOfEnemy2)
    map[enemyName21] = canvas.create_image(ex,ey,image=enemy2img)
    enemy21Val = map[enemyName21]
    enemy21Move()
def enemy21Move():
    # moves up and down, changing direction when colliding with wall
    global e21y, enemy21Health, projectileHit, enemiesDefeated
    if pauseGame == False:
        canvas.move(map[enemyName21], 0 , e21y)
    enemy21Pos = canvas.coords(map[enemyName21])
    enemy21Coll = canvas.find_overlapping(enemy21Pos[0]-25, enemy21Pos[1]-25, enemy21Pos[0]+25, enemy21Pos[1]+25)
    if pauseGame == False:
        if len(enemy21Coll) > 2:
            enemy21Health = enemy21Health - power
            if enemy21Health == 0:
                canvas.delete(map[enemyName21])
                enemiesDefeated = enemiesDefeated + 1
                if enemiesDefeated == numOfEnemies:
                    openSesame()

        if len(enemy21Coll) > 1:
            if enemy21Coll[0] != enemy21Val:
                if (enemy21Coll[0] > (baseid+1)) and (enemy21Coll[0] < (baseid+11)):
                    e21y = -e21y
                elif enemy21Coll[0] == (baseid+1):
                    projectileHit = False
                    damagePlayer()
            else:
                if (enemy21Coll[1] > (baseid+12+numOfEnemies)):
                    enemy21Health = enemy21Health - power
                    if enemy21Health == 0:
                        canvas.delete(map[enemyName21])
                        enemiesDefeated = enemiesDefeated + 1
                        if enemiesDefeated == numOfEnemies:
                            openSesame()
    window.after(10,enemy21Move)

def enemy22():
    global numOfEnemy2,e22y,enemyName22,enemy22Health, enemy22Val
    e22y = enemySpeed
    enemy22Health = enemyHealth
    enemyCoords()
    enemyName22 = "enemy2."+str(numOfEnemy2)
    map[enemyName22] = canvas.create_image(ex,ey,image=enemy2img)
    enemy22Val = map[enemyName22]
    enemy22Move()
def enemy22Move():
    # moves up and down, changing direction when colliding with wall
    global e22y, enemy22Health, projectileHit, enemiesDefeated
    if pauseGame == False:

        canvas.move(map[enemyName22], 0 , e22y)
    enemy22Pos = canvas.coords(map[enemyName22])
    enemy22Coll = canvas.find_overlapping(enemy22Pos[0]-25, enemy22Pos[1]-25, enemy22Pos[0]+25, enemy22Pos[1]+25)
    if pauseGame == False:

        if len(enemy22Coll) > 2:
            enemy22Health = enemy22Health - power
            if enemy22Health == 0:
                canvas.delete(map[enemyName22])
                enemiesDefeated = enemiesDefeated + 1
                if enemiesDefeated == numOfEnemies:
                    openSesame()
        
        if len(enemy22Coll) > 1:
            if enemy22Coll[0] != enemy22Val:
                if (enemy22Coll[0] > (baseid+1)) and (enemy22Coll[0] < (baseid+11)):
                    e22y = -e22y
                elif enemy22Coll[0] == (baseid+1):
                    projectileHit = False
                    damagePlayer()
            else:
                if (enemy22Coll[1] > (baseid+12+numOfEnemies)):
                    enemy22Health = enemy22Health - power
                    if enemy22Health == 0:
                        canvas.delete(map[enemyName22])
                        enemiesDefeated = enemiesDefeated + 1
                        if enemiesDefeated == numOfEnemies:
                            openSesame()
    window.after(10,enemy22Move)

def enemy23():
    global numOfEnemy2,e23y,enemyName23,enemy23Health, enemy23Val
    e23y = enemySpeed
    enemy23Health = enemyHealth
    enemyCoords()
    enemyName23 = "enemy2."+str(numOfEnemy2)
    map[enemyName23] = canvas.create_image(ex,ey,image=enemy2img)
    enemy23Val = map[enemyName23]
    enemy23Move()
def enemy23Move():
    # moves up and down, changing direction when colliding with wall
    global e23y, enemy23Health, projectileHit, enemiesDefeated
    if pauseGame == False:
        canvas.move(map[enemyName23], 0 , e23y)
    enemy23Pos = canvas.coords(map[enemyName23])
    enemy23Coll = canvas.find_overlapping(enemy23Pos[0]-25, enemy23Pos[1]-25, enemy23Pos[0]+25, enemy23Pos[1]+25)
    if pauseGame == False:

        if len(enemy23Coll) > 2:
            enemy23Health = enemy23Health - power
            if enemy23Health == 0:
                canvas.delete(map[enemyName23])
                enemiesDefeated = enemiesDefeated + 1
                if enemiesDefeated == numOfEnemies:
                    openSesame()
        
        if len(enemy23Coll) > 1:
            if enemy23Coll[0] != enemy23Val:
                if (enemy23Coll[0] > (baseid+1)) and (enemy23Coll[0] < (baseid+11)):
                    e23y = -e23y
                elif enemy23Coll[0] == (baseid+1):
                    projectileHit = False
                    damagePlayer()
            else:
                if (enemy23Coll[1] > (baseid+12+numOfEnemies)):
                    enemy23Health = enemy23Health - power
                    if enemy23Health == 0:
                        canvas.delete(map[enemyName23])
                        enemiesDefeated = enemiesDefeated + 1
                        if enemiesDefeated == numOfEnemies:
                            openSesame()
    window.after(10,enemy23Move)

def enemy24():
    global numOfEnemy2,e24y,enemyName24,enemy24Health, enemy24Val
    e24y = enemySpeed
    enemy24Health = enemyHealth
    enemyCoords()
    enemyName24 = "enemy2."+str(numOfEnemy2)
    map[enemyName24] = canvas.create_image(ex,ey,image=enemy2img)
    enemy24Val = map[enemyName24]
    enemy24Move()
def enemy24Move():
    # moves up and down, changing direction when colliding with wall
    global e24y, enemy24Health, projectileHit, enemiesDefeated
    if pauseGame == False:
        canvas.move(map[enemyName24], 0 , e24y)
    enemy24Pos = canvas.coords(map[enemyName24])
    enemy24Coll = canvas.find_overlapping(enemy24Pos[0]-25, enemy24Pos[1]-25, enemy24Pos[0]+25, enemy24Pos[1]+25)
    if pauseGame == False:

        if len(enemy24Coll) > 2:
            enemy25Health = enemy25Health - power
            if enemy25Health == 0:
                canvas.delete(map[enemyName25])
                enemiesDefeated = enemiesDefeated + 1
                if enemiesDefeated == numOfEnemies:
                    openSesame()
        
        if len(enemy24Coll) > 1:
            if enemy24Coll[0] != enemy24Val:
                if (enemy24Coll[0] > (baseid+1)) and (enemy24Coll[0] < (baseid+11)):
                    e24y = -e24y
                elif enemy24Coll[0] == (baseid+1):
                    projectileHit = False
                    damagePlayer()
            else:
                if (enemy24Coll[1] > (baseid+12+numOfEnemies)):
                    enemy24Health = enemy24Health - power
                    if enemy24Health == 0:
                        canvas.delete(map[enemyName24])
                        enemiesDefeated = enemiesDefeated + 1
                        if enemiesDefeated == numOfEnemies:
                            openSesame()
    window.after(10,enemy24Move)

def enemy25():
    global numOfEnemy2,e25y,enemyName25,enemy25Health, enemy25Val
    e25y = enemySpeed
    enemy25Health = enemyHealth
    enemyCoords()
    enemyName25 = "enemy2."+str(numOfEnemy2)
    map[enemyName25] = canvas.create_image(ex,ey,image=enemy2img)
    enemy25Val = map[enemyName25]
    enemy25Move()
def enemy25Move():
    # moves up and down, changing direction when colliding with wall
    global e25y, enemy25Health, projectileHit, enemiesDefeated
    if pauseGame == False:
        canvas.move(map[enemyName25], 0 , e25y)
    enemy25Pos = canvas.coords(map[enemyName25])
    enemy25Coll = canvas.find_overlapping(enemy25Pos[0]-25, enemy25Pos[1]-25, enemy25Pos[0]+25, enemy25Pos[1]+25)
    if pauseGame == False:

        if len(enemy25Coll) > 2:
            enemy25Health = enemy25Health - power
            if enemy25Health == 0:
                canvas.delete(map[enemyName25])
                enemiesDefeated = enemiesDefeated + 1
                if enemiesDefeated == numOfEnemies:
                    openSesame()
    
        if len(enemy25Coll) > 1:
            if enemy25Coll[0] != enemy25Val:
                if (enemy25Coll[0] > (baseid+1)) and (enemy25Coll[0] < (baseid+11)):
                    e25y = -e25y
                elif enemy25Coll[0] == (baseid+1):
                    projectileHit = False
                    damagePlayer()
            else:
                if (enemy25Coll[1] > (baseid+12+numOfEnemies)):
                    enemy25Health = enemy25Health - power
                    if enemy25Health == 0:
                        canvas.delete(map[enemyName25])
                        enemiesDefeated = enemiesDefeated + 1
                        if enemiesDefeated == numOfEnemies:
                            openSesame()
    window.after(10,enemy25Move)


def enemy31():  
    global numOfEnemy3,enemyName31,enemy31Health, enemy31Val, projectileHit
    enemy31Health = enemyHealth
    enemyCoords()
    enemyName31 = "enemy3."+str(numOfEnemy3)
    map[enemyName31] = canvas.create_image(ex,ey,image=enemy3img)
    enemy31Val = map[enemyName31]
    enemy31Move()
def enemy31Move():
    global enemy31Health, enemiesDefeated, enemy31Pos, projectileHit, j1
    #stays in one spot and spits projectiles at player
    enemy31Pos = canvas.coords(map[enemyName31])
    enemy31Coll = canvas.find_overlapping(enemy31Pos[0]-25, enemy31Pos[1]-25, enemy31Pos[0]+25, enemy31Pos[1]+25)
    if j1 % 50 == 0:
        if pauseGame == False:
            e31projectile() # Shoots projectile
    if pauseGame == False:

        if len(enemy31Coll) > 2:
            enemy31Health = enemy31Health - power
            if enemy31Health == 0:
                canvas.delete(map[enemyName31])
                enemiesDefeated = enemiesDefeated + 1
                if enemiesDefeated == numOfEnemies:
                    openSesame()

        elif len(enemy31Coll) > 1:
            if enemy31Coll[0] != enemy31Val:
                if enemy31Coll[0] == (baseid+1):
                    projectileHit = False
                    damagePlayer()
            else:
                if (enemy31Coll[1] > (baseid+12+numOfEnemies)):
                    enemy31Health = enemy31Health - power
                    if enemy31Health == 0:
                        canvas.delete(map[enemyName31])
                        enemiesDefeated = enemiesDefeated + 1
                        if enemiesDefeated == numOfEnemies:
                            openSesame()
    
    j1 = j1 + 1
    window.after(10,enemy31Move)
def e31projectile():
    global enemy31Pos, e31bullx, e31bully, e31decay, playerPos
    xdifference = (enemy31Pos[0] - playerPos[0])
    ydifference = (enemy31Pos[1] - playerPos[1])
    # calculates distance between this enemy and the player
    if (abs(xdifference) > abs(ydifference)):

        if xdifference > 0:
            e31direction = "left"
        else:
            e31direction = "right"
    else:
        if ydifference > 0:
            e31direction = "up"
        else:
            e31direction = "down"
    # shoots in the direction of the player
    if e31direction == "left":
        map["e31bullet"] = canvas.create_oval(enemy31Pos[0]-30, enemy31Pos[1]+10,enemy31Pos[0]-40,enemy31Pos[1], fill="lime")
        e31decay = 0
        e31bullx = -1
        e31bully = 0
        e31moveProjectile()
    if e31direction == "right":
        map["e31bullet"] = canvas.create_oval(enemy31Pos[0]+30, enemy31Pos[1]+10,enemy31Pos[0]+40,enemy31Pos[1], fill="lime")
        e31decay = 0
        e31bullx = 1
        e31bully = 0
        e31moveProjectile()
    if e31direction == "up":
        map["e31bullet"] = canvas.create_oval(enemy31Pos[0], enemy31Pos[1]-30,enemy31Pos[0]+10,enemy31Pos[1]-40, fill="lime")
        e31decay = 0
        e31bullx = 0
        e31bully = -1
        e31moveProjectile()
    if e31direction == "down":
        map["e31bullet"] = canvas.create_oval(enemy31Pos[0], enemy31Pos[1]+30,enemy31Pos[0]+10,enemy31Pos[1]+40, fill="lime")
        e31decay = 0
        e31bullx = 0
        e31bully = 1
        e31moveProjectile()
def e31moveProjectile():
    global e31bullx, e31bully, e31decay, projectileHit
    e31projectilePos = canvas.coords(map["e31bullet"])
    canvas.move(map["e31bullet"], bulletSpeed*e31bullx, bulletSpeed*e31bully)
    e31decay = e31decay + 1
    e31projectileColl = canvas.find_overlapping(e31projectilePos[0], e31projectilePos[1], e31projectilePos[2], e31projectilePos[3])
    # detects collision with enemies bullet
    if len(e31projectileColl) > 0:
        if e31projectileColl[0] == (baseid+1):
            projectileHit = True
            # if projectile hits player, the player is damaged with different invincibilit frames due to speed of projectile
            damagePlayer()
        elif (e31projectileColl[0] < (baseid+12)) and (e31projectileColl[0] > (baseid+1)):
            e31decay = 50
        elif len(e31projectileColl) == 2:
            if (e31projectileColl[1] < (baseid+12)) and (e31projectileColl[1] > (baseid+1)):
                e31decay = 50
    if e31decay < 50:
        window.after(10,e31moveProjectile)

def enemy32():  
    global numOfEnemy3,enemyName32,enemy32Health, enemy32Val, projectileHit
    enemy32Health = enemyHealth
    enemyCoords()
    enemyName32 = "enemy3."+str(numOfEnemy3)
    map[enemyName32] = canvas.create_image(ex,ey,image=enemy3img)
    enemy32Val = map[enemyName32]
    enemy32Move()
def enemy32Move():
    global enemy32Health, enemiesDefeated, enemy32Pos, projectileHit, j2
    #stays in one spot and spits projectiles at player
    enemy32Pos = canvas.coords(map[enemyName32])
    enemy32Coll = canvas.find_overlapping(enemy32Pos[0]-25, enemy32Pos[1]-25, enemy32Pos[0]+25, enemy32Pos[1]+25)
    if j2 % 50 == 0:
        if pauseGame == False:
            e32projectile()
    if pauseGame == False:

        if len(enemy32Coll) > 2:
            enemy32Health = enemy32Health - power
            if enemy32Health == 0:
                canvas.delete(map[enemyName32])
                enemiesDefeated = enemiesDefeated + 1
                if enemiesDefeated == numOfEnemies:
                    openSesame()

        elif len(enemy32Coll) > 1:
            if enemy32Coll[0] != enemy32Val:
                if enemy32Coll[0] == (baseid+1):
                    projectileHit = False
                    damagePlayer()
            else:
                if (enemy32Coll[1] > (baseid+12+numOfEnemies)):
                    enemy32Health = enemy32Health - power
                    if enemy32Health == 0:
                        canvas.delete(map[enemyName32])
                        enemiesDefeated = enemiesDefeated + 1
                        if enemiesDefeated == numOfEnemies:
                            openSesame()
    
    j2 = j2 + 1
    window.after(10,enemy32Move)
def e32projectile():
    global enemy32Pos, e32bullx, e32bully, e32decay, playerPos
    xdifference = (enemy32Pos[0] - playerPos[0])
    ydifference = (enemy32Pos[1] - playerPos[1])
    if (abs(xdifference) > abs(ydifference)):
        if xdifference > 0:
            e32direction = "left"
        else:
            e32direction = "right"
    else:
        if ydifference > 0:
            e32direction = "up"
        else:
            e32direction = "down"
    if e32direction == "left":
        map["e32bullet"] = canvas.create_oval(enemy32Pos[0]-30, enemy32Pos[1]+10,enemy32Pos[0]-40,enemy32Pos[1], fill="lime")
        e32decay = 0
        e32bullx = -1
        e32bully = 0
        e32moveProjectile()
    if e32direction == "right":
        map["e32bullet"] = canvas.create_oval(enemy32Pos[0]+30, enemy32Pos[1]+10,enemy32Pos[0]+40,enemy32Pos[1], fill="lime")
        e32decay = 0
        e32bullx = 1
        e32bully = 0
        e32moveProjectile()
    if e32direction == "up":
        map["e32bullet"] = canvas.create_oval(enemy32Pos[0], enemy32Pos[1]-30,enemy32Pos[0]+10,enemy32Pos[1]-40, fill="lime")
        e32decay = 0
        e32bullx = 0
        e32bully = -1
        e32moveProjectile()
    if e32direction == "down":
        map["e32bullet"] = canvas.create_oval(enemy32Pos[0], enemy32Pos[1]+30,enemy32Pos[0]+10,enemy32Pos[1]+40, fill="lime")
        e32decay = 0
        e32bullx = 0
        e32bully = 1
        e32moveProjectile()
def e32moveProjectile():
    global e32bullx, e32bully, e32decay, projectileHit
    e32projectilePos = canvas.coords(map["e32bullet"])
    canvas.move(map["e32bullet"], bulletSpeed*e32bullx, bulletSpeed*e32bully)
    e32decay = e32decay + 1
    e32projectileColl = canvas.find_overlapping(e32projectilePos[0], e32projectilePos[1], e32projectilePos[2], e32projectilePos[3])
    if len(e32projectileColl) > 0:
        if e32projectileColl[0] == (baseid+1):
            projectileHit = True
            damagePlayer()
        elif (e32projectileColl[0] < (baseid+12)) and (e32projectileColl[0] > (baseid+1)):
            e32decay = 50
        elif len(e32projectileColl) == 2:
            if (e32projectileColl[1] < (baseid+12)) and (e32projectileColl[1] > (baseid+1)):
                e32decay = 50
    if e32decay < 50:
        window.after(10,e32moveProjectile)

def enemy33():  
    global numOfEnemy3,enemyName33,enemy33Health, enemy33Val, projectileHit
    enemy33Health = enemyHealth
    enemyCoords()
    enemyName33 = "enemy3."+str(numOfEnemy3)
    map[enemyName33] = canvas.create_image(ex,ey,image=enemy3img)
    enemy33Val = map[enemyName33]
    enemy33Move()
def enemy33Move():
    global enemy33Health, enemiesDefeated, enemy33Pos, projectileHit, j3
    #stays in one spot and spits projectiles at player
    enemy33Pos = canvas.coords(map[enemyName33])
    enemy33Coll = canvas.find_overlapping(enemy33Pos[0]-25, enemy33Pos[1]-25, enemy33Pos[0]+25, enemy33Pos[1]+25)
    if j3 % 50 == 0:
        if pauseGame == False:
            e33projectile()
    if pauseGame == False:
        if len(enemy33Coll) > 2:
            enemy33Health = enemy33Health - power
            if enemy33Health == 0:
                canvas.delete(map[enemyName33])
                enemiesDefeated = enemiesDefeated + 1
                if enemiesDefeated == numOfEnemies:
                    openSesame()

        if len(enemy33Coll) > 1:
            if enemy33Coll[0] != enemy33Val:
                if enemy33Coll[0] == (baseid+1):
                    projectileHit = False
                    damagePlayer()
            else:
                if (enemy33Coll[1] > (baseid+12+numOfEnemies)):
                    enemy33Health = enemy33Health - power
                    if enemy33Health == 0:
                        canvas.delete(map[enemyName33])
                        enemiesDefeated = enemiesDefeated + 1
                        if enemiesDefeated == numOfEnemies:
                            openSesame()
        
    j3 = j3 + 1
    window.after(10,enemy33Move)
def e33projectile():
    global enemy33Pos, e33bullx, e33bully, e33decay, playerPos
    xdifference = (enemy33Pos[0] - playerPos[0])
    ydifference = (enemy33Pos[1] - playerPos[1])
    if (abs(xdifference) > abs(ydifference)):
        if xdifference > 0:
            e33direction = "left"
        else:
            e33direction = "right"
    else:
        if ydifference > 0:
            e33direction = "up"
        else:
            e33direction = "down"
    if e33direction == "left":
        map["e33bullet"] = canvas.create_oval(enemy33Pos[0]-30, enemy33Pos[1]+10,enemy33Pos[0]-40,enemy33Pos[1], fill="lime")
        e33decay = 0
        e33bullx = -1
        e33bully = 0
        e33moveProjectile()
    if e33direction == "right":
        map["e33bullet"] = canvas.create_oval(enemy33Pos[0]+30, enemy33Pos[1]+10,enemy33Pos[0]+40,enemy33Pos[1], fill="lime")
        e33decay = 0
        e33bullx = 1
        e33bully = 0
        e33moveProjectile()
    if e33direction == "up":
        map["e33bullet"] = canvas.create_oval(enemy33Pos[0], enemy33Pos[1]-30,enemy33Pos[0]+10,enemy33Pos[1]-40, fill="lime")
        e33decay = 0
        e33bullx = 0
        e33bully = -1
        e33moveProjectile()
    if e33direction == "down":
        map["e33bullet"] = canvas.create_oval(enemy33Pos[0], enemy33Pos[1]+30,enemy33Pos[0]+10,enemy33Pos[1]+40, fill="lime")
        e33decay = 0
        e33bullx = 0
        e33bully = 1
        e33moveProjectile()
def e33moveProjectile():
    global e33bullx, e33bully, e33decay, projectileHit
    e33projectilePos = canvas.coords(map["e33bullet"])
    canvas.move(map["e33bullet"], bulletSpeed*e33bullx, bulletSpeed*e33bully)
    e33decay = e33decay + 1
    e33projectileColl = canvas.find_overlapping(e33projectilePos[0], e33projectilePos[1], e33projectilePos[2], e33projectilePos[3])
    if len(e33projectileColl) > 0:
        if e33projectileColl[0] == (baseid+1):
            projectileHit = True
            damagePlayer()
        elif (e33projectileColl[0] < (baseid+12)) and (e33projectileColl[0] > (baseid+1)):
            e33decay = 50
        elif len(e33projectileColl) == 2:
            if (e33projectileColl[1] < (baseid+12)) and (e33projectileColl[1] > (baseid+1)):
                e33decay = 50
    if e33decay < 50:
        window.after(10,e33moveProjectile)

def enemy34():  
    global numOfEnemy3,enemyName34,enemy34Health, enemy34Val, projectileHit
    enemy34Health = enemyHealth
    enemyCoords()
    enemyName34 = "enemy3."+str(numOfEnemy3)
    map[enemyName34] = canvas.create_image(ex,ey,image=enemy3img)
    enemy34Val = map[enemyName34]
    enemy34Move()
def enemy34Move():
    global enemy34Health, enemiesDefeated, enemy34Pos, projectileHit, j4
    #stays in one spot and spits projectiles at player
    enemy34Pos = canvas.coords(map[enemyName34])
    enemy34Coll = canvas.find_overlapping(enemy34Pos[0]-25, enemy34Pos[1]-25, enemy34Pos[0]+25, enemy34Pos[1]+25)
    if j4 % 50 == 0:
        if pauseGame == False:
            e34projectile()
    if pauseGame == False:

        if len(enemy34Coll) > 2:
            enemy34Health = enemy34Health - power
            if enemy34Health == 0:
                canvas.delete(map[enemyName34])
                enemiesDefeated = enemiesDefeated + 1
                if enemiesDefeated == numOfEnemies:
                    openSesame()

        if len(enemy34Coll) > 1:
            if enemy34Coll[0] != enemy34Val:
                if enemy34Coll[0] == (baseid+1):
                    projectileHit = False
                    damagePlayer()
            else:
                if (enemy34Coll[1] > (baseid+12+numOfEnemies)):
                    enemy34Health = enemy34Health - power
                    if enemy34Health == 0:
                        canvas.delete(map[enemyName34])
                        enemiesDefeated = enemiesDefeated + 1
                        if enemiesDefeated == numOfEnemies:
                            openSesame()
        
    j4 = j4 + 1
    window.after(10,enemy34Move)
def e34projectile():
    global enemy34Pos, e34bullx, e34bully, e34decay, playerPos
    xdifference = (enemy34Pos[0] - playerPos[0])
    ydifference = (enemy34Pos[1] - playerPos[1])
    if (abs(xdifference) > abs(ydifference)):
        if xdifference > 0:
            e34direction = "left"
        else:
            e34direction = "right"
    else:
        if ydifference > 0:
            e34direction = "up"
        else:
            e34direction = "down"
    if e34direction == "left":
        map["e34bullet"] = canvas.create_oval(enemy34Pos[0]-30, enemy34Pos[1]+10,enemy34Pos[0]-40,enemy34Pos[1], fill="lime")
        e34decay = 0
        e34bullx = -1
        e34bully = 0
        e34moveProjectile()
    if e34direction == "right":
        map["e34bullet"] = canvas.create_oval(enemy34Pos[0]+30, enemy34Pos[1]+10,enemy34Pos[0]+40,enemy34Pos[1], fill="lime")
        e34decay = 0
        e34bullx = 1
        e34bully = 0
        e34moveProjectile()
    if e34direction == "up":
        map["e34bullet"] = canvas.create_oval(enemy34Pos[0], enemy34Pos[1]-30,enemy34Pos[0]+10,enemy34Pos[1]-40, fill="lime")
        e34decay = 0
        e34bullx = 0
        e34bully = -1
        e34moveProjectile()
    if e34direction == "down":
        map["e34bullet"] = canvas.create_oval(enemy34Pos[0], enemy34Pos[1]+30,enemy34Pos[0]+10,enemy34Pos[1]+40, fill="lime")
        e34decay = 0
        e34bullx = 0
        e34bully = 1
        e34moveProjectile()
def e34moveProjectile():
    global e34bullx, e34bully, e34decay, projectileHit
    e34projectilePos = canvas.coords(map["e34bullet"])
    canvas.move(map["e34bullet"], bulletSpeed*e34bullx, bulletSpeed*e34bully)
    e34decay = e34decay + 1
    e34projectileColl = canvas.find_overlapping(e34projectilePos[0], e34projectilePos[1], e34projectilePos[2], e34projectilePos[3])
    if len(e34projectileColl) > 0:
        if e34projectileColl[0] == (baseid+1):
            print("hit")
            projectileHit = True
            damagePlayer()
        elif (e34projectileColl[0] < (baseid+12)) and (e34projectileColl[0] > (baseid+1)):
            e34decay = 50
        elif len(e34projectileColl) == 2:
            if (e34projectileColl[1] < (baseid+12)) and (e34projectileColl[1] > (baseid+1)):
                e34decay = 50
    if e34decay < 50:
        window.after(10,e34moveProjectile)

def enemy35():  
    global numOfEnemy3,enemyName35,enemy35Health, enemy35Val, projectileHit
    enemy35Health = enemyHealth
    enemyCoords()
    enemyName35 = "enemy3."+str(numOfEnemy3)
    map[enemyName35] = canvas.create_image(ex,ey,image=enemy3img)
    enemy35Val = map[enemyName35]
    enemy35Move()
def enemy35Move():
    global enemy35Health, enemiesDefeated, enemy35Pos, projectileHit, j5
    #stays in one spot and spits projectiles at player
    enemy35Pos = canvas.coords(map[enemyName35])
    enemy35Coll = canvas.find_overlapping(enemy35Pos[0]-25, enemy35Pos[1]-25, enemy35Pos[0]+25, enemy35Pos[1]+25)
    if j5 % 50 == 0:
        if pauseGame == False:
            e35projectile()
    if pauseGame == False:

        if len(enemy35Coll) > 2:
            enemy35Health = enemy35Health - power
            if enemy35Health == 0:
                canvas.delete(map[enemyName35])
                enemiesDefeated = enemiesDefeated + 1
                if enemiesDefeated == numOfEnemies:
                    openSesame()

        if len(enemy35Coll) > 1:
            if enemy35Coll[0] != enemy35Val:
                if enemy35Coll[0] == (baseid+1):
                    projectileHit = False
                    damagePlayer()
            else:
                if (enemy35Coll[1] > (baseid+12+numOfEnemies)):
                    enemy35Health = enemy35Health - power
                    if enemy35Health == 0:
                        canvas.delete(map[enemyName35])
                        enemiesDefeated = enemiesDefeated + 1
                        if enemiesDefeated == numOfEnemies:
                            openSesame()
    j5 = j5 + 1
    window.after(10,enemy35Move)
def e35projectile():
    global enemy35Pos, e35bullx, e35bully, e35decay, playerPos
    xdifference = (enemy35Pos[0] - playerPos[0])
    ydifference = (enemy35Pos[1] - playerPos[1])
    if (abs(xdifference) > abs(ydifference)):
        if xdifference > 0:
            e35direction = "left"
        else:
            e35direction = "right"
    else:
        if ydifference > 0:
            e35direction = "up"
        else:
            e35direction = "down"
    if e35direction == "left":
        map["e35bullet"] = canvas.create_oval(enemy35Pos[0]-30, enemy35Pos[1]+10,enemy35Pos[0]-40,enemy35Pos[1], fill="lime")
        e35decay = 0
        e35bullx = -1
        e35bully = 0
        e35moveProjectile()
    if e35direction == "right":
        map["e35bullet"] = canvas.create_oval(enemy35Pos[0]+30, enemy35Pos[1]+10,enemy35Pos[0]+40,enemy35Pos[1], fill="lime")
        e35decay = 0
        e35bullx = 1
        e35bully = 0
        e35moveProjectile()
    if e35direction == "up":
        map["e35bullet"] = canvas.create_oval(enemy35Pos[0], enemy35Pos[1]-30,enemy35Pos[0]+10,enemy35Pos[1]-40, fill="lime")
        e35decay = 0
        e35bullx = 0
        e35bully = -1
        e35moveProjectile()
    if e35direction == "down":
        map["e35bullet"] = canvas.create_oval(enemy35Pos[0], enemy35Pos[1]+30,enemy35Pos[0]+10,enemy35Pos[1]+40, fill="lime")
        e35decay = 0
        e35bullx = 0
        e35bully = 1
        e35moveProjectile()
def e35moveProjectile():
    global e35bullx, e35bully, e35decay, projectileHit
    e35projectilePos = canvas.coords(map["e35bullet"])
    canvas.move(map["e35bullet"], bulletSpeed*e35bullx, bulletSpeed*e35bully)
    e35decay = e35decay + 1
    e35projectileColl = canvas.find_overlapping(e35projectilePos[0], e35projectilePos[1], e35projectilePos[2], e35projectilePos[3])
    if len(e35projectileColl) > 0:
        if e35projectileColl[0] == (baseid+1):
            projectileHit = True
            damagePlayer()
        elif (e35projectileColl[0] < (baseid+12)) and (e35projectileColl[0] > (baseid+1)):
            e35decay = 50
        elif len(e35projectileColl) == 2:
            if (e35projectileColl[1] < (baseid+12)) and (e35projectileColl[1] > (baseid+1)):
                e35decay = 50
    if e35decay < 50:
        window.after(10,e35moveProjectile)

    

def enemy41():
    global numOfEnemy4,e41x,e41y,enemyName41,enemy41Health, enemy41Val, e41changeDir
    e41changeDir = 100
    e41x = -enemySpeed
    e41y = 0
    enemy41Health = enemyHealth
    enemyCoords()
    enemyName41 = "enemy4."+str(numOfEnemy4)
    map[enemyName41] = canvas.create_image(ex,ey,image=enemy4img)
    enemy41Move()
def enemy41Move():
    # moves left and right, changing direction at random points, and moving in the opposite direction when colliding with wall
    global e41x, e41y, enemy41Health, projectileHit, e41changeDir, enemiesDefeated
    e41changeDir = e41changeDir -1 #decrement variable
    if e41changeDir == 0:
        e41changeDir = 100
        enemy41dir = random.randint(1,4)
        # choose random direction to move in every time the variable e41changeDir reaches zero
        if enemy41dir == 1:
            e41x = enemySpeed
            e41y = 0
        elif enemy41dir == 2:
            e41x = -enemySpeed
            e41y = 0
        elif enemy41dir == 3:
            e41x = 0
            e41y = enemySpeed
        else:
            e41x = 0
            e41y = -enemySpeed
    if pauseGame == False:
        canvas.move(map[enemyName41], e41x , e41y) #move enemy
    enemy41Pos = canvas.coords(map[enemyName41])
    enemy41Coll = canvas.find_overlapping(enemy41Pos[0]-25, enemy41Pos[1]-25, enemy41Pos[0]+25, enemy41Pos[1]+25)
    if pauseGame == False:

        if len(enemy41Coll) > 2:
            enemy41Health = enemy41Health - power
            if enemy41Health == 0:
                canvas.delete(map[enemyName41])
                enemiesDefeated = enemiesDefeated + 1
                if enemiesDefeated == numOfEnemies:
                    openSesame()

        if len(enemy41Coll) > 1:
            if enemy41Coll[0] != map[enemyName41]:
                if (enemy41Coll[0] > (baseid+1)) and (enemy41Coll[0] < (baseid+11)):
                    if abs(e41x) > abs(e41y):
                        e41x = -e41x
                    else:
                        e41y = -e41y
                elif enemy41Coll[0] == (baseid+1):
                    projectileHit = False
                    damagePlayer()
            if enemy41Coll[0] == map[enemyName41]:
                if (enemy41Coll[1] > (baseid+12+numOfEnemies)):
                    enemy41Health = enemy41Health - power
                    if enemy41Health == 0:
                        canvas.delete(map[enemyName41])
                        enemiesDefeated = enemiesDefeated + 1
                        if enemiesDefeated == numOfEnemies:
                            openSesame()
    window.after(10,enemy41Move)

def enemy42():
    global numOfEnemy4,e42x,e42y,enemyName42,enemy42Health, enemy42Val, e42changeDir
    e42changeDir = 100
    e42x = -enemySpeed
    e42y = 0
    enemy42Health = enemyHealth
    enemyCoords()
    enemyName42 = "enemy4."+str(numOfEnemy4)
    map[enemyName42] = canvas.create_image(ex,ey,image=enemy4img)
    enemy42Move()
def enemy42Move():
    # moves left and right, changing direction when colliding with wall
    global e42x, e42y, enemy42Health, projectileHit, e42changeDir, enemiesDefeated
    e42changeDir = e42changeDir -1
    if e42changeDir == 0:
        e42changeDir = 100
        enemy42dir = random.randint(1,4)
        if enemy42dir == 1:
            e42x = enemySpeed
            e42y = 0
        elif enemy42dir == 2:
            e42x = -enemySpeed
            e42y = 0
        elif enemy42dir == 3:
            e42x = 0
            e42y = enemySpeed
        else:
            e42x = 0
            e42y = -enemySpeed
    canvas.move(map[enemyName42], e42x , e42y)
    if pauseGame == False:
        enemy42Pos = canvas.coords(map[enemyName42])
    enemy42Coll = canvas.find_overlapping(enemy42Pos[0]-25, enemy42Pos[1]-25, enemy42Pos[0]+25, enemy42Pos[1]+25)
    if pauseGame == False:
        if len(enemy42Coll) > 2:
            enemy42Health = enemy42Health - power
            if enemy42Health == 0:
                canvas.delete(map[enemyName42])
                enemiesDefeated = enemiesDefeated + 1
                if enemiesDefeated == numOfEnemies:
                    openSesame()

        if len(enemy42Coll) > 1:
            if enemy42Coll[0] != (map[enemyName42]):
                if (enemy42Coll[0] > (baseid+1)) and (enemy42Coll[0] < (baseid+11)):
                    if abs(e42x) > abs(e42y):
                        e42x = -e42x
                    else:
                        e42y = -e42y
                elif enemy42Coll[0] == (baseid+1):
                    projectileHit = False
                    damagePlayer()
            elif enemy42Coll[0] == (map[enemyName42]):
                if (enemy42Coll[1] > (baseid+12+numOfEnemies)):
                    enemy42Health = enemy42Health - power
                    if enemy42Health == 0:
                        canvas.delete(map[enemyName42])
                        enemiesDefeated = enemiesDefeated + 1
                        if enemiesDefeated == numOfEnemies:
                            openSesame()
    window.after(10,enemy42Move)

def enemy43():
    global numOfEnemy4,e43x,e43y,enemyName43,enemy43Health, enemy43Val, e43changeDir
    e43changeDir = 100
    e43x = -enemySpeed
    e43y = 0
    enemy43Health = enemyHealth
    enemyCoords()
    enemyName43 = "enemy4."+str(numOfEnemy4)
    map[enemyName43] = canvas.create_image(ex,ey,image=enemy4img)
    enemy43Move()
def enemy43Move():
    # moves left and right, changing direction when colliding with wall
    global e43x, e43y, enemy43Health, projectileHit, e43changeDir, enemiesDefeated
    e43changeDir = e43changeDir -1
    if e43changeDir == 0:
        e43changeDir = 100
        enemy43dir = random.randint(1,4)
        if enemy43dir == 1:
            e43x = enemySpeed
            e43y = 0
        elif enemy43dir == 2:
            e43x = -enemySpeed
            e43y = 0
        elif enemy43dir == 3:
            e43x = 0
            e43y = enemySpeed
        else:
            e43x = 0
            e43y = -enemySpeed
    canvas.move(map[enemyName43], e43x , e43y)
    if pauseGame == False:
        enemy43Pos = canvas.coords(map[enemyName43])
    enemy43Coll = canvas.find_overlapping(enemy43Pos[0]-25, enemy43Pos[1]-25, enemy43Pos[0]+25, enemy43Pos[1]+25)
    if pauseGame == False:

        if len(enemy43Coll) > 2:
            enemy43Health = enemy43Health - power
            if enemy43Health == 0:
                canvas.delete(map[enemyName43])
                enemiesDefeated = enemiesDefeated + 1
                if enemiesDefeated == numOfEnemies:
                    openSesame()

        if len(enemy43Coll) > 1:
            if enemy43Coll[0] != map[enemyName43]:
                if (enemy43Coll[0] > (baseid+1)) and (enemy43Coll[0] < (baseid+11)):
                    if abs(e43x) > abs(e43y):
                        e43x = -e43x
                    else:
                        e43y = -e43y
                elif enemy43Coll[0] == (baseid+1):
                    projectileHit = False
                    damagePlayer()
            if enemy43Coll[0] == map[enemyName43]:
                if (enemy43Coll[1] > (baseid+12+numOfEnemies)):
                    enemy43Health = enemy43Health - power
                    if enemy43Health == 0:
                        canvas.delete(map[enemyName43])
                        enemiesDefeated = enemiesDefeated + 1
                        if enemiesDefeated == numOfEnemies:
                            openSesame()
    window.after(10,enemy43Move)

def enemy44():
    global numOfEnemy4,e44x,e44y,enemyName44,enemy44Health, enemy44Val, e44changeDir
    e44changeDir = 100
    e44x = -enemySpeed
    e44y = 0
    enemy44Health = enemyHealth
    enemyCoords()
    enemyName44 = "enemy4."+str(numOfEnemy4)
    map[enemyName44] = canvas.create_image(ex,ey,image=enemy4img)
    enemy44Move()
def enemy44Move():
    # moves left and right, changing direction when colliding with wall
    global e44x, e44y, enemy44Health, projectileHit, e44changeDir, enemiesDefeated
    e44changeDir = e44changeDir -1
    if e44changeDir == 0:
        e44changeDir = 100
        enemy44dir = random.randint(1,4)
        if enemy44dir == 1:
            e44x = enemySpeed
            e44y = 0
        elif enemy44dir == 2:
            e44x = -enemySpeed
            e44y = 0
        elif enemy44dir == 3:
            e44x = 0
            e44y = enemySpeed
        else:
            e44x = 0
            e44y = -enemySpeed
    canvas.move(map[enemyName44], e44x , e44y)
    if pauseGame == False:
        enemy44Pos = canvas.coords(map[enemyName44])
    enemy44Coll = canvas.find_overlapping(enemy44Pos[0]-25, enemy44Pos[1]-25, enemy44Pos[0]+25, enemy44Pos[1]+25)
    if pauseGame == False:

        if len(enemy44Coll) > 2:
            enemy44Health = enemy44Health - power
            if enemy44Health == 0:
                canvas.delete(map[enemyName44])
                enemiesDefeated = enemiesDefeated + 1
                if enemiesDefeated == numOfEnemies:
                    openSesame()

        if len(enemy44Coll) > 1:
            if enemy44Coll[0] != map[enemyName44]:
                if (enemy44Coll[0] > (baseid+1)) and (enemy44Coll[0] < (baseid+11)):
                    if abs(e44x) > abs(e44y):
                        e44x = -e44x
                    else:
                        e44y = -e44y
                elif enemy44Coll[0] == (baseid+1):
                    projectileHit = False
                    damagePlayer()
            if enemy44Coll[0] != map[enemyName44]:
                if (enemy44Coll[1] > (baseid+12+numOfEnemies)):
                    enemy44Health = enemy44Health - power
                    if enemy44Health == 0:
                        canvas.delete(map[enemyName44])
                        enemiesDefeated = enemiesDefeated + 1
                        if enemiesDefeated == numOfEnemies:
                            openSesame()
    window.after(10,enemy44Move)

def enemy45():
    global numOfEnemy4,e45x,e45y,enemyName45,enemy45Health, enemy45Val, e45changeDir, enemiesDefeated
    e45changeDir = 100
    e45x = -enemySpeed
    e45y = 0
    enemy45Health = enemyHealth
    enemyCoords()
    enemyName45 = "enemy4."+str(numOfEnemy4)
    map[enemyName45] = canvas.create_image(ex,ey,image=enemy4img)
    enemy45Move()
def enemy45Move():
    # moves left and right, changing direction when colliding with wall
    global e45x, e45y, enemy45Health, projectileHit, e45changeDir
    e45changeDir = e45changeDir -1
    if e45changeDir == 0:
        e45changeDir = 100
        enemy45dir = random.randint(1,4)
        if enemy45dir == 1:
            e45x = enemySpeed
            e45y = 0
        elif enemy45dir == 2:
            e45x = -enemySpeed
            e45y = 0
        elif enemy45dir == 3:
            e45x = 0
            e45y = enemySpeed
        else:
            e45x = 0
            e45y = -enemySpeed
    if pauseGame == False:
        canvas.move(map[enemyName45], e45x , e45y)
    enemy45Pos = canvas.coords(map[enemyName45])
    enemy45Coll = canvas.find_overlapping(enemy45Pos[0]-25, enemy45Pos[1]-25, enemy45Pos[0]+25, enemy45Pos[1]+25)
    if pauseGame == False:

        if len(enemy45Coll) > 2:
            enemy45Health = enemy45Health - power
            if enemy45Health == 0:
                canvas.delete(map[enemyName45])
                enemiesDefeated = enemiesDefeated + 1
                if enemiesDefeated == numOfEnemies:
                    openSesame()

        if len(enemy45Coll) > 1:
            if enemy45Coll[0] != map[enemyName45]:
                if (enemy45Coll[0] > (baseid+1)) and (enemy45Coll[0] < (baseid+11)):
                    if abs(e45x) > abs(e45y):
                        e45x = -e45x
                    else:
                        e45y = -e45y
                elif enemy45Coll[0] == (baseid+1):
                    projectileHit = False
                    damagePlayer()
            if enemy45Coll[0] == map[enemyName45]:
                if (enemy45Coll[1] > (baseid+12+numOfEnemies)):
                    enemy45Health = enemy45Health - power
                    if enemy45Health == 0:
                        canvas.delete(map[enemyName45])
                        enemiesDefeated = enemiesDefeated + 1
                        if enemiesDefeated == numOfEnemies:
                            openSesame()
    window.after(10,enemy45Move)


def enemy51():  
    global numOfEnemy5,e51x,e51y,enemyName51,enemy51Health, e51changeDir
    e51changeDir = 100
    e51x = 0
    e51y = 0
    enemy51Health = enemyHealth
    enemyCoords()
    enemyName51 = "enemy5."+str(numOfEnemy5)
    map[enemyName51] = canvas.create_image(ex,ey,image=enemy5img)
    enemy51Move()
def enemy51Move():
    # follows player, moving through walls
    global e51x,e51y, enemy51Health, projectileHit, enemiesDefeated, enemySpeed
    if pauseGame == False:
        canvas.move(map[enemyName51], e51x , e51y)
    enemy51Pos = canvas.coords(map[enemyName51])
    enemy51Coll = canvas.find_overlapping(enemy51Pos[0]-25, enemy51Pos[1]-25, enemy51Pos[0]+25, enemy51Pos[1]+25)
    xdifference = (enemy51Pos[0] - playerPos[0])
    ydifference = (enemy51Pos[1] - playerPos[1])
    # calculates difference between this enemy and the player and changes its direction accordingly to move towards the player
    if (abs(xdifference) > abs(ydifference)):
        if xdifference > 0:
            e51x = (-0.7 * enemySpeed)
            e51y = 0
        else:
            e51x = 0.7 * enemySpeed
            e51y = 0
    else:
        if ydifference > 0:
            e51x = 0
            e51y = (-0.7 * enemySpeed)
        else:
            e51x = 0
            e51y = 0.7 * enemySpeed
    if pauseGame == False:

        if len(enemy51Coll) > 2:
            if enemy51Health == 0:
                canvas.delete(map[enemyName51])
                enemiesDefeated = enemiesDefeated + 1
                if enemiesDefeated == numOfEnemies:
                    openSesame()

        # no collision here for walls since this enemy moves through them
        elif len(enemy51Coll) > 1:
            if enemy51Coll[0] != map[enemyName51]:
                if enemy51Coll[0] == (baseid+1):
                    projectileHit = False
                    damagePlayer()
            if enemy51Coll[0] == map[enemyName51]:
                if (enemy51Coll[1] > (baseid+12+numOfEnemies)):
                    enemy51Health = enemy51Health - power
                    if enemy51Health == 0:
                        canvas.delete(map[enemyName51])
                        enemiesDefeated = enemiesDefeated + 1
                        if enemiesDefeated == numOfEnemies:
                            openSesame()
    window.after(10,enemy51Move)

def enemy52():  
    global numOfEnemy5,e52x,e52y,enemyName52,enemy52Health, enemy52Val, e52changeDir
    e52changeDir = 100
    e52x = 0
    e52y = 0
    enemy52Health = enemyHealth
    enemyCoords()
    enemyName52 = "enemy5."+str(numOfEnemy5)
    map[enemyName52] = canvas.create_image(ex,ey,image=enemy5img)
    enemy52Move()
def enemy52Move():
    global e52x,e52y, enemy52Health, projectileHit, enemiesDefeated, enemySpeed
    if pauseGame == False:
        canvas.move(map[enemyName52], e52x , e52y)
    enemy52Pos = canvas.coords(map[enemyName52])
    enemy52Coll = canvas.find_overlapping(enemy52Pos[0]-25, enemy52Pos[1]-25, enemy52Pos[0]+25, enemy52Pos[1]+25)
    xdifference = (enemy52Pos[0] - playerPos[0])
    ydifference = (enemy52Pos[1] - playerPos[1])
    if (abs(xdifference) > abs(ydifference)):
        if xdifference > 0:
            e52x = -0.7 * enemySpeed
            e52y = 0
        else:
            e52x = 0.7 * enemySpeed
            e52y = 0
    else:
        if ydifference > 0:
            e52x = 0
            e52y = -0.7 * enemySpeed
        else:
            e52x = 0
            e52y = 0.7 * enemySpeed
    if pauseGame == False:

        if len(enemy52Coll) > 2:
            enemy52Health = enemy52Health - power
            if enemy52Health == 0:
                canvas.delete(map[enemyName52])
                enemiesDefeated = enemiesDefeated + 1
                if enemiesDefeated == numOfEnemies:
                    openSesame()

        elif len(enemy52Coll) > 1:
            if enemy52Coll[0] != map[enemyName52]:
                if enemy52Coll[0] == (baseid+1):
                    projectileHit = False
                    damagePlayer()
            if enemy52Coll[0] == map[enemyName52]:
                if (enemy52Coll[1] > (baseid+12+numOfEnemies)):
                    enemy52Health = enemy52Health - power
                    if enemy52Health == 0:
                        canvas.delete(map[enemyName52])
                        enemiesDefeated = enemiesDefeated + 1
                        if enemiesDefeated == numOfEnemies:
                            openSesame()
        

    window.after(10,enemy52Move)

def enemy53():  
    global numOfEnemy5,e53x,e53y,enemyName53,enemy53Health, enemy53Val, e53changeDir
    e53changeDir = 100
    e53x = 0
    e53y = 0
    enemy53Health = enemyHealth
    enemyCoords()
    enemyName53 = "enemy5."+str(numOfEnemy5)
    map[enemyName53] = canvas.create_image(ex,ey,image=enemy5img)
    enemy53Move()
def enemy53Move():
    global e53x,e53y, enemy53Health, projectileHit, enemiesDefeated, enemySpeed
    if pauseGame == False:
        canvas.move(map[enemyName53], e53x , e53y)
    enemy53Pos = canvas.coords(map[enemyName53])
    enemy53Coll = canvas.find_overlapping(enemy53Pos[0]-25, enemy53Pos[1]-25, enemy53Pos[0]+25, enemy53Pos[1]+25)
    xdifference = (enemy53Pos[0] - playerPos[0])
    ydifference = (enemy53Pos[1] - playerPos[1])
    if (abs(xdifference) > abs(ydifference)):
        if xdifference > 0:
            e53x = -0.7 * enemySpeed
            e53y = 0
        else:
            e53x = 0.7 * enemySpeed
            e53y = 0
    else:
        if ydifference > 0:
            e53x = 0
            e53y = -0.7 * enemySpeed
        else:
            e53x = 0
            e53y = 0.7 * enemySpeed
    if pauseGame == False:

        if len(enemy53Coll) > 2:
            enemy53Health = enemy53Health - power
            if enemy53Health == 0:
                canvas.delete(map[enemyName53])
                enemiesDefeated = enemiesDefeated + 1
                if enemiesDefeated == numOfEnemies:
                    openSesame()

        elif len(enemy53Coll) > 1:
            if enemy53Coll[0] != map[enemyName53]:
                if enemy53Coll[0] == (baseid+1):
                    projectileHit = False
                    damagePlayer()
            if enemy53Coll[0] == map[enemyName53]:
                if (enemy53Coll[1] > (baseid+12+numOfEnemies)):
                    enemy53Health = enemy53Health - power
                    if enemy53Health == 0:
                        canvas.delete(map[enemyName53])
                        enemiesDefeated = enemiesDefeated + 1
                        if enemiesDefeated == numOfEnemies:
                            openSesame()
            if len(enemy53Coll) > 2:
                for i in range(0, (len(enemy53Coll)-1)):
                    if (enemy53Coll[i] > (baseid+12+numOfEnemies)):
                        enemy53Health = enemy53Health - power
                        if enemy53Health == 0:
                            canvas.delete(map[enemyName53])
                            enemiesDefeated = enemiesDefeated + 1
                            if enemiesDefeated == numOfEnemies:
                                openSesame()

    window.after(10,enemy53Move)

def enemy54():  
    global numOfEnemy5,e54x,e54y,enemyName54,enemy54Health, enemy54Val, e54changeDir
    e54changeDir = 100
    e54x = 0
    e54y = 0
    enemy54Health = enemyHealth
    enemyCoords()
    enemyName54 = "enemy5."+str(numOfEnemy5)
    map[enemyName54] = canvas.create_image(ex,ey,image=enemy5img)
    enemy54Move()
def enemy54Move():
    global e54x,e54y, enemy54Health, projectileHit, enemiesDefeated, enemySpeed
    if pauseGame == False:
        canvas.move(map[enemyName54], e54x , e54y)
    enemy54Pos = canvas.coords(map[enemyName54])
    enemy54Coll = canvas.find_overlapping(enemy54Pos[0]-25, enemy54Pos[1]-25, enemy54Pos[0]+25, enemy54Pos[1]+25)
    xdifference = (enemy54Pos[0] - playerPos[0])
    ydifference = (enemy54Pos[1] - playerPos[1])
    if (abs(xdifference) > abs(ydifference)):
        if xdifference > 0:
            e54x = -0.7 * enemySpeed
            e54y = 0
        else:
            e54x = 0.7 * enemySpeed
            e54y = 0
    else:
        if ydifference > 0:
            e54x = 0
            e54y = -0.7 * enemySpeed
        else:
            e54x = 0
            e54y = 0.7 * enemySpeed
    if pauseGame == False:

        if len(enemy54Coll) > 2:
            enemy54Health = enemy54Health - power
            if enemy54Health == 0:
                canvas.delete(map[enemyName54])
                enemiesDefeated = enemiesDefeated + 1
                if enemiesDefeated == numOfEnemies:
                    openSesame()
        if len(enemy54Coll) > 1:
            if enemy54Coll[0] != map[enemyName54]:
                if enemy54Coll[0] == (baseid+1):
                    projectileHit = False
                    damagePlayer()
            if enemy54Coll[0] == map[enemyName54]:
                if (enemy54Coll[1] > (baseid+12+numOfEnemies)):
                    enemy54Health = enemy54Health - power
                    if enemy54Health == 0:
                        canvas.delete(map[enemyName54])
                        enemiesDefeated = enemiesDefeated + 1
                        if enemiesDefeated == numOfEnemies:
                            openSesame()
        if len(enemy54Coll) > 2:
            for i in range(0, (len(enemy54Coll)-1)):
                if (enemy54Coll[i] > (baseid+12+numOfEnemies)):
                    enemy54Health = enemy54Health - power
                    if enemy54Health == 0:
                        canvas.delete(map[enemyName54])
                        enemiesDefeated = enemiesDefeated + 1
                        if enemiesDefeated == numOfEnemies:
                            openSesame()

    window.after(10,enemy54Move)

def enemy55():  
    global numOfEnemy5,e55x,e55y,enemyName55,enemy55Health, enemy55Val, e55changeDir
    e55changeDir = 100
    e55x = 0
    e55y = 0
    enemy55Health = enemyHealth
    enemyCoords()
    enemyName55 = "enemy5."+str(numOfEnemy5)
    map[enemyName55] = canvas.create_image(ex,ey,image=enemy5img)
    enemy55Move()
def enemy55Move():
    global e55x,e55y, enemy55Health, projectileHit, enemiesDefeated, enemySpeed
    if pauseGame == False:
        canvas.move(map[enemyName55], e55x , e55y)
    enemy55Pos = canvas.coords(map[enemyName55])
    enemy55Coll = canvas.find_overlapping(enemy55Pos[0]-25, enemy55Pos[1]-25, enemy55Pos[0]+25, enemy55Pos[1]+25)
    xdifference = (enemy55Pos[0] - playerPos[0])
    ydifference = (enemy55Pos[1] - playerPos[1])
    if (abs(xdifference) > abs(ydifference)):
        if xdifference > 0:
            e55x = -0.7 * enemySpeed
            e55y = 0
        else:
            e55x = 0.7 * enemySpeed
            e55y = 0
    else:
        if ydifference > 0:
            e55x = 0
            e55y = -0.7 * enemySpeed
        else:
            e55x = 0
            e55y = 0.7 * enemySpeed
    if pauseGame == False:

        if len(enemy55Coll) > 2:
            enemy55Health = enemy55Health - power
            if enemy55Health == 0:
                canvas.delete(map[enemyName55])
                enemiesDefeated = enemiesDefeated + 1
                if enemiesDefeated == numOfEnemies:
                    openSesame()
        if len(enemy55Coll) > 1:
            if enemy55Coll[0] != map[enemyName55]:
                if enemy55Coll[0] == (baseid+1):
                    projectileHit = False
                    damagePlayer()
            if enemy55Coll[0] == map[enemyName55]:
                if (enemy55Coll[1] > (baseid+12+numOfEnemies)):
                    enemy55Health = enemy55Health - power
                    if enemy55Health == 0:
                        canvas.delete(map[enemyName55])
                        enemiesDefeated = enemiesDefeated + 1
                        if enemiesDefeated == numOfEnemies:
                            openSesame()
        if len(enemy55Coll) > 2:
            for i in range(0, (len(enemy55Coll)-1)):
                if (enemy55Coll[i] > (baseid+12+numOfEnemies)):
                    enemy55Health = enemy55Health - power
                    if enemy55Health == 0:
                        canvas.delete(map[enemyName55])
                        enemiesDefeated = enemiesDefeated + 1
                        if enemiesDefeated == numOfEnemies:
                            openSesame()

    window.after(10,enemy55Move)

def damagePlayer():
    global health, invincibleFrames, projectileHit, window, healthDisplay
    # invincible frames provides a cool down for the player when he is hit so it is fair
    if invincibleFrames == 10 and projectileHit == True:
        health = health - enemyDamage # takes damage
        healthDisplay.destroy()
        healthDisplay = Label(window, text=("Health: "+str(health)), bg = "purple", fg = "crimson", font=("Helvetica", 18),width = 20)
        healthDisplay.place(x = 100, y = 3)
        # updates the text that displays the health

    if invincibleFrames <20:
        invincibleFrames = invincibleFrames + 1
    else:
        health = health - enemyDamage
        healthDisplay.destroy()
        healthDisplay = Label(window, text=("Health: "+str(health)), bg = "purple", fg = "crimson", font=("Helvetica", 18),width=20)
        healthDisplay.place(x = 100, y = 3)
        invincibleFrames = 0
    if health <= 0:
        leaderBoard() #opens leaderboard

def leaderBoard():
    global window, name, lettersEntered, level
    leaderBoardPanel = canvas.create_rectangle((width/2-400,height/2-300),(width/2 + 400,height/2 + 300), fill="grey")
    scores = open("CWK2/leaderBoard.txt")
    i = 1
    boardItems = {}
    # reads data in leaderBoard.txt and displays it on various labels on a leader board display
    for line in scores:
        boardText = str(line).strip()
        boardItem = "boardScore"+str(i)  
        print(boardText)
        boardItems[boardItem] = Label(canvas, text = boardText, bg = "black", fg = "white", font=("Helvetica", 50), width = 12, height = 1)
        i = i + 1
        if i == 11: 
            break
    scores.close()

    # place all the leaderboard name and score displays
    boardItems["boardScore1"].place(x=325, y=125)
    boardItems["boardScore2"].place(x=700, y=125)
    boardItems["boardScore3"].place(x=325, y=200)
    boardItems["boardScore4"].place(x=700, y=200)
    boardItems["boardScore5"].place(x=325, y=275)
    boardItems["boardScore6"].place(x=700, y=275)
    boardItems["boardScore7"].place(x=325, y=350)
    boardItems["boardScore8"].place(x=700, y=350)
    boardItems["boardScore9"].place(x=325, y=425)
    boardItems["boardScore10"].place(x=700, y=425)

    lettersEntered = 0
    name = ""

    def details(event):
        # detects when a key is pressed and takes the players name to save their score
        global lettersEntered, name
        print(lettersEntered)
        if lettersEntered <3: #name limited to 3 letters
            if event.char == " " or event.char == "":
                lettersEntered = lettersEntered - 1
            else:
                name = name+event.char
                name = name.upper()
        if lettersEntered == 2:
            # once name is entered, creates dictionary of entries in leaderBoard.txt
            scores = open("CWK2/leaderBoard.txt")
            i = 1
            boardScores = {}
            for line in scores:
                boardItem = str(line).strip()
                if i % 2 != 0:
                    boardName =  boardItem
                else:
                    boardItem = int(boardItem)
                    boardScores.update({boardName : boardItem})
                i = i + 1
            keys = []
            for key in boardScores.keys():
                keys.append(key)
            if name in keys:
                # checks to see if name has been used before, if it has then the entry with the higher score is kept while the other is discarded
                for key in boardScores.keys():
                    if name == key and level < boardScores[key]:
                        scores.close()
                            
                    elif name == key and level > boardScores[key]:
                        scores.close()
                        scores = open("CWK2/leaderBoard.txt","a")
                        scores.write("\n"+str(name))
                        scores.write("\n"+str(level))
                        scores.close()
            else:
                scores.close()
                scores = open("CWK2/leaderBoard.txt","a")
                scores.write("\n"+str(name))
                scores.write("\n"+str(level))
                scores.close()
            scores = open("CWK2/leaderBoard.txt")
            i = 1
            # This following code sorts the entries so that the player with the highest score is at the top
            boardScores = {}
            for line in scores:
                # creates dictionary again this time with the latest entry {name : score}
                boardItem = str(line).strip()
                if i % 2 != 0:
                    boardName =  boardItem
                else:
                    boardItem = int(boardItem)
                    boardScores.update({boardName : boardItem})
                i = i + 1
            orderedScores = sorted(boardScores.values()) # list of the scores in ascending order
            scores.close()
            scores = open("CWK2/leaderBoard.txt","w") #clear the file
            scores.close()
            scores = open("CWK2/leaderBoard.txt","a") 
            keys = []
            for key in boardScores.keys():
                keys.append(key)
            i = len(orderedScores) - 1
            while i > -1:
                found = False
                for key in boardScores.keys():
                    if boardScores[key] == orderedScores[i] and found == False and key in keys:
                        # only appends if the score matches the entries score, if the entry hasn't already been found and if the key hasn't been used already
                        scores.write(key+"\n")
                        if i == 0:
                            scores.write(str(boardScores[key])) #makes sure the last entry doesn't end in a new line
                        else:
                            scores.write(str(boardScores[key])+"\n")
                        found = True
                        keys.remove(key) #removes key from list of possible keys

                i = i-1

        lettersEntered = lettersEntered+1 #increments the letters entered to detect when name has been typed
        print(name)
    
    
    window.bind("<Key>", details) #detects key press for details
    replayButton = tkinter.Button(canvas, text = "REPLAY", font=("Helvetica", 50),height=2, width=11, command = lambda : replayGame()) # button that restarts game
    replayButton.place(x=325,y=525)
    replayButton = tkinter.Button(canvas, text = "QUIT", font=("Helvetica", 50),height=2, width=11, command = lambda : quitGame()) # button that quits game
    replayButton.place(x=700,y=525)
    def replayGame():
        global level, name, lettersEntered, window
        scores = open("CWK2/leaderBoard.txt","a")
        if lettersEntered > 2:
            # as long as the name has been typed, the window is destroyed and created again, reinitialising the game
            scores.write("\n"+str(name))
            scores.write("\n"+str(level))
            window.destroy()
            window = tkinter.Tk()
            init()
            window.mainloop()

        scores.close()
    def quitGame():
        # as long as the name has been typed, the window is destroyed
        global level, name, lettersEntered, window
        if lettersEntered > 2:
            window.destroy()    



def bossKey():
    global pauseGame, bossOpen, bossKeyScreen, levelDisplay, healthDisplay
    pauseGame = True #also pauses game
    if bossOpen == True:
        # displays image of lecture when "[" is pressed
        bossKeyScreen = canvas.create_image(width/2,height/2,image=lecture)
        levelDisplay.destroy()
        healthDisplay.destroy()
        # must delete and replace health and level display since they are in front

    else:
        global level, health
        canvas.delete(bossKeyScreen)
        levelDisplay = Label(window, text=("Floor: "+str(level)), bg = "purple", fg = "crimson", font=("Helvetica", 18))
        levelDisplay.place(x = 30, y = 3)
        healthDisplay = Label(window, text=("Health: "+str(health)), bg = "purple", fg = "crimson", font=("Helvetica", 18), width=20)
        healthDisplay.place(x = 100, y = 3)
        pauseGame = False

def pause():
    global pausePanel, resumeButton, saveButton, loadButton, settingsButton, canvas, pauseGame
    pauseGame = True #pauses game
    pausePanel = canvas.create_rectangle((width/2-400,height/2-300),(width/2 + 400,height/2 + 300), fill="grey")
    resumeButton = Button(canvas, text = "X", highlightbackground = "red", font = ("Helvetica", 30), height = 1, width = 1, command = lambda : resume()) #button resumes game
    resumeButton.place(x=325,y=100)
    saveButton = tkinter.Button(canvas, text = "SAVE & QUIT", font=("Helvetica", 50),height=2, width=24, command = lambda : save()) #button saves game
    saveButton.place(x=325,y=150)
    loadButton = tkinter.Button(canvas, text = "LOAD FROM SAVE", font=("Helvetica", 50),height=2, width=24, command = lambda : load()) # button loads game from save
    loadButton.place(x=325,y=325)
    settingsButton = tkinter.Button(canvas, text = "SETTINGS", font=("Helvetica", 50),height=2, width=24, command = lambda : settingsMenu()) # button opens up a new settings panel
    settingsButton.place(x=325,y=500)
    def resume():
        global pausePanel, resumeButton, saveButton, loadButton, settingsButton, canvas, pauseGame
        canvas.delete(pausePanel)
        resumeButton.destroy()
        saveButton.destroy()
        loadButton.destroy()
        settingsButton.destroy()
        #destroys pause menu to see the game
        pauseGame = False #unpauses game
def save():
    global level, health
    levelData = open("CWK2/levelData.txt", "w")
    #checks wether player is saving in middle of the round, so their saved level is 1 less
    # the level the player is on is written to a file
    if enemiesDefeated == numOfEnemies:
        levelData.write(str(level))
    elif level != 0:
        levelData.write(str(level-1))
    else:
        levelData.write("0")
    
    levelData.close()
    healthData = open("CWK2/healthData.txt", "w") #players health is written to another file
    healthData.write(str(health))
    window.destroy() # game is quit
def load():
    global window, loadSave
    loadSave = True
    window.destroy()
    # initialises game as usual but with the boolean loadSave as True, trigger loading of certain variables
    window = tkinter.Tk()
    init()
    window.mainloop()

def settingsMenu():
    global settingsPanel, resumeButton2, upButton, breakBindUp, breakBindDown, breakBindLeft, breakBindRight
    canvas.delete(pausePanel)
    resumeButton.destroy()
    saveButton.destroy()
    loadButton.destroy()
    settingsButton.destroy()
    settingsPanel = canvas.create_rectangle((width/2-400,height/2-300),(width/2 + 400,height/2 + 300), fill="grey")
    resumeButton2 = Button(canvas, text = "X", highlightbackground = "red", font = ("Helvetica", 30), height = 1, width = 1, command = lambda : resume()) #resumes game
    resumeButton2.place(x=325,y=100)
    # creates series of buttons representing the four directions the player can move so that they can change the keys used for moving
    breakBindUp = False
    upButton = tkinter.Button(canvas, text = "UP", font=("Helvetica", 50),height=2, width=6, command = lambda : upKeyBind())
    upButton.place(x=575,y=150)

    breakBindDown = False
    downButton = tkinter.Button(canvas, text = "DOWN", font=("Helvetica", 50),height=2, width=6, command = lambda : downKeyBind())
    downButton.place(x=575,y=300)

    breakBindLeft = False
    leftButton = tkinter.Button(canvas, text = "LEFT", font=("Helvetica", 50),height=2, width=6, command = lambda : leftKeyBind())
    leftButton.place(x=350,y=300)

    breakBindRight = False
    rightButton = tkinter.Button(canvas, text = "RIGHT", font=("Helvetica", 50),height=2, width=6, command = lambda : rightKeyBind())
    rightButton.place(x=800,y=300)
    # creates a series of buttons of different colour so the player can change the colour of their player
    redButton = tkinter.Button(canvas, highlightbackground = "red",height=6, width=8, command = lambda : setColourRed())
    redButton.place(x=350,y=500)

    blueButton = tkinter.Button(canvas, highlightbackground = "steel blue",height=6, width=8, command = lambda : setColourBlue())
    blueButton.place(x=460,y=500)

    cyanButton = tkinter.Button(canvas, highlightbackground = "cyan",height=6, width=8, command = lambda : setColourCyan())
    cyanButton.place(x=570,y=500)

    greenButton = tkinter.Button(canvas, highlightbackground = "green",height=6, width=8, command = lambda : setColourGreen())
    greenButton.place(x=680,y=500)

    pinkButton = tkinter.Button(canvas, highlightbackground = "magenta",height=6, width=8, command = lambda : setColourPink())
    pinkButton.place(x=790,y=500)

    yellowButton = tkinter.Button(canvas, highlightbackground = "gold",height=6, width=8, command = lambda : setColourYellow())
    yellowButton.place(x=900,y=500)


    def resume():
        global settingsPanel, resumeButton2, pauseGame, leftKey, rightKey, upKey, downKey, playerColour
        # deletes and destroys all items in the settings panel to see the game
        canvas.delete(settingsPanel)
        resumeButton2.destroy()
        upButton.destroy()
        downButton.destroy()
        leftButton.destroy()
        rightButton.destroy()
        redButton.destroy()
        blueButton.destroy()
        cyanButton.destroy()
        greenButton.destroy()
        pinkButton.destroy()
        yellowButton.destroy()
        canvas.itemconfig(map["player"],fill=playerColour) #changes players colour
        settings = open("CWK2/settings.txt", "w")
        lines = [leftKey, rightKey, upKey, downKey, playerColour]
        for i in range(len(lines)):
            # writes the values of these new settings to the file so that these changes are saved
            settings.write(lines[i])
            settings.write("\n")


        pauseGame = False #unpauses game

def upKeyBind():
    global upKey, breakBindUp
    def keyBind(event):
        global breakBindUp, upKey
        # only allows this one letter to be pressed for the key bind, will not accept p or ] since these are already in use
        if breakBindUp == False and event.char != "p" and event.char != "]":
            upKey = event.char
            breakBindUp = True
    if breakBindUp == True:
        window.bind("<Key>", keyPressed) #once the key is pressed revert key presses to trigger the keyPressed function
    else:
        window.bind("<Key>", keyBind)
        window.after(10, upKeyBind)

def downKeyBind():
    global downKey, breakBindDown
    def keyBind(event):
        global breakBindDown, downKey
        if breakBindDown == False and event.char != "p" and event.char != "]":
            downKey = event.char
            breakBindDown = True
    if breakBindDown == True:
        window.bind("<Key>", keyPressed)
    else:
        window.bind("<Key>", keyBind)
        window.after(10, downKeyBind)

def leftKeyBind():
    global leftKey, breakBindLeft
    def keyBind(event):
        global breakBindLeft, leftKey
        if breakBindLeft == False and event.char != "p" and event.char != "]":
            leftKey = event.char
            breakBindLeft = True
    if breakBindLeft == True:
        window.bind("<Key>", keyPressed)
    else:
        window.bind("<Key>", keyBind)
        window.after(10, leftKeyBind)

def rightKeyBind():
    global rightKey, breakBindRight
    def keyBind(event):
        global breakBindRight, rightKey
        if breakBindRight == False and event.char != "p" and event.char != "]":
            rightKey = event.char
            breakBindRight = True
    if breakBindRight == True:
        window.bind("<Key>", keyPressed)
    else:
        window.bind("<Key>", keyBind)
        window.after(10, rightKeyBind)

def setColourRed():
    global playerColour, map
    playerColour = "red" #simply creates a global variable set to a colour recognised by the tkinter syntax

def setColourBlue():
    global playerColour
    playerColour = "steel blue"

def setColourCyan():
    global playerColour
    playerColour = "cyan"

def setColourGreen():
    global playerColour
    playerColour = "green"

def setColourPink():
    global playerColour
    playerColour = "magenta"

def setColourYellow():
    global playerColour
    playerColour = "Gold"


#creates window
window = tkinter.Tk()
#if game is started from the main code then no loading is performed
loadSave = False

def init():
    global window, canvas, width, height, health, invincibleFrames, enemiesDefeated, enemyHealth, enemySpeed, enemyDamage, direction, replay, level, numOfEnemies, player_size, left, right, up, down, x, y, m, decay, j1, j2, j3, j4, j5, playerPos, bulletSpeed, coords, press, doorimg, enemy1img, enemy2img, enemy3img, enemy4img, enemy5img, map, idcoords, baseid, power, pauseGame, loadSave, leftKey, rightKey, upKey, downKey, playerColour, lecture, bossOpen, levelDisplay, healthDisplay, health
    # Initialises the code, with all its variables and functions
    pauseGame = False
    bossOpen = False
    # if the game is being loaded from a save
    if loadSave == True:
        loadLevel = open("CWK2/levelData.txt")
        level = int(loadLevel.readline())
        # the value of level is taken from the save file and the difficulty of the enemies are adjusted accordingly
        for i in range(level):
            if i % 2 == 0:
                enemyHealth = enemyHealth +1
            enemySpeed = enemySpeed * 1.05
            enemyDamageFl = enemyDamage * 1.1
            enemyDamage = int(enemyDamageFl)
        loadLevel.close()
        loadHealth = open("CWK2/healthData.txt") #the value of the players health is taken from the save file
        health = int(loadHealth.readline())
        loadHealth.close()
        loadSave = False
    else:
        #otherwise these initial values are used
        level = 0
        enemyHealth = 1
        enemySpeed = 2
        enemyDamage = 10
        health = 100
    width = 1366 #standard resolution
    height = 768
    invincibleFrames = 0
    enemiesDefeated = 0
    direction = "none"
    replay = False
    numOfEnemies = 0
    player_size = 30
    left, right, up, down = -5, 5, -5, 5
    # reads the data from the settings files and binds the keys accordingly, aswell as setting the player colour
    settings = open("CWK2/settings.txt")
    lineNum = 0
    lines = settings.readlines()
    for line in lines:
        if lineNum == 0:
            leftKey = line.strip()
        elif lineNum == 1:
            rightKey = line.strip()
        elif lineNum == 2:
            upKey = line.strip()
        elif lineNum == 3:
            downKey = line.strip()
        elif lineNum == 4:
            playerColour = line.strip()
        lineNum = lineNum + 1
    x = 0
    y = 0
    m = 0
    power = 1
    decay = 0
    j1 = 0
    j2 = 0
    j3 = 0
    j4 = 0
    j5 = 0
    playerPos= [0,0,0,0]
    bulletSpeed = 5
    coords = [0,0,0,0]
    press = False
    set_window_dimensions(width, height)
    canvas = tkinter.Canvas(window,bg="black",width=width, height=height,)
    # creates canvas that acts as the root for the movement of the game

    # These are the images used throughout the game, taken from open source sprite sites mainly

    lecture = tkinter.PhotoImage(file="CWK2/lectureScreen.gif")
    # taken from a blackboard lecture, given by Stewart Blakely

    doorimg = tkinter.PhotoImage(file="CWK2/door.gif")
    #https://opengameart.org/content/animated-bamboo-door-sprite

    enemy1img = tkinter.PhotoImage(file="CWK2/enemy1.gif")
    #https://itch.io/game-assets/free/tag-slime

    enemy2img = tkinter.PhotoImage(file="CWK2/enemy2.gif")
    #https://itch.io/game-assets/free/tag-slime

    enemy3img = tkinter.PhotoImage(file="CWK2/enemy3.gif")
    #https://www.realmeye.com/forum/t/new-enemy-sprite/2230/9
    
    enemy4img = tkinter.PhotoImage(file="CWK2/enemy4.gif")
    #https://jose-moyano.itch.io/evil-tree-pixel-art

    enemy5img = tkinter.PhotoImage(file="CWK2/enemy5.gif")
    #https://itch.io/game-assets/tag-ghosts

    map = {}
    # allows objects to be easily referenced
    map["baseID"] = canvas.create_rectangle((0,0),(0,0), fill="steel blue")
    idcoords = canvas.coords(map["baseID"])
    baseid = canvas.find_overlapping(idcoords[0], idcoords[1], idcoords[2], idcoords[3])
    baseid = baseid[0]
    # determines base id for reference
    map["player"] = canvas.create_rectangle((width/2,height/2),(width/2 + player_size,height/2 + player_size), fill=playerColour)
    # creates player
    room1() #begins with first room instantiation, no enemies
    openSesame() #spawns the first door, this is how the player begins the game
    window.bind("<Key>", keyPressed) #binds keys to move player
    window.bind("<KeyRelease>", keyReleased)
    levelDisplay = Label(window, text=("Floor: "+str(level)), bg = "purple", fg = "crimson", font=("Helvetica", 18)) #creates display to show player the level they are on
    levelDisplay.place(x = 30, y = 3)
    healthDisplay = Label(window, text=("Health: "+str(health)), bg = "purple", fg = "crimson", font=("Helvetica", 18), width=20) #creates display to show player their health
    healthDisplay.place(x = 100, y = 3)
    canvas.pack()
    # place objects

    move()
    # allows player to move, this happens as the mainloop is open
init() # triggers the initialisation of the game
window.mainloop()
