import os
import pygame as pg
import random, cv2 as cv, time, pickle
from PIL import Image, ImageFilter
from tkinter.messagebox import *
#Định nghĩa các hằng số

SCREEN_SIZE = 640,360
DEFAULT_SIZE = 50,50
BUTTON_SIZE = 80,40
ZERO_P = 0.0,0.0
BLACK = 0,0,0
WHITE = 255,255,255
GRAY = 200,200,200
FPS_TICK=60
RED = 155,0,0
GREEN = 0,155,0
BLUE = 0,0,255
FONT_SIZE = 20
FONT_SVN_RETRON = "src/font/SVN-Retron 2000.otf"
FONT_PADDING_TOP = -4
TEXT_COLOR = 220,220,220
MENU_PADDING = 10,4
BOARD_SCALE = 0.45, 0.7
IMG_BOARD_DEMO = 0.1
PADDING_IMG = 2
BUTTON_WARD_SCALE = 0.05
RANDOM_MARGIN = 50
RADIUS_BLUR = 10

#Hàm Half_size lấy một nữa kích thước ví dụ In[(10, 8)] -> Out[(5,4)] 
def Half_size(size: tuple):
  return size[0] // 2, size[1] // 2

#Hàm trả về giá trị lớn nhất trong một mảng
def Max(array):
  i_max = 0 #đánh dấu max
  for i in range(len(array)):
    if array[i] > array[i_max]: #nếu lớn hơn max
      i_max = i
  return array[i_max]

#Tính tổng các phần tử trong mảng
def Sum(array):
  sum = 0
  for i in range(len(array)):
    sum += array[i]
  return sum

def catdeuheso(size, heso):
  return size[0] - (size[0]%heso[0]), size[1] - (size[1]%heso[1])

#Float to int 2d
def f2i(float):
  return int(float[0]), int(float[1])

def cong2d(tuple1:tuple, tuple2:tuple):
  return f2i((tuple1[0] + tuple2[0], tuple1[1] + tuple2[1]))

def tru2d(tuple1:tuple, tuple2:tuple):
  return f2i((tuple1[0] - tuple2[0], tuple1[1] - tuple2[1]))

def nhan2d(tuple1:tuple, tuple2:tuple):
  return f2i((tuple1[0] * tuple2[0], tuple1[1] * tuple2[1]))

def nhan2d_hs(tuple1:tuple, thua_so:int):
  return f2i((tuple1[0] * thua_so, tuple1[1] * thua_so))

def abs(num):
  return num * -1 if num < 0 else 1

def absolute_2d(tuple1:tuple):
  return f2i([abs(p) for p in tuple1])

#trả về kích thước mới vừa với kích thước board
def scale_size_to_fit(size:tuple, board_size:tuple):
  abs_size = absolute_2d(tru2d(size, board_size))
  index_min = 0 if abs_size[0] < abs_size[1] else 1
  hsboard_size = board_size[index_min] / size[index_min]
  return nhan2d_hs(size, hsboard_size)

from level import *

level = Levelpk()
level.read_level()
level.index_level = 0

# print(level.current_level)
