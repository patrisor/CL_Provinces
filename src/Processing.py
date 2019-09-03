import Auxiliary
import Getch
import random
import Menu

# Quits our game if input is 'q'
def die(i):
    if i == "q":
        print("Goodbye!")
        exit(-1)

# Update User Skill Tree
def itemPickUp(p, c, r):
    if Auxiliary.isCollided(c, 1, r): # GOLD
        p.gold += random.randint(5, 15)
    if Auxiliary.isCollided(c, 2, r): #SWORD
        p.attributes['Strength'] += 15

# Takes in a valid-input parameter, and a valid data type you want to comapre it to
# Returns array of these found parameters
def isValid(inp, inputs):
    ret = ''
    for x in inputs:
        if x == inp: ret += str(x)
    return(ret)

# Basic processing of input to see if input is valid
# Checks if key passed was valid to aid with collision
def processInput(p, m, i, e, SCREEN_W = 30, SCREEN_H = 22):
    collisions = Auxiliary.getCollisions(p, m, i)
    while True:
        ret = Getch.getch()
        if ret == "p": Menu.openMenu(p, SCREEN_W, SCREEN_H)
        # NOTE: DO NOT DELETE -> Collision detected if length of keys is greater than 0
        if Auxiliary.isCollided(collisions, 0, ret): continue
        # Update User Skill Tree
        itemPickUp(p, collisions, ret)
        # Collision between enemies
        # TODO: Make it so you lose health when right next to enemy and not colliding into enemy
        if Auxiliary.isCollided(collisions, 3, ret): 
            p.attributes["Health"] -= e[0].attack
            continue
        return ret
