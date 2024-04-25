from turtle import Turtle
DISTANCE = 40

class Board(Turtle):
  def __init__(self):
    super().__init__()
    self.draw_board()
    self.hideturtle()
  def draw_board(self):
    self.board = Turtle("square")
    self.board.shapesize(stretch_len=7,stretch_wid=1)
    self.board.penup()
    self.board.goto(x=0,y=-230)
    
  
  def move_board_left(self):
    x_cor = self.board.xcor()
    x_cor -= DISTANCE
    if x_cor > -250:
      self.board.goto(x=x_cor,y=-230)
  
  def move_board_right(self):
    x_cor = self.board.xcor()
    x_cor += DISTANCE
    if x_cor < 250:
      self.board.goto(x=x_cor,y=-230)
    
  
  
    
  

    