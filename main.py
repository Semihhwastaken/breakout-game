import time
from turtle import *
from board import Board
from blocks import Blocks
from ball import Ball


screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)

board = Board()
ball = Ball()
blocks = Blocks()
blocks.create_block()
blocks.line_blocks()

screen.listen()
screen.onkeypress(board.move_board_left,key="Left")
screen.onkeypress(board.move_board_right,key="Right")
isGameOver = False
while not isGameOver:
  screen.update()
  ball.move()
  print(f"ball xcor: {ball.ball.xcor()}, board xcor : {board.board.xcor()}")
  if ball.ball.xcor() > 275:
    ball.x_speed *= -1
  elif board.board.distance(ball.ball) < 20 or (board.board.xcor() -80 < ball.ball.xcor() < board.board.xcor() + 80
                                                and ball.ball.ycor() == board.board.ycor()) :
    ball.y_speed *= -1
  elif ball.ball.xcor() < -275:
    ball.x_speed *= -1
  elif ball.ball.ycor() < -285:
    ball.x_speed = 0
    ball.y_speed = 0
    isGameOver = False
  elif ball.ball.ycor() > 285:
    ball.y_speed *= -1
  
  for block in blocks.blocks:
    if block.distance(ball.ball) < 20:
      block.hideturtle()
      blocks.blocks.remove(block)
      if ball.y_speed < 0:
        ball.y_speed -=1
      elif ball.x_speed < 0:
        ball.x_speed -=1
      elif ball.y_speed > 0:
        ball.y_speed +=1
      elif ball.x_speed > 0:
        ball.x_speed +=1
      ball.y_speed *= -1
      
    
  
  

screen.mainloop()


