from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_part(position)

    def add_part(self, position):
        part = Turtle(shape="square")
        part.color("white")
        part.penup()
        part.goto(position)
        self.snake_body.append(part)

    def reset(self):
        for parts in self.snake_body:
            parts.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

    def extend(self):
        self.add_part(self.snake_body[-1].position())

    def move(self):
        for part_num in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[part_num - 1].xcor()
            new_y = self.snake_body[part_num - 1].ycor()
            self.snake_body[part_num].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
