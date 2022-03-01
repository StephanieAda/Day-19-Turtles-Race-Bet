from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Choose your winner from the colors of the rainbow", prompt="Which Turtle color?: ")
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

start_game = False
#
# for i in range(0,7):
#     if user_bet == i:
#         start_game = True

if user_bet:
    start_game = True

all_turtles = []
distance = -100
for i in range(0, 7):
    turtle = Turtle("turtle")
    turtle.penup()
    turtle.color(colors[i])
    turtle.goto(x=-230, y=distance)
    distance += 30
    all_turtles.append(turtle)


while start_game:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            start_game = False
            win_turtle = turtle.pencolor()
            if user_bet == win_turtle:
                print(f'yay, you won. The {win_turtle} turtle won ')
            else:
                print(f'shame, you lost. The {win_turtle} turtle won ')
        turtle.forward(random.randint(0, 10))

screen.exitonclick()
