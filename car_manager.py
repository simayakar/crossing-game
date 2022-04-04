from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.move_speed = STARTING_MOVE_DISTANCE

    def car_generator(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            rand_color = random.choice(COLORS)
            car.color(rand_color)
            rand_y = random.randint(-250, 250)
            car.goto(300, rand_y)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.setheading(180)
            car.forward(self.move_speed)

    def speed_up(self):
        self.move_speed += MOVE_INCREMENT
