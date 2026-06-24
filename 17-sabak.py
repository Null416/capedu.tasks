from turtle import*


#1 Zadanie

color('purple')
begin_fill()
for i in range(3):
    pensize(5)
    forward(100)
    left(120)
end_fill()

#2 Zadanie

penup()
goto(-200,0)
pendown()

color('orange')
begin_fill()
for i in range(5):
    forward(100)
    left(72)
end_fill()

#3 Zadanie
#Желтый круг (Лицо)
color('yellow')
penup()
goto(0,-300)
pendown()
begin_fill()
circle(100)
end_fill()

#Белая глазница 1 
color('white')
penup()
goto(-30,-180)
pendown()
begin_fill()
circle(20)
end_fill()


#Глазница 2
penup()
forward(70)
pendown()
begin_fill()
circle(20)
end_fill()

#Губы
color('black')
penup()
goto(20,-270)
pendown()
circle(10,180)
right(180)
circle(10,180)

#Зрачок глаза 1 
penup()
goto(-25,-150)
pendown()
begin_fill()
circle(10)
end_fill()


#Зрачок глаза 2
penup()
forward(-70)
pendown()
begin_fill()
circle(10)
end_fill()


#просто убрать кисть с рисунка
color('white')
penup()
goto(500,500)
pendown()

exitonclick()