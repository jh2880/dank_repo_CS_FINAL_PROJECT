import os
import random
path = os.getcwd()

###################################################################################################################################################################################################
#IMAGES

#kirito images
kiritoImages = []
for file in os.listdir(path+"/images/Kirito/single"):
	kiritoImages.append(file)
kiritoImages.sort()

#tatsuya images

#asuna images

#enemy images

###################################################################################################################################################################################################
#MOVING OBJECTS

#create class Entity; all moving objects will stem from this
#attributes: (self, x, y, radius, width, height, ground, image, frame)
    #def update(self):
    #def display(self):
    
#create class Player, derived from class Entity
#attributes: (self, hp = 100, atk = 50, mp = 0, xp = 0
    #def gravity(self):
    #def dealDamage(self, enemy):
        #enemy.hp = enemy.hp - self.atk #Subtract atk from health of enemy
    
#create class Boss, derived from class Player

#create class Enemy, derived from class Entity

#create class Projectile, derived from class Entity; this is the projectile throw by player

#create class KnockBackBlast, derived from class Entity; this is knockback effect for both player and boss

#

###################################################################################################################################################################################################
#STAGES

#create class Stage; all stages will stem from this (uses player (will need to be constant throughout game; g.kirito),enemies,etc)

#create class StageOne

#create class StageTwo

#create class StageThree

###################################################################################################################################################################################################
#GAME

#create class Game (self,g,h,w,kirito = Player(arg))

#def update(self):
    #this whole area will take care of all stages and levels in them. self.stageCount will determine the stage (background and enemies)
    #and self.levelCount will determine the level (level 3, enter boss room)
    
    #if player's health reaches 0, self.playerDeath == True
    
#def gameOver(self):
    #display "You Died" in red. display restart menu
    #if restart is clicked:
        #g.gameReset == True

#def gameComplete(self):
    #

###################################################################################################################################################################################################
#SETUP AND DRAW

#g = Game()

#def setup():
    #code for main menu and UI
    #start game
#def draw():
    #if g.gameEnd == False:
        #g.update()
        #g.display()
    #if playerDeath == True:
        #g.gameOver()
    #if g.gameEnd == True:
        #g.gameComplete()
        
###################################################################################################################################################################################################
#KEYBOARD CONTROL AND RESET

#if basic attack pressed == True:
    #kirito.mp += 10 #builds up magic points

#if g.gameReset == True:
    #g = Game()
