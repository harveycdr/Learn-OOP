from PIL import Image
import base64, json, os, pickle
import pygame as pg

# def ImgToBase64(image):
#   # Chuyển đổi ảnh thành chuỗi dữ liệu nhị phân
#   try:
#     # Chuyển đổi ảnh thành chuỗi dữ liệu nhị phân
#     str = base64.b64encode(image.tobytes()).decode("utf-8")
#     return str, image.size, image.mode
#   except:
#     print("Không thể chuyển đổi ảnh thành bytes")

#     return None
  
# def SufToBase64(sface, mode):
#   try:
#     surface_bytes = pg.image.tostring(sface, mode)
#     # Chuyển đổi ảnh thành chuỗi dữ liệu nhị phân
#     str = base64.b64encode(surface_bytes).decode("utf-8")
#     return str, sface.get_size(), mode
#   except:
#     print("Không thể chuyển đổi surface thành bytes")
  
# def Base64ToBytes(str):
#   # Giải mã chuỗi dữ liệu ảnh từ Base64
#   bytes = base64.b64decode(str)
#   # # Tạo lại đối tượng hình ảnh từ dữ liệu nhị phân
#   # image = Image.frombytes("RGB", (width, height), bytes)
#   return bytes

def BytesToSurface(bytes, size, mode):
  # Create a Pygame surface from the bytes data
  surface = pg.image.fromstring(bytes, size, mode)
  return surface

def BytesToImage(bytes, size, mode):
  # Create a Pygame image from the bytes data
  image = Image.frombytes(mode, size, bytes)
  return image

class Lv:
  def __init__(self) -> None:
    self.img = None
    self.size = (0,0)
    self.mode = 'RGBA'
    self.name = ""
    self.matrix = (0,0)
    self.locked = False
    self.countdown = 60 #second

  def img2sface(self):
    surface = pg.image.fromstring(self.img, self.size, self.mode)
    return surface
  
  def img2Image(self):
    image = Image.frombytes(self.mode, self.size, self.img)
    return image
  
  def setImage(self, image):
    self.img = image.tobytes()

  def setSface(self, sface):
    self.img = pg.image.tostring(sface, self.mode)

class Levelpk:
  def __init__(self) -> None:
    self.index_level = 0
    self.current_level = 0
    self.current_size = (640,360)
    self.game_data = []

  def is_endlevel(self):
    return True if self.index_level >= len(self.game_data) else False
  
  def unlock_curr_level(self):
    self.game_data[self.index_level].locked = True
    self.write_level()
  
  def read_level(self):
    # read game data
    try:
      with open('game.data', 'rb') as file:
        bien = pickle.load(file)
        self.index_level = bien.index_level
        self.current_size = bien.current_size
        self.current_level = bien.current_level
        self.game_data = bien.game_data
      print("Đọc dữ liệu game thành công")

    except Exception as ex:
      print("Đọc dữ liệu game thất bại", ex)

  def get_level(self):
    return self.game_data[self.index_level]
  
  def write_level(self):
    with open('game.data', 'wb') as file:
      bien = Levelpk()
      bien.index_level = self.index_level
      bien.current_size = self.current_size
      bien.game_data = self.game_data
      bien.current_level = self.current_level
      pickle.dump(bien, file)
      print("Lưu game thành công")
