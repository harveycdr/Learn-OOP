from package.setting import *
from screen.screen import *
from package.menu import *
from package.button import *

class InforScreen(screen):
  def __init__(self, screen_size) -> None:
    super().__init__(screen_size)
    w,h = SCREEN_SIZE
    self.infor = Menu( "Thông tin về game",
                    [
                      f"Đây là tựa game xếp hình",
                      f"Là đề tài tự chọn cho môn học Xử lý ảnh",
                      f"Được phát triển bằng pygame và được lập trình bằng mô hình hướng đối tượng",
                      f"---",
                      f"Các sinh viên tham gia phát triển:",
                      f"Đinh Phi Hậu - 2051120231",
                      f"Nguyễn Xuân Hậu - 2051120232"
                    ])
    self.infor.set_pos(center=Half_size(screen_size))

    self.back = Button("Quay lại")
    self.back.set_pos(lefttop=ZERO_P)
    self.back.event_mouseup = lambda obj: self.back_click(obj)
    self.event_back_menu = None
    self.event_setscreen = None

    #Chặn nút
    for i in self.infor.controls:
      i.block_hover = True

    self.controls.append(self.infor)
    self.controls.append(self.back)

  def screen_resize(self, screen_size):
    self.set_size(screen_size)
    self.infor.set_pos(center=Half_size(screen_size))
    self.back.set_pos(lefttop=ZERO_P)

  def back_click(self, obj:Button):
    self.event_back_menu("back") if self.event_back_menu != None else 0
