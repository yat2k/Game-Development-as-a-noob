import turtle
import os
import math
import random


#initialize the screen
wn = turtle.Screen()
wn.bgpic("space_invaders_background.gif")
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")
#background colour
wn.bgcolor('black')

#title
wn.title('space invaders')

#draw border
borderPen = turtle.Turtle()

#speed should be fast
borderPen.speed(0)

#colour
borderPen.color('white')

#we dont want to draw anything
borderPen.penup()

borderPen.setposition(-300,-300)

#now we want to draw
borderPen.pendown()

#size of the pen
borderPen.pensize(3)        #width of the square

#loop to draw square
for size in range(4):
	borderPen.fd(600)       #fd - forward
	borderPen.lt(90)		#lt - left

#now to hide the turtkle
borderPen.hideturtle()

#creating player
player = turtle.Turtle()
player.color('blue')
player.shape('player.gif')
player.penup()                #we dont want our player(turtle) to draw anythings as it moves
player.speed(0)
player.setposition(0,-250)    #keeping it at coordinates(0,-250)
player.setheading(90)         #rotate the triangle by 90 degrees towards the left

playerspeed = 15

#creating enemies
#create multiple enemies
numberOfEnemies = 5
#add enemies to the list
enemies = []
#add enemies to the list
for i in range(numberOfEnemies):
	#create a new enemy
	enemies.append(turtle.Turtle())
for enemy in enemies:
	enemy.color('red')
	enemy.shape('invader.gif')
	enemy.penup()
	enemy.speed(0)
	x = random.randint(-200,200)
	y = random.randint(100,150)
	enemy.setposition(x,y)

enemyspeed = 2

#create bullets
bullet = turtle.Turtle()
bullet.color('yellow')
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed = 20

bulletstate = 'ready'

#functions
def moveLeft():
	x = player.xcor()
	x -= playerspeed
	if x<-280:
		x = -280
	player.setx(x)

def moveRight():
	x = player.xcor()
	x += playerspeed
	if x>280:
		x = 280
	player.setx(x)

def fireBullet():
	global bulletstate
	if bulletstate == 'ready':
		bulletstate = 'fired'

		#move bullet upwards from where it is fired
		x = player.xcor()
		y = player.ycor()
		bullet.setposition(x,y)
		bullet.showturtle()

def iscollision(t1,t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 15:
		return True
	else:
		return False


#keyboard bindings
turtle.listen()
turtle.onkey(fireBullet,'space')
turtle.onkeypress(moveLeft,'Left')      #here we have used another function
turtle.onkeypress(moveRight,'Right')

while True:
	for enemy in enemies:

		#moving the enemy
		x=enemy.xcor()
		x+=enemyspeed
		enemy.setx(x)

		#moving the enemy down and change direction
		if enemy.xcor() > 280:
			y=enemy.ycor()
			y-=30
			enemyspeed *= -1
			enemy.sety(y)
		if enemy.xcor() < -280:
			y=enemy.ycor()
			y-=30
			enemyspeed *= -1
			enemy.sety(y)

		

		#detect collisions b/w bullet and enemies
		if iscollision(bullet,enemy):
			#reseting the bullet
			bullet.hideturtle()
			bulletstate = 'ready'
			bullet.setposition(0,-400)

			#resetting the enemy
			enemy.setposition(-200,250)

		if iscollision(player,enemy):
			player.hideturtle()
			print('Game over')
			break

	#moving bullet upwards
	if bulletstate == 'fired':
		y = bullet.ycor()
		y+=bulletspeed
		bullet.sety(y)

	#if bullet reaches top
	if bullet.ycor()>275:
		bullet.hideturtle()
		bulletstate = 'ready'