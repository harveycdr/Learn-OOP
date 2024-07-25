from package.setting import *
from package.widget import *

class Photo(widget):
  def __init__(self, sface: pg.surface.Surface = None, index=-1, fill=False) -> None:
    super().__init__()
    self.photo = None
    
    if sface is not None:
      self.photo = sface.copy() 
      self.sface = self.photo
      
    self.fill = fill
    self.link = None
    self.index = index

  def set_img(self, path_img):
    self.link = path_img
    self.photo = pg.image.load(path_img)
    self.sface = self.photo

  def scale_size(self, size):
    self.sface = pg.transform.scale(self.photo, size)
    