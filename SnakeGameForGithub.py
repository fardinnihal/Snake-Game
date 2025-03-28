import turtle
import random
import time


screen= turtle.Screen()
screen.title("Fardin's snake game")
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.tracer(0)

head= turtle.Turtle()
head.shape("square")
head.color("green")
head.penup()  #for leaving no trail behind
head.goto(0,0)
head.direction='stop'

segments=[]
#Food
food= turtle.Turtle()
food.shape("circle")
food.color("pink")
food.penup()
food.goto(0,100)

speed = 0.1

#direction
def go_up():
    if head.direction!='down':
        head.direction='up'
def go_down():
    if head.direction!='up':
        head.direction='down'
def go_left():
    if head.direction!='right':
        head.direction='left'
def go_right():
    if head.direction!='left':
        head.direction='right'

def move():
    if head.direction=='up':
        y= head.ycor()
        head.sety(y+20)
    if head.direction=='down':
        y=head.ycor()
        head.sety(y-20)
    if head.direction=='left':
        x=head.xcor()
        head.setx(x-20)
    if head.direction=='right':
        x=head.xcor()
        head.setx(x+20)

#Keyboard commands
screen.listen()
screen.onkey(go_up,'w')
screen.onkey(go_down,'s')
screen.onkey(go_left,'a')
screen.onkey(go_right,'d')
while True:
    screen.update()
    if head.distance(food)<20:
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        new_segment=turtle.Turtle()
        new_segment.color('white')
        new_segment.shape('square')
        new_segment.penup()
        segments.append(new_segment)

        speed-=.001
    for i in range (len(segments)-1,0,-1):
        x=segments[i-1].xcor()
        y=segments[i-1].ycor()
        segments[i].goto(x,y)
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
    move()
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction='stop'
            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()
            speed=0.1 #previous speed
    if abs(head.xcor())>290 or abs(head.ycor())>290:
        time.sleep(1)
        head.goto(0,0)
        head.direction='stop'
        for segment in segments:
            segment.goto(1000,1000)
        segments.clear()
        speed=0.1
    time.sleep(speed)

screen.mainloop()
        
        
    








    
