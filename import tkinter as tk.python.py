import tkinter as tk
from tkinter import messagebox
INITIAL_WIDTH = 400
INITIAL_HEIGHT = 400
def apply_options():
    """
    این تابع بر اساس وضعیت چک‌باکس‌ها، تغییرات لازم را اعمال می‌کند.
    """
    if double_size_var.get() == 1:
        new_width = INITIAL_WIDTH * 2
        new_height = INITIAL_HEIGHT * 2
        root.geometry(f"{new_width}x{new_height}")
    else:
        root.geometry(f"{INITIAL_WIDTH}x{INITIAL_HEIGHT}")
    if black_bg_var.get() == 1:
        root.config(bg="black")
    else:
        root.config(bg="SystemButtonFace") 
    if show_message_var.get() == 1:
        messagebox.showinfo("پیام", "سلام دنیا")
root = tk.Tk()
root.title("برنامه چک‌باکس‌ها")
root.geometry(f"{INITIAL_WIDTH}x{INITIAL_HEIGHT}")
double_size_var = tk.IntVar()
black_bg_var = tk.IntVar()
show_message_var = tk.IntVar()
chk_double_size = tk.Checkbutton(
    root,
    text="دو برابر کردن سایز پنجره (800x800)",
    variable=double_size_var,
    command=apply_options
)
chk_double_size.pack(pady=10, padx=10, anchor="w")
chk_black_bg = tk.Checkbutton(
    root,
    text="مشکی کردن پس‌زمینه",
    variable=black_bg_var,
    command=apply_options
)
chk_black_bg.pack(pady=5, padx=10, anchor="w")
chk_show_message = tk.Checkbutton(
    root,
    text="نمایش پیام 'سلام دنیا'",
    variable=show_message_var,
    command=apply_options 
)
chk_show_message.pack(pady=5, padx=10, anchor="w")
root.mainloop()