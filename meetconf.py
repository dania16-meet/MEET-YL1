import turtle
x,y=turtle.position()
turtle.goto(x,y)	
turtle.pendown()
turtle.pencolor("red")
turtle.onscreenclick(turtle.goto,btn=1,add=True)
turtle.shape("circle")
def change():
	turtle.pencolor("yellow")
	
def clear():
	turtle.clear()
	
def change1():
	turtle.pencolor("green")
	

def shakel():
	turtle.shape("triangle")
	turtle.getscreen().onkeypress(shakel, "t")
	turtle.getscreen().listen()
x=0
y=0
def draw_square(x,y):
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()
	turtle.goto(x+50,y)
	turtle.goto(x+50,y+50)
	turtle.goto(x,y+50)
	turtle.goto(x,y)
	turtle.getscreen().onkeypress(draw_square, "s")
	turtle.getscreen().listen()

draw_square(0,0)
turtle.onscreenclick(draw_square,btn=1,add=True)


turtle.getscreen().onkeypress(change, "Up")
turtle.getscreen().listen()
turtle.getscreen().onkeypress(clear, "c")
turtle.getscreen().listen()
turtle.getscreen().onkeypress(change1, "Down")
turtle.getscreen().listen()
turtle.getscreen().onkeypress(shakel, "t")
turtle.getscreen().listen()

turtle.mainloop()

