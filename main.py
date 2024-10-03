from turtle import Turtle, Screen
import time
import random
from snake import Snake
from food import Food

pixel_size = 20
snake = Snake(3,pixel_size=pixel_size)
snake.generate_screen()
snake.generate_snake()
snake.update_score_board()
snake.draw_walls()
snake.screen.update()

snake.game_on()

snake.screen.exitonclick()