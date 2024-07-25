import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter.messagebox import *
from PIL import ImageTk, Image
from level import *

level = Levelpk()
level.read_level()
# Tạo cửa sổ giao diện
window = tk.Tk()
window.geometry("700x400")
window.title("Edit Level")
window.resizable(False, False)

font ="Arial 14"
font2 ="Arial 15"
font3 ="Arial 16"

image = None
tkimage = None
current_index = 0

def browse_file():
  global image, tkimage
  file_path = filedialog.askopenfilename(filetypes=(("PNG files", "*.png"), ("All files", "*.*")))
  if file_path:
    image = Image.open(file_path)
    img = image.resize((photo_image.winfo_width(), photo_image.winfo_height()))
    tkimage = ImageTk.PhotoImage(img)
    photo_image.config(image=tkimage)
    size_label["text"] = f"Size: {image.size[0]}x{image.size[1]}"
    img_mode_label["text"] = "Mode: " + image.mode

# Label "Xin chao"
title_label = tk.Label(window, font=font, text="Tùy chỉnh level")
title_label.place(relx=0.4, rely=0, relwidth=0.6, relheight=0.1)

# Listbox danh sách level
level_listbox = tk.Listbox(window, font=font)
level_listbox.place(relx=0, rely=0, relwidth=0.4, relheight=1)

# Textbox nhập photo image
photo_image = ttk.Label(window, background="#ffffff")
photo_image.place(relx=0.4, rely=0.1, relwidth=0.2, relheight=0.3)

# Textbox nhập photo image
photo_image_bt = tk.Button(window, font=font3, text="Tải ảnh", command=browse_file)
photo_image_bt.place(relx=0.6, rely=0.1, relwidth=0.15, relheight=0.1)

# Label "Hien size"
size_label = tk.Label(window, font=font, text="Size:")
size_label.place(relx=0.75, rely=0.1, relwidth=0.25, relheight=0.15)

# Label "Img mode"
img_mode_label = tk.Label(window, font=font, text="Mode:")
img_mode_label.place(relx=0.75, rely=0.25, relwidth=0.25, relheight=0.15)

# Textbox nhập level name
level_name_label = tk.Label(window, font=font, text="Tên Level:")
level_name_label.place(relx=0.4, rely=0.4, relwidth=0.2, relheight=0.1)
level_name_entry = tk.Entry(window, font=font2)
level_name_entry.place(relx=0.6, rely=0.4, relwidth=0.4, relheight=0.1)

# Combobox true/false
lock_label = tk.Label(window, font=font, text="Locked:")
lock_label.place(relx=0.4, rely=0.5, relwidth=0.2, relheight=0.1)
lock_combobox = ttk.Combobox(window, values=["True", "False"], font=font2)
lock_combobox.place(relx=0.6, rely=0.5, relwidth=0.2, relheight=0.1)


# Textbox nhập img mode
rc_label = tk.Label(window, font=font, text="Hàng x cột:")
rc_label.place(relx=0.4, rely=0.6, relwidth=0.2, relheight=0.1)

# Textbox nhập int value 1
row_entry = tk.Entry(window, font=font2)
row_entry.place(relx=0.6, rely=0.6, relwidth=0.1, relheight=0.1)

x_label = tk.Label(window, font=font, text="X")
x_label.place(relx=0.7, rely=0.6, relwidth=0.1, relheight=0.1)

# Textbox nhập int value 2
col_entry = tk.Entry(window, font=font2)
col_entry.place(relx=0.8, rely=0.6, relwidth=0.1, relheight=0.1)


# Label countdown tính bằngg giây
cd_label = tk.Label(window, font=font, text="Đếm ngược (giây):")
cd_label.place(relx=0.4, rely=0.7, relwidth=0.3, relheight=0.1)

# Textbox nhập int countdown tính bằngg giây
cd_entry = tk.Entry(window, font=font2)
cd_entry.place(relx=0.7, rely=0.7, relwidth=0.1, relheight=0.1)

def update_listbox():
  level_listbox.delete(0, tk.END)
  for i in level.game_data:
    level_listbox.insert(tk.END, i.name)
    
update_listbox()

def item_selected(event):
  global image, tkimage, current_index
  # Lấy chỉ mục của mục được chọn
  if level_listbox.curselection() == ():
    return
  
  selected_index = level_listbox.curselection()[0]
  current_index = selected_index
  data = level.game_data[selected_index]
  image = data.img2Image()
  img = image.resize((photo_image.winfo_width(), photo_image.winfo_height()))
  tkimage = ImageTk.PhotoImage(img)

  photo_image.config(image=tkimage)

  size_label["text"] = f"Size: {data.size[0]}x{data.size[1]}"
  img_mode_label["text"] = "Mode: " + data.mode

  level_name_entry.delete(0, tk.END)  
  level_name_entry.insert(0, data.name)
  
  lock_combobox.set("True" if data.locked else "False")
  row_entry.delete(0, tk.END)
  col_entry.delete(0, tk.END)

  row_entry.insert(0, data.matrix[0])
  col_entry.insert(0, data.matrix[1])

  cd_entry.delete(0, tk.END)
  cd_entry.insert(0, data.countdown)

def update_level(event):
  global image, tkimage, current_index
  
  data = Lv()
  try:
    data.mode = image.mode
    data.size = image.size
    data.setImage(image)
    data.name = level_name_entry.get()
    data.locked = True if lock_combobox.get() == "True" else False
    data.matrix = [int(row_entry.get()), int(col_entry.get())]
    data.countdown = int(cd_entry.get())
  except:
    print("Lỗi trong quá trình update")
    return
  level.game_data[current_index] = data

  showinfo("Thông báo", f"Sửa đổi {current_index} thành công")
  update_listbox()

def delete_level(event):
  global image, tkimage, current_index
  data = level.game_data.pop(current_index)
  print("đã xóa level", data.name)

  showinfo("Thông báo", f"Đã xóa {data.name} thành công")
  update_listbox()

def add_level(event):
  data = Lv()
  try:
    data.size = image.size
    data.mode = image.mode
    data.setImage(image)
    data.name = level_name_entry.get()
    data.locked = True if lock_combobox.get() == "True" else False
    data.matrix = [int(row_entry.get()), int(col_entry.get())]
    data.countdown = int(cd_entry.get())
  except:
    print("Lỗi trong quá trình update")
    return
  level.game_data.append(data)

  update_listbox()

def save_level(event):

  try:
    level.write_level()
    showinfo("Thông báo", "Lưu thành công")
  except:
    print("Lỗi trong quá trình update")
    return


# Button thêm level
add_button = tk.Button(window, font=font3, text="Thêm", command=lambda: add_level(add_button))
add_button.place(relx=0.4, rely=0.85, relwidth=0.15, relheight=0.1)

# Button xóa level
delete_button = tk.Button(window, font=font3, text="Xóa", command=lambda: delete_level(delete_button))
delete_button.place(relx=0.55, rely=0.85, relwidth=0.15, relheight=0.1)

# Button sửa level
update_button = tk.Button(window, font=font3, text="Sửa", command=lambda: update_level(save_button))
update_button.place(relx=0.7, rely=0.85, relwidth=0.15, relheight=0.1)

save_button = tk.Button(window, font=font3, text="Lưu", command=lambda: save_level(save_button))
save_button.place(relx=0.85, rely=0.85, relwidth=0.15, relheight=0.1)

# Gắn sự kiện khi người dùng nhấn vào mục trong Listbox
level_listbox.bind("<<ListboxSelect>>", item_selected)


window.mainloop()