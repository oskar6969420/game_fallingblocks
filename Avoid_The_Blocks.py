import turtle
import time
import random

delay = 0.1

wn = turtle.Screen()
wn.title = ("AVOID THE FALLING SQUARE")
wn.bgcolor = ("white")
wn.tracer(0)
wn.setup(width=600, height=350)

cube = turtle.Turtle()
cube.speed(0)
cube.shape("square")
cube.color("black")
cube.penup()
cube.goto(0, -150)
cube.direction = "stop"

enemy = turtle.Turtle()
enemy.speed(0)
enemy.shape("square")
enemy.color("red")
enemy.penup()
enemy.goto(20,150)
enemy.direction = "down"

enemy2 = turtle.Turtle()
enemy2.speed(0)
enemy2.shape("square")
enemy2.color("red")
enemy2.penup()
enemy2.goto(20,150)
enemy2.direction = "down"

enemy3 = turtle.Turtle()
enemy3.speed(0)
enemy3.shape("square")
enemy3.color("red")
enemy3.penup()
enemy3.goto(20,150)
enemy3.direction = "down"

enemy4 = turtle.Turtle()
enemy4.speed(0)
enemy4.shape("square")
enemy4.color("red")
enemy4.penup()
enemy4.goto(20,150)
enemy4.direction = "down"

enemy5 = turtle.Turtle()
enemy5.speed(0)
enemy5.shape("square")
enemy5.color("red")
enemy5.penup()
enemy5.goto(20,150)
enemy5.direction = "down"

def falling():
    enemy.direction == "down"
    y = enemy.ycor()
    enemy.sety(y - 20)

def falling2():
    enemy2.direction == "down"
    y = enemy2.ycor()
    enemy2.sety(y - 20)

def falling3():
    enemy3.direction == "down"
    y = enemy3.ycor()
    enemy3.sety(y - 20)

def falling4():
    enemy4.direction == "down"
    y = enemy4.ycor()
    enemy4.sety(y - 20)

def falling5():
    enemy5.direction == "down"
    y = enemy5.ycor()
    enemy5.sety(y - 20)

def go_up():
    cube.direction = "up"
def go_down():
    cube.direction = "down"
def go_right():
    cube.direction = "right"
def go_left():
    cube.direction = "left"


def jump():
    if cube.direction == "right":
        x = cube.xcor ()
        cube.setx(x + 20)
    if cube.direction == "left":
        x = cube.xcor ()
        cube.setx(x - 20)

wn.listen()
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

while True:
    wn.update()

    jump()

    falling()

    falling2()

    falling3()

    falling4()

    falling5()

    time.sleep(delay)

    if cube.distance(enemy) < 20:
        cube.direction = "stop"
        cube.goto(0,-150)

    if cube.distance(enemy2) < 20:
        cube.direction = "stop"
        cube.goto(0,-150)

    if cube.distance(enemy3) < 20:
        cube.direction = "stop"
        cube.goto(0,-150)
    
    if cube.distance(enemy4) < 20:
        cube.direction = "stop"
        cube.goto(0,-150)
    if cube.distance(enemy) < 20:
        cube.direction = "stop"
        cube.goto(0,-150)


    if enemy.ycor() < -200:
        x = random.randint(-290, 290)
        y = random.randint(150,151)
        enemy.goto(x, y)
        enemy.direction = "stop"

    if enemy2.ycor() < -200:
        x = random.randint(-290, 290)
        y = random.randint(150,151)
        enemy2.goto(x, y)
        enemy2.direction = "stop"

    if enemy3.ycor() < -200:
        x = random.randint(-290, 290)
        y = random.randint(150,151)
        enemy3.goto(x, y)
        enemy3.direction = "stop"
    if enemy4.ycor() < -200:
        x = random.randint(-290, 290)
        y = random.randint(150,151)
        enemy4.goto(x, y)
        enemy4.direction = "stop"
    if enemy5.ycor() < -200:
        x = random.randint(-290, 290)
        y = random.randint(150,151)
        enemy5.goto(x, y)
        enemy5.direction = "stop"

    if cube.ycor() < -200 or cube.ycor() > 200 or cube.xcor() < -290 or cube.xcor() > 290:
        cube.direction = "stop"
        cube.goto(0,-150)