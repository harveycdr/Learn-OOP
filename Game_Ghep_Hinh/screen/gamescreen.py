from pygame.surface import Surface
from package.setting import *
from screen.screen import *
from package.menu import *
from package.button import *
from package.setting import ZERO_P
from package.widget import *
from package.photo import *
from package.widget import ZERO_P

# img = pg.image.load(f"{os.getcwd()}\\src\\img\\newcogai.png")

# lv = {
#   "title": "lv 1: Cô gái",
#   "img": img,
#   "size": img.get_size(),
#   "matrix": (3,3),
#   "link": f"{os.getcwd()}\\src\\img\\newcogai.png"
# }



class BoardBlank(control):
  def __init__(self, screen_size) -> None:
    super().__init__()
    self.initallcomponent(screen_size)
    self.event_board_setimg = None
    self.event_remove_img = None
    self.sukien_hoanthanh_game = None

  def initallcomponent(self, screen_size):
    #lấy row col từ lv
    row, col = level.get_level().matrix

    #kích thước board vừa với màn hình theo tỉ lệ BOARD_SCALE
    size_scaled = scale_size_to_fit(level.get_level().size, nhan2d(screen_size, BOARD_SCALE))
    #kích thước 1 ảnh con để ghép ảnh lớn
    w, h = size_scaled[0] // col, size_scaled[1] // row

    #kích thước của board bao gồm các ảnh con ghép thành ảnh lớn và các line gird 
    board_size = size_scaled[0] + col + 1, size_scaled[1] + row + 1
    self.set_size(board_size)
    self.default_color = GRAY

    for n in range(row*col):
      i, j = n % col, n // col
      p = Photo()
      p.set_size((w, h))
      #xét vị trí thêm đường kẻ
      p.set_pos(lefttop=(w*i + (i+1), h*j + (j+1)))
      self.controls.append(p)

  def set_child_photo(self, photo):
    for i in self.controls:
      if i.is_hover:
        if i.index != -1:
          self.event_remove_img(i) if self.event_remove_img != None else 0
        i.index = photo.index
        i.sface = photo.sface
        i.event_mouseup = lambda obj: self.photo_mouseup(obj)

    if self.is_complete():
      self.sukien_hoanthanh_game(True) if self.sukien_hoanthanh_game != None else 0

  def photo_mouseup(self, obj:Photo):
    if obj.index != -1:
      self.event_remove_img(obj) if self.event_remove_img != None else 0
      obj.index = -1
      obj.set_bg(obj.default_color)
      obj.event_mouseup = None

  def is_complete(self):
    row, col = level.get_level().matrix
    for i in range(row * col):
      if self.controls[i].index != i:
        return False
    return True

class BoardPuzzle(control):
  def __init__(self, screen_size) -> None:

    super().__init__()
    self.initallcomponent(screen_size)
    self.event_hold_img = None

  def initallcomponent(self, screen_size):
    #lấy row col từ lv
    row, col = level.get_level().matrix

    #kích thước board chứa các split của img
    puzzle_size = nhan2d(screen_size, BOARD_SCALE)
    self.set_size(puzzle_size)
    self.default_color = GRAY
    
    #kích thước board vừa với màn hình theo tỉ lệ BOARD_SCALE
    size_scaled = scale_size_to_fit(level.get_level().size, nhan2d(screen_size, BOARD_SCALE))
    photo = Photo(level.get_level().img2sface())
    photo.scale_size(size_scaled)
    #kích thước 1 ảnh con để ghép ảnh lớn
    w, h = size_scaled[0] // col, size_scaled[1] // row

    for n in range(row*col):
      i, j = n % col, n // col
      sface = photo.sface.subsurface((i*w,j*h), (w,h))
      child_photo = Photo(sface, n)
      self.add_photo_rnd_pos(child_photo)

  def add_photo_rnd_pos(self, photo:Photo):
    if photo is None:
      return
  
    child = Photo(photo.sface, photo.index)
    p_x = random.randint(0, self.get_size()[0])
    p_y = random.randint(0, self.get_size()[1])
    child.set_pos(center=(p_x, p_y))
    child.event_mousedown = lambda obj: self.img_mousedown(obj)
    self.controls.append(child)

  def img_mousedown(self, obj):
    self.event_hold_img(obj) if self.event_hold_img != None else 0

