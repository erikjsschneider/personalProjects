import sys

from treehouse.animated import AnimatedGIF
from tkinter import *


def button1():
    novi = Toplevel(bg='peach puff')
    canvas = Canvas(novi, width=600, height=500, bg='peach puff')
    canvas.pack(expand=True, fill=BOTH)
    canvas.create_text(300, 25, text='Happy Birthday, Emily!', font='Verdana 24 bold')
    gif1 = PhotoImage(file='catBalloons.gif')
    canvas.create_image(300, 175, image=gif1)
    canvas.gif1 = gif1
    canvas.create_text(250, 375,
                       text='''
                       This may feel like just another day to you, 
                       but it is much more than that. You are an  
                       amazing woman, wife, and soon-to-be-mother 
                       of our twin children. Without you, my life would be  
                       less enjoyable, and less prosperous. You  
                       push me to be better, and I am stronger because of 
                       that. I love you with all my heart, Emily, 
                       and I can't wait to welcome Gabe and Lily with you. =)''',
                       font='Verdana 10', justify='center')
    button3 = Button(novi, text='Thanks!', command=mGui.destroy, height=2, width=10).pack()


mGui = Tk()
button1 = Button(mGui, text='Open', command=button1, height=3, width=15, fg='deep pink', bg='light sky blue',
                 font='Times 18 bold').pack()
button2 = Button(mGui, text='Fin', command=mGui.destroy, height=2, width=20, fg='light sky blue', bg='deep pink',
                 font='Times 12 italic').pack()

mGui.mainloop()
