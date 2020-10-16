import turtle

gr = turtle.Screen( )
gr.bgcolor("black")
gr.title("Turtle Demo")

player = turtle.Turtle( )
player.color("gold")
player.shape("triangle")
player.penup( )
player.speed(0)
player.setposition(0, -250)
player.setheading(90)
player.pendown( )

playerspeed = 10


def move_left( ):
    x = player.xcor( )
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right( ):
    x = player.xcor( )
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

def move_up( ):
    y = player.ycor( )
    y += playerspeed
    if y > 300:
        y = 300
    player.sety(y)

def move_down( ):
    y = player.ycor( )
    y -= playerspeed
    if y < -300:
        y = -300
    player.sety(y)

turtle.listen( )
turtle.onkey(move_left, "a")
turtle.onkey(move_right,"d")
turtle.onkey(move_up,"w")
turtle.onkey(move_down,"s")


turtle.mainloop( )
