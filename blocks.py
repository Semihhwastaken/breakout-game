from turtle import Turtle

class Blocks(Turtle):
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.blocks = []
    self.block_size = (1.5,2.2,1.0)
    
  def create_block(self):
    for _ in range(60):
      new_block = Turtle("square")
      new_block.turtlesize(*self.block_size)
      new_block.penup()
      new_block.color("gray")
      self.blocks.append(new_block)
    
  
  def line_blocks(self):
    a = 275
    b = -275
    for block in self.blocks:
      block.goto(x=b,y=a)
      b += 49
      if b > 275:
        a -=33
        b= -275
    
        
    