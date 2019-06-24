import turtle
import time

delay = 0.1

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

    move()

    time.sleep(delay)

mn.mainloop()
