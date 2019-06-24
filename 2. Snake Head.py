import turtle

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

# Main game loop
while True:
    mn.update()

mn.mainloop()
