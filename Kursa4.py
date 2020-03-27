from tkinter import *
from tkinter import font as tkFont
def func():
    pass
    
def create_window_about_us():
    window1 = Toplevel(window)
    window1.geometry('400x100')
    w = Label(window1, text="Just about us" ,font=helv36)
    w.pack()
    button_quit = Button(window1, width = 20, text="Quit", command=window1.destroy , font=helv35)
    button_quit.place(relx=0.5, rely=0.88, anchor=CENTER)


    
window = Tk()

window.configure(background="green")
window.title("TIMSnNM")
window.geometry('800x500')
window.resizable(False,False)
helv36 = tkFont.Font(family='Helvetica', size=24, weight=tkFont.BOLD)
helv35 = tkFont.Font(family='Helvetica', size=10, weight=tkFont.BOLD)



button_continuous = Button(window, width = 20, text="Continuous", command=func, font=helv36)
button_discrete = Button(window, width = 20, text="Discrete", command=func , font=helv36)
button_methog_simple_iteration = Button(window, width = 20, text="Methon simple iteration", command=func , font=helv36 )
button_newton_zeydel_iteration = Button(window, width = 20, text="Newton-Zeydel iteration", command=func, font=helv36)
button_about_us = Button(window, text="About us", width = 20, command=create_window_about_us , font=helv36)
button_quit = Button(window, width = 20, text="Quit", command=window.destroy , font=helv36)

button_continuous.place(relx=0.5, rely=0.08, anchor=CENTER)
button_discrete.place(relx=0.5, rely=0.24, anchor=CENTER)
button_methog_simple_iteration.place(relx=0.5, rely=0.4, anchor=CENTER)
button_newton_zeydel_iteration.place(relx=0.5, rely=0.56, anchor=CENTER)
button_about_us.place(relx=0.5, rely=0.72, anchor=CENTER)
button_quit.place(relx=0.5, rely=0.88, anchor=CENTER)

window.mainloop()   
