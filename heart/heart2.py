import turtle

t = turtle.Turtle()

# Configurações da caneta
t.pensize(3)
t.speed(1)

# Desenha o coração
t.color('#660000')
t.begin_fill()
t.left(45)
t.forward(100)
t.circle(50, 180)
t.right(90)
t.circle(50, 180)
t.forward(100)
t.end_fill()

# Esconde a caneta
t.hideturtle()

turtle.done()