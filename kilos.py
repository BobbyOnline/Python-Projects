import tkinter as tk

import ttkbootstrap as ttk
def convert():
    mile_input = entry_Int.get()
    kilo_output = mile_input * 1.61
   
    output_string.set(kilo_output)
#window code

window = ttk.Window(themename = 'darkly' )
window.title('Kilos Demo')
window.geometry('300x150')

#title
title_label = ttk.Label(master = window, text = 'Miles to Kilometers', font = 'Comicsans 24')
title_label.pack()


#input field
input_frame = ttk.Frame(master = window)
entry_Int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_Int)
button = ttk.Button(master = input_frame, text = 'Convert' , command = convert)
entry.pack(side = 'left' , padx = 15)
button.pack(side = 'left')
input_frame.pack(pady = 10)


#output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = 'output' , font = 'Comicsans 24', textvariable = output_string)
output_label.pack(pady = 10)


window.mainloop()
