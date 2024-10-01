from turtle import Turtle, Screen
import time
import random
from snake import Snake

snake = Snake(3)
snake.generate_screen()
snake.generate_snake()
snake.update_score_board()
snake.draw_walls()
food = snake.generate_food()
snake.screen.update()

snake.game_on()

snake.screen.exitonclick()