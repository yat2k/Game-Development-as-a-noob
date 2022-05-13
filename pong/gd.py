import turtle
import os
import winsound

#Create the window
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800,height=900)
wn.tracer(0) #animation speed

#Paddle A
paddleA=turtle.Turtle()   
paddleA.speed(0)         #higher the value within the paranthesis, lower will be the speed
paddleA.shape("square")  #by default the dimesnion is 20px
paddleA.color("white")
paddleA.shapesize(stretch_wid=5,stretch_len=1)
paddleA.penup() #to remove the trace of the path
paddleA.goto(-350,0)

#Paddle B
paddleB=turtle.Turtle()   
paddleB.speed(0)         #higher the value within the paranthesis, lower will be the speed
paddleB.shape("square")  #by default the dimesnion is 20px
paddleB.color("white")
paddleB.shapesize(stretch_wid=5,stretch_len=1)
paddleB.penup() #to remove the trace of the path
paddleB.goto(350,0)

#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)

ball.dx=0.15
ball.dy=0.15

#Scores
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.goto(0,260)
pen.write("Player A:0 Player B:0", align="center",font=("Courier",24,"normal"))

#Functions

def paddleAUp():
    y=paddleA.ycor()
    y=y+20
    paddleA.sety(y)

def paddleADown():
    y=paddleA.ycor()
    y=y-20
    paddleA.sety(y)


def paddleBUp():
    y=paddleB.ycor()
    y=y+20
    paddleB.sety(y)

def paddleBDown():
    y=paddleB.ycor()
    y=y-20
    paddleB.sety(y)
 
scoreA=0
scoreB=0

#Keyboard binding 

wn.listen()
wn.onkeypress(paddleAUp,"w")
wn.onkeypress(paddleADown,"s")
wn.onkeypress(paddleBUp,"Up")
wn.onkeypress(paddleBDown,"Down")



while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    
    #Border Checking
    if ball.ycor()>290:
        ball.sety(290)
        winsound.PlaySound("ballBounce.wav",winsound.SND_ASYNC)
        ball.dy=ball.dy*-1
    if ball.ycor()<-290:
        ball.sety(-290)
        winsound.PlaySound("ballBounce.wav",winsound.SND_ASYNC)
        ball.dy=ball.dy*-1
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx=ball.dx*-1
        scoreA +=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scoreA,scoreB),  align="center",font=("Courier",24,"normal"))
    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx=ball.dx*-1
        scoreB +=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scoreA,scoreB),  align="center",font=("Courier",24,"normal"))

    
    #collide with the padddles

    if ball.xcor()>340 and (ball.ycor()<paddleB.ycor()+50 and ball.ycor()>paddleB.ycor()-50):
        ball.dx=ball.dx*-1
    if ball.xcor()<-340 and (ball.ycor()<paddleA.ycor()+50 and ball.ycor()>paddleA.ycor()-50):
        ball.dx=ball.dx*-1

    

    
