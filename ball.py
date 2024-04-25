from turtle import Turtle

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.ball = Turtle("circle")
    self.ball.shapesize(0.7,0.7)
    self.ball.penup()
    self.x_speed = 2
    self.y_speed = 2
  
  def move(self):
      self.ball.setx(self.ball.xcor() + self.x_speed)
      self.ball.sety(self.ball.ycor() + self.y_speed)
      
      