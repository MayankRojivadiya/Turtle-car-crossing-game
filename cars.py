from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREASE = 10


class Cars:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        
    
    def create_car(self):
        random_chance = random.randint(1,5)
        if random_chance == 2:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-210, 210)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car) 
    
    def move_forward(self):
        for i in self.all_cars:
            i.backward(self.car_speed) 
            if i.xcor() < -300:
                i.color("black")
    
    def level_up(self):
        self.car_speed += MOVE_INCREASE