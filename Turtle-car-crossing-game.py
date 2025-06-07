from turtle import Screen
import time
from src.player import Player
from src.cars import Cars
from src.score import Score
from src.border import Border

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=550)
screen.tracer(0)
screen.title("Cross Road Turtle")

player = Player()
car = Cars()
score = Score()
border = Border()

screen.listen()
screen.onkey(player.go_up, "Up")

is_on = True
while is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_forward()

    for c in car.all_cars:
        if c.distance(player) < 20:
            player.go_to_start()
            score.game_over()
            is_on = False

    if player.is_at_finish():
        player.go_to_start()
        car.level_up() 
        score.scr += 1
        score.score_update()

screen.exitonclick()