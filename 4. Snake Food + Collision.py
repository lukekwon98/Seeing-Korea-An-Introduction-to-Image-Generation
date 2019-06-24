import turtle
import time
import random

delay = 0.1

body_colours = ["yellow", "blue", "red", "black", "white"]
body_count = 0

# Set up the screen

mn = turtle.Screen()
mn.title("미르의 모험")
mn.bgcolor("green")
mn.setup(width=600, height=600)
mn.tracer(0) #turns off animation on screen(), screen updates

# Snake head
head = turtle.Turtle()
head.speed(0) # not actual speed, speed of turtle module, fastest animation speed
head.shape("square") #triange
head.color("white")
head.penup() # doesn't draw lines
head.goto(0,0) # head starts in center of screen
head.direction = "stop" #doesn't move when started

# Snake food
food = turtle.Turtle()
food.speed(0) # not actual speed, speed of turtle module, fastest animation speed
food.shape("circle") #triange
food.color(body_colours[body_count%5])
food.penup() # doesn't draw lines
food.goto(0,100) # head starts in center of screen

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"
    
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
        
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Keyboard bindings
mn.listen()
mn.onkeypress(go_up, "w")
mn.onkeypress(go_down, "s")
mn.onkeypress(go_left, "a")
mn.onkeypress(go_right, "d")

        
# Main game loop
while True:
    mn.update()

    if head.distance(food) < 20: #measures distance between two turtles, basic turtle pixel = 20
        # Move the food to a random spot
        #winsound.PlaySound("power.wav", winsound.SND_ASYNC)
        #playsound("power.wav")
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x,y)
    
    move()

    time.sleep(delay)

mn.mainloop()
