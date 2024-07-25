from package.setting import *
from package.widget import *
#Khởi tạo control
class control(widget):
  def __init__(self) -> None:
    super().__init__()

    #chứa các widgets
    self.controls = []

  def event(self, parent_pos=ZERO_P):
    pos = self.pos[0] + parent_pos[0], self.pos[1] + parent_pos[1]
    #Đánh dấu một widget khi hover để đảm bảo chỉ 1 widget được dùng khi bị hover
    hover_one = False
    for i in self.controls[::-1]:
      i.event(pos)

      #cập nhật các hover thành false sau khi đã có 1 widget được hover
      if hover_one and i.is_hover == True:
        i.is_hover = False

      #Đánh dấu hover 1 widget đã được dùng
      hover_one = True if i.is_hover and not hover_one else 0

  def update(self):
    for i in self.controls[::-1]:
      i.update()
    
    #clear sface với màu mặc định để băt đầu vẽ lại
    self.sface.fill(self.default_color)

  def render(self, sf_parent:pg.surface.Surface):
    for i in self.controls:
      i.render(self.sface)
    #Vẽ sface lên sface_parent tại vị trí pos
    sf_parent.blit(self.sface, self.pos)