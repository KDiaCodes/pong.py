import table, random

class Ball:
  def __init__(self, table, width=14, height=14, colour="red", x_speed=6, y_speed=4, x_start=0, y_start=0):
    self.width = width
    self.height = height
    self.x_posn = x_start
    self.y_posn = y_start
    self.colour = colour
    
    self.x_start = x_start
    self.y_start = y_start
    self.x_speed = x_speed
    self.y_speed = y_speed
    self.table = table
    self.circle = self.table.draw_oval(self)
    
  def start_position(self):
    self.x_posn = self.x_start
    self.y_posn = self.y_start
    
  def start_ball(self, x_speed, y_speed):
    self.x_speed = -x_speed if random.randint(0, 1) else x_speed
    self.y_speed = -y_speed if random.randint(0, 1) else y_speed
    self.start_position()
    
  def move_next(self):
    self.x.posn= self.x_posn + self.x_speed
