import turtle
import time
import random
import winsound
from playsound import playsound

winsound.PlaySound("Peace1.wav", winsound.SND_ASYNC)

delay = 0.1

body_colours = ["yellow", "blue", "red", "black", "white"]
body_count = 0

# Score
score = 0
high_score = 0

mn = turtle.Screen()
mn.title("미르의 모험")
mn.bgcolor("grey")
mn.bgpic("11.gif")
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

segments = [] # at the start of the game there are no segments

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0  High score: 0", align="center", font=("Courier", 24, "normal"))
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


#Main game loop
while True:
    mn.update()

    # Check for a collision with the border
    if head.xcor() > 290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        playsound("Gameover.wav")
        time.sleep(1) # pause
        head.goto(0,0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000) # sends all segments to 1000,1000, could not find a way to delete

        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align= "Center", font=("Courier", 24, "normal"))

    # Check for a collision with the food
    if head.distance(food) < 20: #measures distance between two turtles, basic turtle pixel = 20
        # Move the food to a random spot
        #winsound.PlaySound("power.wav", winsound.SND_ASYNC)
        playsound("power.wav")
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x,y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        bc = body_count%5
        new_segment.color(body_colours[bc])
        new_segment.penup()
        segments.append(new_segment)


        # Shorten the delay
        delay -= 0.001
        
        # Increase the score
        score += 1
        body_count += 1
        food.color(body_colours[body_count%5])

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align= "Center", font=("Courier", 24, "normal"))
    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    #Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)
        
    move()

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) <20:
            playsound("Gameover.wav")
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000) # sends all segments to 1000,1000, could not find a way to delete

            # Reset the score
            score = 0
            
            # Reset the delay
            delay = 0.1
            
            # Clear the segments list
            segments.clear()

            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align= "Center", font=("Courier", 24, "normal"))
    time.sleep(delay) #stops program from 1/10th of a second

mn.mainloop() # keeps code open