class GameScreen(screen):
  def __init__(self, screen_size) -> None:
    super().__init__(screen_size)
    self.setlevel_game(screen_size)
    self.setposallcomponent(screen_size)

    self.img_select = None
    self.event_back_menu = None
    self.sukien_hoanthanh_game = None

  def setlevel_game(self, screen_size):
    #Tạo nút quay lại
    self.back = Button("Quay lại")
    self.back.event_mouseup = lambda obj: self.back_click(obj)

    self.start_game = False
    self._tick = 0
    self.time_limited = level.get_level().countdown
    self.countdown = Label(f"Đếm ngược: {self.time_limited} giây")

    self.title_image = Label(level.get_level().name)

    self.board = BoardBlank(screen_size)
    self.board.event_remove_img = lambda obj: self.event_remove_img(obj)
    self.board.sukien_hoanthanh_game = lambda obj: self.sukien_hoanthanh_game(obj)
    
    self.puzzle = BoardPuzzle(screen_size)
    self.puzzle.event_hold_img = lambda obj: self.event_hold_img(obj)

    self.demo_img = Photo(level.get_level().img2sface())
    self.demo_img.scale_size( scale_size_to_fit(self.demo_img.get_size(), nhan2d_hs(screen_size, IMG_BOARD_DEMO)) )

    self.controls = []
    self.controls.append(self.back)
    self.controls.append(self.countdown)
    self.controls.append(self.title_image)
    self.controls.append(self.puzzle)
    self.controls.append(self.board)
    self.controls.append(self.demo_img)
    
  def setposallcomponent(self, screen_size):
    self.back.set_pos(lefttop=ZERO_P)
    self.countdown.set_pos(midtop=(screen_size[0]//2, 0))
    self.board.set_pos(leftmid=(0+3, screen_size[1]//2))
    self.puzzle.set_pos(rightmid=(screen_size[0]-3, screen_size[1]//2))
    self.demo_img.set_pos(leftbot=(0,screen_size[1]))
    self.title_image.set_pos(leftbot=(self.demo_img.get_size()[0],screen_size[1]))

  def event_remove_img(self, obj:Photo):
    self.puzzle.add_photo_rnd_pos(obj)

  def event_hold_img(self, obj):
    if self.img_select is None:
      if not self.start_game:
        self.start_game = True
        self._tick = time.time()

      self.img_select = obj

      #Sự kiện kết thúc nhấn chuột trái
      self.img_select.event_mouseup = lambda obj: self.event_release_img(obj)
      self.puzzle.controls.remove(obj)

  def event_release_img(self, obj):
    #Nếu ảnh đã được chọn 
    if self.img_select != None:
      #Nếu ảnh và chuột nằm trong self.puzzle thì khi bỏ chuột sẽ giữ vị trí cũ
      if self.puzzle.get_rect().collidepoint(pg.mouse.get_pos()):
        self.img_select.set_pos(center=tru2d(pg.mouse.get_pos(), self.puzzle.pos))
        self.puzzle.controls.append(self.img_select)

      #Nếu ảnh và chuột nằm trong self.board thì gán ảnh lên child Image
      elif self.board.get_rect().collidepoint(pg.mouse.get_pos()):
        self.board.set_child_photo(self.img_select)

      #Nếu nằm ngoài khi bỏ chuột sẽ random vị trí và thêm vào lại self.puzzle
      else:
        self.puzzle.add_photo_rnd_pos(self.img_select)

      self.img_select = None
      
  def screen_resize(self, screen_size):
    self.set_size(screen_size)
    self.setlevel_game(screen_size)
    self.setposallcomponent(screen_size)

  def back_click(self, obj:Button):
    self.event_back_menu(obj) if self.event_back_menu != None else 0

  def event(self, parent_pos=ZERO_P):
    super().event(parent_pos)
    self.img_select.event() if self.img_select != None else 0
    
    
  def update(self):
    super().update()
    self.img_select.update() if self.img_select != None else 0

    if self.start_game:
      tick = time.time()
      if tick - self._tick >= 1:
        self.time_limited -= 1
        self._tick = tick
        self.countdown.set_text(f"Đếm ngược: {self.time_limited} giây")

      if self.time_limited <= 0:
        #kết thúc game
        self.sukien_hoanthanh_game(False) if self.sukien_hoanthanh_game != None else 0
    

  def render(self, sf_parent: Surface):
    super().render(sf_parent)
    
    if self.img_select != None:
      # print("hello") if self.img_select.is_hover else 0
      mouse_pos = pg.mouse.get_pos()
      self.img_select.set_pos(center=mouse_pos)
      self.img_select.render(sf_parent)

    

