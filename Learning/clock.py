from operator import truediv
from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("Clock")
root.configure(background="black")
screen_width = int(root.winfo_screenwidth()/4)
screen_height = int(root.winfo_screenheight()/4)
root.geometry("{}x{}".format(screen_width,screen_height))

def time():

    sec = int(strftime("%S"))
    if ((sec%2)==0):
        root.title("Clock")
    else:
    
        root.title('Clock             by Gazstao')
    
    string = strftime('%H:%M:%S\n%D')    
    lbl.config(text = string)
    lbl.after(1000,time)


lbl = Label(root, font=('calibri', 40, 'bold'), background='black', foreground='slategrey')
lbl.pack(expand = True)

time()

mainloop()
