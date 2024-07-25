from package.setting import *

#Khởi tạo widget
class widget:
  def __init__(self) -> None:
    #sface là một vùng được định nghĩa có thể vẽ và bị vẽ lên
    self.sface = pg.surface.Surface(DEFAULT_SIZE)
    #màu mặc định background của widget
    self.default_color = BLACK
    self.sface.fill(self.default_color)

    #vị trí mặc định để vẽ sface lên sfaceparent
    self.pos = ZERO_P
    
    self.fill = True
    #hàm kiểm tra khi nhấn chuột vào mặt phẳng
    self.is_hover = False
    #hàm kiểm tra khi nhấn chuột vào mặt phẳng
    self.is_mousedown = False 
    self.is_mouseup = False 

    #gọi đến khi click
    self.event_mousedown = None

    self.event_mouseup = None

  def get_rect(self):
    return pg.rect.Rect(self.pos, self.get_size())

  def set_size(self, size):
    self.sface = pg.surface.Surface(size)
  
  def get_size(self):
    return self.sface.get_size()
    
  def set_bg(self, color):
    self.sface.fill(color)
    
  def set_pos(self, lefttop=None, midtop=None, righttop=None, leftmid=None, center=None, rightmid=None, leftbot=None, midbot=None, rightbot=None):
    #thiết lặp vị trí sface dựa vào các điểm 
    if center != None:
      #một nữa kích thước sface là trung tâm
      s_x, s_y = Half_size(self.sface.get_size())
      c_x, c_y = center
      #Thiết lập pos khi điểm trung tâm nằm ở center
      self.pos = c_x - s_x, c_y - s_y
      return
    elif lefttop != None:
      self.pos = lefttop
      return
    elif midtop != None:
      s_x, s_y = Half_size(self.sface.get_size())
      mt_x, mt_y = midtop
      #Thiết lập pos khi điểm giữa trên nằm ở midtop
      self.pos = mt_x - s_x, mt_y
      return
    elif righttop != None:
      s_x, s_y = self.sface.get_size()
      rt_x, rt_y = righttop
      #Thiết lập pos khi điểm giữa trên nằm ở righttop
      self.pos = rt_x - s_x, rt_y
      return
    elif leftmid != None:
      s_x, s_y = Half_size(self.sface.get_size())
      lm_x, lm_y = leftmid
      #Thiết lập pos khi điểm giữa trên nằm ở leftmid
      self.pos = lm_x, lm_y - s_y
      return
    elif rightmid != None:
      s_x, s_y = self.sface.get_size()
      rm_x, rm_y = rightmid
      #Thiết lập pos khi điểm giữa trên nằm ở rightmid
      self.pos = rm_x - s_x, rm_y - int(s_y//2)
      return
    elif leftbot != None:
      s_x, s_y = self.sface.get_size()
      lb_x, lb_y = leftbot
      #Thiết lập pos khi điểm giữa trên nằm ở leftbottom
      self.pos = lb_x, lb_y - s_y
      return
    elif midbot != None:
      s_x, s_y = self.sface.get_size()
      mb_x, mb_y = midbot
      #Thiết lập pos khi điểm giữa trên nằm ở midbottom
      self.pos = mb_x - int(s_x//2) , mb_y - s_y
      return
    elif rightbot != None:
      s_x, s_y = self.sface.get_size()
      rb_x, rb_y = rightbot
      #Thiết lập pos khi điểm giữa trên nằm ở rightbottom
      self.pos = rb_x - s_x, rb_y - s_y
      return

  def event(self, parent_pos=ZERO_P):
    #khi widget nằm trong một widget khác phải cộng thêm parent pos
    #Kiểm tra chuột có nằm trong vùng kích thước và vị trí của sface
    pos = self.pos[0] + parent_pos[0], self.pos[1] + parent_pos[1]
    rect = pg.rect.Rect(pos, self.sface.get_size())

    #Kiểm tra vị trí chuột
    if rect.collidepoint(pg.mouse.get_pos()):
      #là hover khi chuột nằm bên trong rect
      self.is_hover = True
    elif self.is_hover:
      #nếu không nằm trong
      self.is_hover = False
      self.is_mouseup = self.is_mousedown = False

    click = pg.mouse.get_pressed()
    #
    if self.is_hover and click[0]:
      #nếu hover và click chuột trái
      self.is_mousedown = True
      
    elif self.is_mousedown:
      #nếu thả chuột trái thì bắt đầu event 
      self.is_mousedown = False

      
  def update(self):
    #clear sface với màu mặc định để băt đầu vẽ lại
    self.sface.fill(self.default_color) if self.fill else 0

    if self.is_mousedown != self.is_mouseup:
      self.is_mouseup = self.is_mousedown
      
      #Nếu hàm event_mousedown tồn tại
      self.event_mousedown(self) if self.event_mousedown != None and self.is_mousedown else 0

      #Nếu hàm event_mouseup tồn tại
      self.event_mouseup(self) if self.event_mouseup != None and not self.is_mousedown else 0

  def render(self, sf_parent:pg.surface.Surface):
    #Vẽ sface lên sface_parent tại vị trí pos
    sf_parent.blit(self.sface, self.pos)