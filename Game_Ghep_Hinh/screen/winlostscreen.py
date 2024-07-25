from package.setting import *
from screen.screen import *
from package.menu import *
from package.button import *
from package.photo import *

class WinLostScreen(screen):
  def __init__(self, screen_size, winner) -> None:
    super().__init__(screen_size)
    self.label = Label("")
    text_continues = ""
    sface = None
    if winner:
      self.label.set_text(text="Chúc mừng bạn đã chiến thắng!", text_size=30, text_color=GREEN)
      text_continues = "Tiếp tục game"
      sface = level.get_level().img2sface()
    else:
      self.label.set_text(text="Bạn đã thua cuộc!", text_size=30, text_color=RED)
      text_continues = "Chơi lại"
      image = level.get_level().img2Image().filter(ImageFilter.GaussianBlur(RADIUS_BLUR))
      sface = BytesToSurface(image.tobytes(), level.get_level().size, level.get_level().mode )

    pos_he = 0
    self.label.set_pos(midtop=(screen_size[0]//2, 0))
    pos_he += self.label.get_size()[1]
    
    #kích thước board vừa với màn hình theo tỉ lệ BOARD_SCALE
    size_scaled = scale_size_to_fit(level.get_level().size, nhan2d(screen_size, BOARD_SCALE))
    
    
    self.photo = Photo(sface)
    self.photo.scale_size(size_scaled)
    self.photo.set_pos(midtop=(screen_size[0]//2, pos_he))
    pos_he += self.photo.get_size()[1]

    self.back = Button("Quay lại Menu")
    self.back.set_pos(midtop=(0.25*screen_size[0], pos_he+10))
    self.back.event_mouseup = lambda obj: self.back_click(obj)


    self.continue_game = Button(text_continues)
    self.continue_game.set_pos(midtop=(0.75*screen_size[0], pos_he+10))
    self.continue_game.event_mouseup = lambda obj: self.continue_click(obj)
    
    self.event_back_menu = None
    self.event_continue_game = None

    self.controls.append(self.label)
    self.controls.append(self.photo)
    self.controls.append(self.back)
    self.controls.append(self.continue_game)

  def back_click(self, obj:Button):
    self.event_back_menu("back") if self.event_back_menu != None else 0

  def continue_click(self, obj:Button):
    self.event_continue_game("back") if self.event_continue_game != None else 0
