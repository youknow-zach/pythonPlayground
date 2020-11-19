import turtle as tu

wn = tu.Screen()

# new turtle
rabbit = tu.Turtle()
rabbit.shape('turtle')
rabbit.color('#00A500')
rabbit.up()

dist = 10
angle = 90
rabbit.left(90)
rabbit.forward(100)
for _ in range(15):
    rabbit.stamp()
    rabbit.forward(dist)
    rabbit.right(angle)
    angle -= 3
    dist += 5

rabbit.goto(-100,-100)
print(rabbit.heading())

wn.exitonclick()
