from pygame import Surface
from package.setting import *
from package.widget import *

#Khởi tạo button
class Button(widget):
  def __init__(self, text, auto_size=True) -> None:
    super().__init__()
    #Chữ trên button
    self.txt = None
    self.font = None

    #auto size là thiết lập kích thước nút
    #sface nút tự động vừa với chữ
    self.auto_size = True
    self.set_text(text)
    self.auto_size = auto_size
    
    self.block_hover = False

  def get_text_size(self):
    return self.txt_sface.get_size()
  
  def set_size(self, size):
    super().set_size(size)

    self.auto_center()

  def set_text(self, text=None, name_font=FONT_SVN_RETRON, text_size=FONT_SIZE, text_color=TEXT_COLOR):
    #Chữ trên button
    if self.txt is None or (text != None and self.txt != text):
      #Nếu name button chưa tồn tại
      #Hoặc đã tồn tại nhưng khác text đã tồn tại
      self.txt = text

    if self.font is None or name_font != FONT_SVN_RETRON or text_size != FONT_SIZE:
      #Nếu fone chữ chưa tồn tại
      #Hoặc đã tồn tại nhưng name_font và text_size khác mặc định
      self.font = pg.font.Font(name_font, text_size)
    
    #tạo text_sface để vẽ lên sface
    self.txt_sface = self.font.render(self.txt, True, text_color)
    self._auto_size() if self.auto_size else 0

  def auto_center(self):
    s_x, s_y = Half_size(self.txt_sface.get_size())
    c_x, c_y = Half_size(self.sface.get_size())

    #tạo vị trí text đựa trên sface của widget
    #vị trí này nằm giữa sface
    self.txt_pos = c_x - s_x, c_y - s_y + FONT_PADDING_TOP

  def _auto_size(self):
    #Tạo auto_size cho sface
    #lấy kích thước của txt_sface
    size = self.get_text_size()
    #cộng thêm padding để thẩm mỹ
    size_padding = size[0] + MENU_PADDING[0] * 2, size[1] + MENU_PADDING[1] * 2
    self.set_size(size_padding)
    self.auto_center()

  def update(self):
    super().update()

    #Nếu không khóa button khỏi nhấn
    if not self.block_hover:
      #thiết lập màu sface cho nút khi có event
      self.set_bg(GREEN) if self.is_hover else 0
      self.set_bg(RED) if self.is_mousedown else 0

  def render(self, sf_parent: Surface):
    #Vẽ text lên sface tại text_pos
    self.sface.blit(self.txt_sface, self.txt_pos)
    super().render(sf_parent)

#Label là Button khi không nhấn được
class Label(Button):
  def __init__(self, text) -> None:
    super().__init__(text)
    self.block_hover = True

