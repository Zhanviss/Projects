from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
color = ["red", "orange", "blue", "green", "yellow", "purple"]
y_pos = [-125, -75, -25, 25, 75, 125]
all_turtles = []
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-235, y=y_pos[turtle_index])
    all_turtles.append(new_turtle)

bet = screen.textinput("Make your bet:",
                       "Which turtle wins the race? (ENTER THE COLOR")
if bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == bet:
                print(f"You've won! The {winning_color} is the winner!")
            else:
                print(f"You've lost! The {winning_color} is the winner!")
        random_pace = random.randint(0, 10)
        turtle.forward(random_pace)


screen.exitonclick()
