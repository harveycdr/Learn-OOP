from package.setting import *
from screen.screen import *
from package.menu import *
from package.button import *

class MenuScreen(screen):
  def __init__(self, screen_size) -> None:
    super().__init__(screen_size)
    self.menu = Menu("Menu của game", ["Bắt đầu", "Tiếp tục", "Cài đặt", "Thông tin","Thoát"])
    self.menu.set_pos(center=Half_size(screen_size))
    self.menu.event_menuclick = lambda obj: self.menu_click(obj)

    self.event_menuclick = None

    self.controls.append(self.menu)

  def menu_click(self, obj:Menu):
    self.event_menuclick(obj) if self.event_menuclick != None else 0

  def screen_resize(self, screen_size):
    self.set_size(screen_size)
    self.menu.set_pos(center=Half_size(screen_size))