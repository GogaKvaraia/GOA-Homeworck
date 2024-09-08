from turtle import*


#______________________________________________________________

#drawing casle

#__________________________________________________________________

#drawing sky and land

#____________________________________________________________________












#___________________________________________________________________
# drawing rectangle

speed (30)

color ("gray")
begin_fill()
width(5)
forward(100)
right (90)
forward(300)
penup()
goto(0,0)
pendown()
forward(300)
left(90)
forward(100)
end_fill()

#end drawing rectangle
#____________________________________________________________________________


goto(100,-100)

#__________________________________________________________________________________

#drawing 2 rectangle

begin_fill()
forward(100)
right(90)
forward(200)
right(90)
forward(100)
left(90)
end_fill()
#end drawing 2 rectangle

#_______________________________________________________________________________

penup()
goto(0,-100)
pendown()

#_______________________________________________________________________________

#drawing 3 rectangle

begin_fill()
right(90)
forward(100)
left(90)
forward(200)
left(90)
forward(100)
end_fill()
#end drawing 3 rectangle

#___________________________________________________________________________________

penup()
goto(0,0)
pendown()

#______________________________________________________________________________________

#giveing the form of a casle

color("dark gray")
forward(100)
right(90)
forward(300)
right(90)
forward(100)
right(90)
forward(300)

penup()
goto(0,-100)
pendown()

left(90)
forward(100)
left(90)
forward(200)
left(90)
forward(100)
left(90)
forward(200)

penup()
goto(100,-100)
pendown()

right(90)
forward(100)
right(90)
forward(200)
right(90)
forward(100)

#end drawing casle form

#_________________________________________________________________________________

penup()
goto(50,5)
pendown()

#______________________________________________________________________________________

#drawing triangle

color ("red")
begin_fill()
right (90)
forward(100)
right(140)
forward(140)
left (230)
forward(90)


penup()
goto(50,5)
pendown()


right(90)
forward(100)
left(140)
forward(140)
right(230)
forward(100)

end_fill()

penup()
goto(53,5)
pendown()

width(7)
right(90)
forward (3)

width(5)

#______________________________________________________________________________________



# drawing casle form


#drawing squares


color("gray")

penup()
goto(-5,-100)
pendown()


begin_fill()
left(180)
forward(30)
left(90)
forward(20)
left(90)
forward(30)
left (90)
forward(20)
end_fill()

begin_fill()
left(180)
forward(36)
right(90)
forward(30)
left(90)
forward(20)
left(90)
forward(30)
left(90)
forward(20)
end_fill()


begin_fill()
left(180)
forward(36)
right(90)
forward(30)
left(90)
forward(20)
left(90)
forward(30)
left(90)
forward(20)
end_fill()

color("dark gray")
goto(0,-100)

left(180)
forward(100)
right(90)
forward(30)
right(90)
forward(23)
right(90)
forward(30)

left(90)
forward(36)
left(90)
forward(30)
left(90)
forward(20)
left(90)
forward(30)

left(90)
forward (56)
left(90)
forward(30)
left(90)
forward(20)
left(90)
forward(30)



penup()
goto(105,-100)
pendown()

color("gray")

begin_fill()
left(180)
forward(30)
right(90)
forward(20)
right(90)
forward(30)
right(90)
forward(20)
end_fill()


begin_fill()
right(180)
forward(36)
left(90)
forward(30)
right(90)
forward(20)
right(90)
forward(30)
right(90)
forward(20)
end_fill()


begin_fill()
right(180)
forward(36)
left(90)
forward(30)
right(90)
forward(20)
right(90)
forward(30)
right(90)
forward(20)
left(180)
forward(20)

end_fill()




color("dark gray")

left(180)
forward(95)
right(90)
forward(30)
right(90)
forward(23)
right(90)
forward(30)

left(90)
forward(36)
left(90)
forward(30)
left(90)
forward(20)
left(90)
forward(30)

left(90)
forward (56)
left(90)
forward(30)
left(90)
forward(20)
left(90)
forward(30)

#end drawing squares

#_______________________________________________________________

#drawing windows for casle

penup()
goto(50,-40)
pendown()

color ("black")
width(15)

forward(40)


penup()
goto(50,-130)
pendown()

forward(40)

penup()
goto(50,-220)
pendown()

forward(40)


penup()
goto(-50,-130)
pendown()

forward(40)

penup()
goto(-50,-230)
pendown()

forward(40)




penup()
goto(150,-130)
pendown()

forward(40)

penup()
goto(150,-230)
pendown()
forward(40)
#end drawing windows

#_____________________________________________________________________


#drawing goa flag



width(5)
penup()
goto(50,103)
pendown()

left(180)
color("light gray")
forward(100)

color("black")
begin_fill()

right(90)
forward(100)
left(90)
forward(50)
left(90)
forward(100)
left(90)
forward(50)

end_fill()

goto(100,230)

color ("dark green")

left(90)
forward(15)
right(90)
forward(20)
right(90)
forward(35)
right(90)
forward(37)
right(90)
forward(35)


penup()
goto(1000,1000)






exitonclick()



#end drawing goa flag
#end drawing casle


#_____________________________________________________________________________