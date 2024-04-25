from tkinter import Tk, Text, Menu


window = Tk()
window.title('Note pad')
text_area = Text(window, font="Arial 20 bold")
text_area.pack()
window.mainloop()
