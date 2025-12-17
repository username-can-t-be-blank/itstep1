import tkinter
import random
screen = tkinter.Tk()
can = tkinter.Canvas(screen)
can.pack()
can['width'] = 500
can['height'] = 500

def draw(sur):
    r = random.randint(10, 30)
    can.create_oval(sur.x-r, sur.y-r, sur.x+r, sur.y+r)

can.bind("<B1-Motion>", draw)
screen.mainloop()