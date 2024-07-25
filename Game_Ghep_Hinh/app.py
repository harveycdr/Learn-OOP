from package.setting import *



from package.widget import *
from package.menu import *
from screen.screen import *
from screen.configscreen import *
from screen.menuscreen import *
from screen.gamescreen import *
from screen.inforscreen import *
from screen.winlostscreen import *

class App:
  def __init__(self, title, screen_size = SCREEN_SIZE) -> None:
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (100,100)
    pg.init()
    self.running = False

    self.root = pg.display.set_mode(screen_size)
    self.title = title
    self.screen_size = screen_size
    pg.display.set_caption(self.title)


    self.clock = pg.time.Clock()
    self.controls = []

    self.menu = MenuScreen(self.screen_size)
    self.menu.event_menuclick = lambda obj: self.menu_click(obj)

    ##screen là kiểu biến cha có thể gán thành từ nhiều screen con khác
    #ví dụ screen được gán thành screen menu, screen game, screen config
    self.screen = self.menu

  def event(self):
    for e in pg.event.get():
      if e.type == pg.QUIT:
        self.running = False
      elif e.type == pg.KEYDOWN:
        if e.key == pg.K_ESCAPE:
          self.running = False

      self.screen.event()

  def render(self):
    self.root.fill(BLACK)
    self.screen.render(self.root)

  def update(self):
    self.screen.update()

    pg.display.flip()
    self.clock.tick(FPS_TICK)
    pg.display.set_caption(self.title + f" {self.clock.get_fps():.3f}")

  def run(self):
    self.running = True

    while self.running:
      self.event()
      self.render()
      self.update()

    level.current_size = self.screen_size
    level.current_level = level.index_level if level.current_level < level.index_level else level.current_level
    level.write_level()

    pg.quit()
    print("Exit App")

    
  def start_game(self):
    if level.is_endlevel():
      showinfo("Thông báo về level mới", f"Hiện tại game chỉ mới có {len(level.game_data)} level")
      return
    
    game = GameScreen(self.screen_size)
    game.event_back_menu = lambda obj: self.backto_menu(obj)
    game.sukien_hoanthanh_game = lambda obj: self.hoanthanh_level(obj)

    self.screen = game

  def config_game(self):
    config = ConfigScreen(self.screen_size)
    config.event_back_menu = lambda obj: self.backto_menu(obj)
    config.event_setscreen = lambda obj: self.set_screen_size(obj)

    self.screen = config

  def infor_game(self):
    infor = InforScreen(self.screen_size)
    infor.event_back_menu = lambda obj: self.backto_menu(obj)

    self.screen = infor

  def menu_click(self, obj:Menu):

    if obj.selectIndex == 0: #bắt đầu
      self.start_game()
    elif obj.selectIndex == 1: #tiếp tục
      level.index_level = level.current_level
      self.start_game()
    elif obj.selectIndex == 2:
      self.config_game()
    elif obj.selectIndex == 3:
      self.infor_game()
    elif obj.selectIndex == 4:
      self.running = False

  def hoanthanh_level(self, obj):
    complete = obj
    self.screen = WinLostScreen(self.screen_size, complete)
    self.screen.event_back_menu = lambda obj: self.backto_menu(obj)
    self.screen.event_continue_game = lambda obj: self.event_continue_game(complete)

  def event_continue_game(self, obj):
    level.index_level += 1 if obj else 0
    self.start_game()

  def set_screen_size(self, obj):
    self.screen_size = obj
    self.root = pg.display.set_mode(self.screen_size)
    self.screen.screen_resize(self.screen_size)
    self.menu.screen_resize(self.screen_size)

  def backto_menu(self, obj):
    self.screen = self.menu


app = App("Game xếp hình", level.current_size)
app.run()
