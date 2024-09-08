from turtle import *
width(7)

#drawing house

#drawing square

speed(20)
color("purple")
forward (200) 
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end

#drawing door

forward(70)
color ("yellow")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
color("brown")
penup()
goto(120,60)
pendown()
forward(1)

#end drawing a door

#drawing a traengle

penup()
goto(200,200)
pendown()
begin_fill()
color("red")
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#end drawing 

#drawing windows

penup()
goto(0,0)
pendown()
penup()
goto(60,120)
pendown()
right(60)
color("brown")
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)

penup()
goto(140,120)
pendown()
forward(1)
left(90)
forward(50)

left(90)
forward(50)

left(90)
forward(50)

left(90)
forward(50)

color("purple")
penup()
goto(0,0)
pendown()




exitonclick()


