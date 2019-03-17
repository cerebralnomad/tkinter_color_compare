#! /usr/bin/env python3.6

import tkinter as tk
import tkinter.ttk as ttk
from ColorList import color_list

def ChangeColor():
    
    box1_color_var = b1color_choice.get()
    box2_color_var = b2color_choice.get()
    box3_color_var = b3color_choice.get()
    box4_color_var = b4color_choice.get()
    box1_bg = box1_color_var
    box2_bg = box2_color_var
    box3_bg = box3_color_var
    box4_bg = box4_color_var
    box1.configure(background = box1_bg)
    box2.configure(background = box2_bg)
    box3.configure(background = box3_bg)
    box4.configure(background = box4_bg)

    #frame.configure(background = bg_color)
    #color_label.configure(text = bg_color)
    #color_entered.delete(0, 'end') 

bg_color = 'moccasin'

root = tk.Tk()
root.geometry('%sx%s' % (400, 500))
root.title("Color Compare for Tkinter on Ubuntu")
root.configure(background = 'slate grey')

frame = tk.LabelFrame(root)
frame.configure(background = bg_color)
frame.pack(fill = 'both', expand = True, side = 'top')
frame.rowconfigure(0, weight = 1)
frame.rowconfigure(1, weight = 1)
frame.columnconfigure(0, weight = 1)
frame.columnconfigure(1, weight = 1)

box1_bg = 'red'
box1 = tk.Label(frame)
box1.configure(background = box1_bg)
box1.grid(row = 0, column = 0, sticky = 'news')

box2_bg = 'blue'
box2 = tk.Label(frame)
box2.configure(background = box2_bg)
box2.grid(row = 0, column = 1, sticky = 'news')

box3_bg = 'green'
box3 = tk.Label(frame)
box3.configure(background = box3_bg)
box3.grid(row = 1, column = 0, sticky = 'news')

box4_bg = 'yellow'
box4 = tk.Label(frame)
box4.configure(background = box4_bg)
box4.grid(row = 1, column = 1, sticky = 'news')

bot_frame = tk.LabelFrame(root)
bot_frame.configure(background = 'grey')
bot_frame.pack(fill = 'x', side = 'bottom')
bot_frame.rowconfigure(0, weight = 1)
bot_frame.rowconfigure(1, weight = 1)
bot_frame.rowconfigure(2, weight = 1)
bot_frame.rowconfigure(3, weight = 1)
bot_frame.rowconfigure(4, weight = 1)
bot_frame.columnconfigure(0, weight = 1)
bot_frame.columnconfigure(1, weight = 1)

#color_label = tk.Label(frame, text = bg_color)
#color_label.pack(pady = 50, side = 'top')

b1_label = tk.Label(bot_frame, text = 'Top Left Color')
b1_label.configure(background = 'grey')
b1_label.grid(row = 0, column = 0, pady = (3, 0))

b1color = tk.StringVar()
b1color_choice = ttk.Combobox(bot_frame, width = 20, textvariable = b1color)
b1color_choice['values'] = color_list
b1color_choice.current(451)
b1color_choice.grid(row = 0, column = 1, pady = (3, 0))

b2_label = tk.Label(bot_frame, text = 'Top Right Color')
b2_label.configure(background = 'grey')
b2_label.grid(row = 1, column = 0, pady = (3, 0))

b2color = tk.StringVar()
b2color_choice = ttk.Combobox(bot_frame, width = 20, textvariable = b2color)
b2color_choice['values'] = color_list
b2color_choice.current(24)
b2color_choice.grid(row = 1, column = 1, pady = (3, 0))

b3_label = tk.Label(bot_frame, text = 'Bottom Left Color')
b3_label.configure(background = 'grey')
b3_label.grid(row = 2, column = 0, pady = (3, 0))

b3color = tk.StringVar()
b3color_choice = ttk.Combobox(bot_frame, width = 20, textvariable = b3color)
b3color_choice['values'] = color_list
b3color_choice.current(255)
b3color_choice.grid(row = 2, column = 1, pady = (3, 0))

b4_label = tk.Label(bot_frame, text = 'Bottom Right Color')
b4_label.configure(background = 'grey')
b4_label.grid(row = 3, column = 0, pady = (3, 0))

b4color = tk.StringVar()
b4color_choice = ttk.Combobox(bot_frame, width = 20, textvariable = b4color)
b4color_choice['values'] = color_list
b4color_choice.current(552)
b4color_choice.grid(row = 3, column = 1, pady = (3, 0))

c_button = tk.Button(bot_frame, text = 'Change Colors', command = ChangeColor,
    background = '#48483E', foreground = '#CFD0C2')
c_button.grid(row = 4, column = 0, padx = 5, pady = 10, sticky = 'w')
button = tk.Button(bot_frame, text = 'Exit', command = root.destroy,
    background = '#48483E', foreground = '#CFD0C2')
button.grid(row = 4, column = 1, padx = 5, pady = 10, sticky = 'e')

root.mainloop()