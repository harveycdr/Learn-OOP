from package.setting import *
from package.control import *

class screen(control):
  def __init__(self, screen_size) -> None:
    super().__init__()
    self.set_size(screen_size)

  def screen_resize(self, screen_size):
    pass
