# ЗАДАНИЕ 6: Алгоритмы с циклами
# Важно: шаги, условия, границы цикла
# turtle: forward(), right(), left(), up(), down()

from turtle import*
tracer(0)
k = 20
left(90)

for i in range(3):
    forward (27 * k)
    right(90)
    forward (12 * k)
    right(90)
up()
forward(4 * k)
right(90)
forward(6 * k)
left(90)
down ()
for i in range(4):
    forward(83 * k)
    right(90)
    forward(77 * k)
    right(90)
up()
for x in range(-50, 50):
    for y in range (-50, 50):
        goto(x * k, y * k)
        dot(3, 'black')

exitonclick()