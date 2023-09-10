import turtle
screen= turtle.Screen()
screen.bgcolor("white")

heart= turtle.Turtle()
heart.shape("turtle")
heart.color("red")
heart.fillcolor("red")
heart.speed(1)

heart.begin_fill()
heart.left(140)
heart.forward(224)
for _ in range(200):
    heart.right(1)
    heart.forward(2)
heart.left(120)
for _ in range (200):
    heart.right(1)
    heart.forward(2)
heart.forward(224)
heart.end_fill()

heart.hideturtle()
screen.exitonclick()
