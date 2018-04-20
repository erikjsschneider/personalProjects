import sys

from treehouse.animated import AnimatedGIF
from tkinter import *


# def animate():
#     c.move(ball, 15, 0)
#     root.after(50, animate)
#
# root = Tk()
# c = Canvas(root, width=1000, height=1000)
# c.pack()
# ball = c.create_oval(0, 10, 100, 80)
# animate()
# root.mainloop()


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
    # button3.configure(height=5, width=10).pack(side=BOTTOM)


# def kill_button():
#     button3 = Button(text='Thanks!', command=mGui.destroy, height=5, width=10).pack()


mGui = Tk()
button1 = Button(mGui, text='Open', command=button1, height=3, width=15, fg='deep pink', bg='light sky blue',
                 font='Times 18 bold').pack()
button2 = Button(mGui, text='Fin', command=mGui.destroy, height=2, width=20, fg='light sky blue', bg='deep pink',
                 font='Times 12 italic').pack()

mGui.mainloop()

# class Application(Frame):
#     def __init__(self, master=None):
#         super().__init__(master)
#         self.pack()
#         self.create_widgets()
#
#     def create_widgets(self):
#         self.happy_bday = Button(self)
#         self.happy_bday["text"] = "Happy Birthday\n\n (click me)"
#         self.happy_bday["command"] = self.say_happy_bday
#         self.happy_bday.pack(side="top", expand=True)
#
#         self.quit = Button(self, text="I'm done", fg="dark red", command=root.destroy)
#         self.quit.pack(side="bottom", expand=True)
#
#     def say_happy_bday(self):
#         print("EMILY!")
#
# root = Tk()
# app = Application(master=root)
# app.mainloop()

# root = tkinter.Tk()
#
# happy_bday = tkinter.Label(
#     root,
#     text="Happy Birthday, Honey Bunny!!!",
#     bg="deep sky blue",
#     fg="deep pink",
#     font="ComicSans"
# )
#
# happy_bday.pack(fill=tkinter.BOTH, expand=True)
#
# my_name = tkinter.Label(root, text="You're turning 25 years old today!")
# my_name.pack()
#
# root.mainloop()

# class Birthday:
#     def __init__(self, master):
#         self.master = master
#         self.mainframe = tkinter.Frame(self.master, bg="dark slate gray")
#         self.mainframe.pack(fill=tkinter.BOTH, expand=True)
#
#         self.open_img = Image.open("Balloons.gif")
#
#         self.build_grid()
#         self.build_banner()
#         self.build_buttons()
#         self.build_balloons()
#         # self.load_gif()
#
#     def build_grid(self):
#         self.mainframe.columnconfigure(0, weight=1)
#         self.mainframe.rowconfigure(0, weight=0)
#         self.mainframe.rowconfigure(1, weight=1)
#         self.mainframe.rowconfigure(2, weight=0)
#
#     def build_banner(self):
#         banner = tkinter.Label(
#             self.mainframe,
#             bg="light sky blue",
#             text="HAPPY BIRTHDAY, EMILY!",
#             fg="deep pink",
#             font="Times 24 bold"
#         )
#         banner.grid(
#             row=0, column=0,
#             sticky="we",
#             padx=10, pady=10
#         )
#
#     def build_buttons(self):
#         buttons_frame = tkinter.Frame(self.mainframe)
#         buttons_frame.grid(row=2, column=0, sticky="nswe", padx=10, pady=10)
#         buttons_frame.columnconfigure(0, weight=1)
#
#         self.open_button = tkinter.Button(
#             buttons_frame,
#             text="Open"
#         )
#         self.open_button.grid(row=0, column=0, sticky="we")
#
#     def build_balloons(self):
#         label = tkinter.Label(
#             self.mainframe,
#             self.open_img
#         )
#         label.grid(
#             row=1, column=0,
#             sticky="we",
#             padx=10, pady=10
#         )
#
#     def load_gif(self):
#         Image.open("Balloons.gif")
#         self.loc = 0
#         self.frames = []
#
#     # def open_button(self):
#     #     self.
#
#
# if __name__ == '__main__':
#     root = tkinter.Tk()
#     # gif_balloons = tkinter.Label(root, compound="top")
#     # gif_balloons.balloons_gif = tkinter.PhotoImage(file="Balloons.gif")
#     Birthday(root)
#     root.mainloop()
