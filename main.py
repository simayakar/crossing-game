import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move_forward, "Up")



game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.car_generator()
    car_manager.move()

    # WHEN TURTLE HITS THE TOP OF THE SCREEN
    if player.ycor() > 280:
        player.next_level()
        scoreboard.level_up()
        car_manager.speed_up()

    # DETECTING COLLISION WITH A CAR
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()