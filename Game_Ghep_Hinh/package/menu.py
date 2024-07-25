
from package.button import *
from package.control import *

class Menu(control):
  def __init__(self, title_menu, options=None) -> None:
    super().__init__()

    #Tạo tiêu đề cho menu
    self.title_sface = Label(title_menu)
    self.title_sface.set_text(text_color=WHITE, text_size=FONT_SIZE+5)

    #Gọi đến even khi nhấn một nút trong menu
    self.event_menuclick = None

    self.selectIndex = -1

    self.controls.append(self.title_sface)

    super().set_size(self.title_sface.get_size())

    #Menu bao gồm các nút lựa chọn
    if options != None:
      for option_str in options:
        self.add_option(option_str)


  def add_option(self, text_option):
    button = Button(text_option)
    #event khi nhấn các nút gọi hàm click
    button.event_mouseup = lambda obj: self.click(obj)

    w = Max([self.get_size()[0], button.get_size()[0]])
    h = self.get_size()[1] + button.get_size()[1]
    self.controls.append(button)
    super().set_size((w, h))

    #điều chỉnh lại vị trí tất cả các thànhh phânf option
    midtop = (w//2, 0)
    for ele in self.controls:
      ele.set_pos(midtop=midtop)
      midtop = midtop[0], midtop[1] + ele.get_size()[1]

  def click(self, obj):
    #Tìm index trong các lựa chọn
    self.selectIndex = self.controls.index(obj) - 1

    self.event_menuclick(self) if self.event_menuclick != None else 0

  def value_selection(self) -> str:
    #Trả về chữ tại vị trí đã nhấn
    return self.controls[self.selectIndex + 1].txt
