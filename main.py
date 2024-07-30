import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")
player = Player()

screen.listen()
screen.onkeypress(player.move, "Up")

scoreboard = Scoreboard()
game_is_on = True
cars = CarManager()


while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.generate_car()

    cars.move_car()

    if player.reset_position():
        scoreboard.update_score()
        cars.increase_speed()

    for car in cars.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.clear()
            scoreboard.goto(0, 0)
            scoreboard.write("GAME OVER", align="center", font=("Courier", 24, "normal"))

screen.exitonclick()
