from turtle import Turtle
position = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake:

    def __init__(self):
        self.number_of_turtles = []
        self.create_snake()
        self.head = self.number_of_turtles[0]

    def create_snake(self):
        for i in position:
            self.add_segment(i)


    def move(self):
        for i in range(len(self.number_of_turtles) - 1, 0, -1):
            new_x = self.number_of_turtles[i - 1].xcor()
            new_y = self.number_of_turtles[i - 1].ycor()
            self.number_of_turtles[i].goto(new_x, new_y)
        self.number_of_turtles[0].forward(MOVE_DISTANCE)

    def add_segment(self, i):
        turtle = Turtle('square')
        turtle.color('white')
        turtle.penup()
        turtle.goto(i)
        self.number_of_turtles.append(turtle)

    def reset(self):
        for seg in self.number_of_turtles:
            seg.goto(1000, 1000)
        self.number_of_turtles.clear()
        self.create_snake()
        self.head = self.number_of_turtles[0]

    def extent(self):
        self.add_segment(self.number_of_turtles[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
