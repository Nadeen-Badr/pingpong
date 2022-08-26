import turtle
wind=turtle.Screen()
wind.title("Ping-Pong")
wind.bgcolor("black")
wind.setup(width=800,height=600)
wind.tracer(0)

var1 = turtle.Turtle()
var1.speed(0)
var1.shape("square")
var1.color("blue")
var1.penup()
var1.shapesize(stretch_wid=5,stretch_len=1)
var1.goto(-350,0)

var2 = turtle.Turtle()
var2.speed(0)
var2.shape("square")
var2.color("red")
var2.penup()
var2.shapesize(stretch_wid=5,stretch_len=1)
var2.goto(350,0)

var3 = turtle.Turtle()
var3.speed(0)
var3.shape("circle")
var3.color("white")
var3.penup()
var3.goto(0,0)
var3.dx=0.3
var3.dy=0.3


score1=0
score2=0
score=turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score,turtle.hideturtle()
score.goto(0,260)
score.write("Player1: 0  Player2: 0 ", align="center", font=("Courier",24,"normal"))
#functions
def var1_up():
    y=var1.ycor()
    y+=20
    var1.sety(y)
def var1_down():
    y=var1.ycor()
    y-=20
    var1.sety(y)
def var2_up():
    y=var2.ycor()
    y+=20
    var2.sety(y)
def var2_down():
    y=var2.ycor()
    y-=20
    var2.sety(y)
       
#keyboard bind
wind.listen()
wind.onkeypress(var1_up,"w")
wind.onkeypress(var1_down,"s")
wind.onkeypress(var2_up,"Up")
wind.onkeypress(var2_down,"Down")

while True:
    wind.update()
    var3.setx(var3.xcor()+var3.dx)
    var3.sety(var3.ycor()+var3.dy)
    #border check
    if var3.ycor()>290:
        var3.sety(290)
        var3.dy *=-1
    if var3.ycor()<-290:
        var3.sety(-290)
        var3.dy *=-1
    if var3.xcor()>390:
        var3.goto(0,0)
        var3.dx *=-1
        score1+=1
        score.clear()
        score.write("Player1: {} Player2: {} ".format(score1,score2), align="center", font=("Courier",24,"normal"))
    if var3.xcor()<-390:
        var3.goto(0,0)
        var3.dx *=-1
        score2+=1
        score.clear()
        score.write("Player1: {} Player2: {} ".format(score1,score2), align="center", font=("Courier",24,"normal"))
    if(var3.xcor()>340 and var3.xcor()<350) and (var3.ycor()<var2.ycor() +40 and var3.ycor()>var2.ycor()-40):
        var3.setx(340)
        var3.dx *=-1
    if(var3.xcor()<-340 and var3.xcor()>-350) and (var3.ycor()<var1.ycor() +40 and var3.ycor()>var1.ycor()-40):
        var3.setx(-340)
        var3.dx *=-1
    
    
        
        
