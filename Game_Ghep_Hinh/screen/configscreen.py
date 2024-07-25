from package.setting import *
from screen.screen import *
from package.menu import *
from package.button import *

class ConfigScreen(screen):
  def __init__(self, screen_size) -> None:
    super().__init__(screen_size)
    w,h = SCREEN_SIZE
    self.menu = Menu("Thiết lập màn hình game", 
                    [
                      f"{w}x{h}",
                      f"{int(w*1.25)}x{int(h*1.25)}",
                      f"{int(w*1.5)}x{int(h*1.5)}",
                      f"{int(w*2)}x{int(h*2)}"
                    ])
    self.menu.set_pos(center=Half_size(screen_size))
    self.menu.event_menuclick = lambda obj: self.menu_click(obj)

    self.back = Button("Quay lại")
    self.back.set_pos(lefttop=ZERO_P)
    self.back.event_mouseup = lambda obj: self.back_click(obj)
    self.event_back_menu = None
    self.event_setscreen = None

    self.controls.append(self.menu)
    self.controls.append(self.back)

  def screen_resize(self, screen_size):
    self.set_size(screen_size)
    self.menu.set_pos(center=Half_size(screen_size))
    self.back.set_pos(lefttop=ZERO_P)

  def back_click(self, obj:Button):
    self.event_back_menu("back") if self.event_back_menu != None else 0

  def menu_click(self, obj:Menu):
    print("thiết lập màn hình: " + obj.value_selection())
    width, height = self.menu.value_selection().split('x')
    change_sz = int(width), int(height)
    self.event_setscreen(change_sz) if self.event_setscreen != None else 0
