import turtle as tu

wn = tu.Screen()

# turtle 1
elan = tu.Turtle()

elandist = 50
elanangle = 90
for _ in range(10):
    elan.forward(elandist)
    elan.right(elanangle)
    elandist += 10
    elanangle -= 3

# new turtle
drake = tu.Turtle()
drake.color('red')

drake.right(180)
drake.forward(100)
drake.up()
for _ in range(10):
    drake.forward(10)
    drake.down()
    drake.forward(15)
    drake.up()

# new turtle
rabbit = tu.Turtle()
rabbit.shape('turtle')
rabbit.color('#00A500')
rabbit.up()

rabbitlen = 10
rabbitangle = 90
rabbit.left(90)
rabbit.forward(100)
for _ in range(15):
    rabbit.stamp()
    rabbit.right(rabbitangle)
    rabbit.forward(rabbitlen)
    rabbitlen += 5
    if rabbitangle > 5:
        rabbitangle -= 5

wn.exitonclick()
