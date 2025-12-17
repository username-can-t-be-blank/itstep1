import tkinter
screen = tkinter.Tk()
can = tkinter.Canvas(screen)
can.pack()
can['width'] = 500
can['height'] = 500

def draw(sur):
    can.create_oval(sur.x-10, sur.y-10, sur.x+10, sur.y+10)

can.bind("<Button-1>", draw)
screen.mainloop()