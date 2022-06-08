# Importing the Required Modules
from tkinter import * 
import webbrowser
from time import sleep
import os 
import pyautogui as py
from time import sleep
from PIL import ImageTk, Image
import cv2 
import threading
import random

import assign
import compUsage
import freeTime
import improve
import office
import study

#button1
def clearbin():
   compUsage.clearRecycleBin()
   l4.configure(text = "Deleted all files in Recycle bin !")


#button2
def tasknotify():
   def save():
     assign.tasker(site.get(), info.get())
     l4.configure(text= "Added the Task Successfully !")   
     login.destroy()  
   login = Toplevel(root)
   login.title("Enter Task Info")
   login.geometry("500x230")
   login.configure(bg="light blue")
   site = StringVar()
   info = StringVar()
   Label(login, text=" Enter Task Info ", font = ('Times','20'), fg="Green",anchor='e').pack()
   Label(login, text="Site : ", font=(None,10,'bold')).place(x=50,y=80)
   Label(login, text="Info : ", font=(None,10,'bold')).place(x=50,y=120)
   site1 = Entry(login, width=20,textvariable = site, font=('Verdana',12)).place(x=150, y=80)
   info1 = Entry(login, width=20,textvariable = info, font=('Verdana',12)).place(x=150, y=120)
   Button(login , text="Add Task", bd = 5, activebackground = 'yellow', command = save, bg='light yellow').place(x=200,y=170)

#button4
def sorter():
   def save():
     compUsage.sortAndstoreFiles(path.get())
     l4.configure(text= "Sorted and stored all Files !")   
     login.destroy()

   login = Toplevel(root)
   login.title("Files Sorter")
   login.geometry("500x200")
   login.configure(bg="light blue")
   path = StringVar()
   Label(login, text=" Enter Path of Folder ", font = ('Times','20'), fg="Green",anchor='e').pack()
   Label(login, text="Folder Path : ", font=(None,10,'bold')).place(x=50,y=80)
   site1 = Entry(login, width=20,textvariable = path, font=('Verdana',12)).place(x=190, y=80)
   Button(login , text="Sort Files", bd = 5, activebackground = 'yellow', command = save, bg='light yellow').place(x=200,y=130)

#button6
def shortener():
   def save():
     res = compUsage.shorten(link.get())
     l4.configure(text= res)   
     login.destroy()  
   login = Toplevel(root)
   login.title("URL Shortener")
   login.geometry("500x200")
   login.configure(bg="light blue")
   link = StringVar()
   Label(login, text=" Enter Link to shorten ", font = ('Times','20'), fg="Green",anchor='e').pack()
   Label(login, text="Link : ", font=(None,10,'bold')).place(x=50,y=80)
   site1 = Entry(login, width=20,textvariable = link, font=('Verdana',12)).place(x=170, y=80)
   Button(login , text="Shorten", bd = 5, activebackground = 'yellow', command = save, bg='light yellow').place(x=200,y=130)


########################################################################################
  
#help-menu
def helpmenu():
   help = Toplevel(root)
   help.geometry("620x300")
   help.title("Help Window")
   Label(help, text=" Help Window", font = ('Times','20'), fg="Green",anchor='e').pack()
   Label(help, text="\n1) Install all the Required modules from requirements.txt file", font = ('Times','13')).pack()
   Label(help, text="\n2) Then run the main file app.py to run the desktop app", font = ('Times','13')).pack()
   Label(help, text="\n3) Then click on the button you want to use !", font=('Times', '13')).pack()
 
#about-menu
def aboutmenu():
   about = Toplevel(root)
   about.title("About")
   about.geometry("550x300")
   
   Label(about, text=" About Study Tool", font = ('Times','20'), fg="Green",anchor='e').pack()
   Label(about, text="\n\t", font=('Times',14)).pack()


############################################################################################################
     
# root widget 
root = Tk()  
 
root.title(" Study Tool") 
root.geometry('720x640')
root.configure(bg="light blue")
 
str1 = StringVar()
int1 = IntVar()

# Adding menu
menubar = Menu(root)
home = Menu(menubar, tearoff=0)
menubar.add_cascade(label='Home', menu= home)

about = Menu(menubar, tearoff=0)
menubar.add_cascade(label='About', menu = about)
about.add_command(label="About",command=aboutmenu)

help = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu = help)
help.add_command(label="Help", command=helpmenu)

l1 = Label(root, text=" Welcome to Study Tool ! ", font = ('Times','22'), fg="Green",anchor='e').pack()

#info-message
l4 = Label(root , text="", font=('Times',15), fg="Green")
l4.place(x=5, y=70) 

#images to be added on buttons
photo1 = ImageTk.PhotoImage(Image.open("images\\1.png"))
photo2 = ImageTk.PhotoImage(Image.open("images\\2.png")) 
photo3 = ImageTk.PhotoImage(Image.open("images\\3.png"))
photo4 = ImageTk.PhotoImage(Image.open("images\\4.png"))
photo5 = ImageTk.PhotoImage(Image.open("images\\5.png")) 
photo6 = ImageTk.PhotoImage(Image.open("images\\6.png")) 

#x-gap = 200 for buttons

btn1 = Button(root , image = photo1, bd = 5,activebackground = 'light green',height=120,width=120, command=clearbin)
btn1.image = photo1
btn1.place(x=80,y=130)

cmd1 = Label(root , text="Trash Cleaner", font=(None,11))
cmd1.place(x='80',y='270')

btn2 = Button(root , image = photo5, bd = 5,activebackground = 'light green', height=120,width=120, command=tasknotify)
btn2.image = photo5
btn2.place(x=280,y=130)

cmd2 = Label(root , text="Task Notifier", font=(None,11))
cmd2.place(x='295',y='270')

btn3 = Button(root , image = photo3, bd = 5,activebackground = 'light green',height=120,width=120)
btn3.image = photo3
btn3.place(x=480,y=130)

cmd3 = Label(root , text="PDF Creator", font=(None,11))
cmd3.place(x='490',y='270')

## ---------------------------------------------------------------------------------------

btn4 = Button(root , image = photo4, bd = 5,activebackground = 'light green',height=120,width=120, command=sorter)
btn4.image = photo4
btn4.place(x=80,y=340)

cmd4 = Label(root , text="Sort & Store Files", font=(None,11))
cmd4.place(x='80',y='480')

btn5 = Button(root , image = photo2, bd = 5,activebackground = 'light green', height=120,width=120)
btn5.image = photo2
btn5.place(x=280,y=340)

cmd5 = Label(root , text="PDF to DOCX", font=(None,11))
cmd5.place(x='290',y='480')

btn6 = Button(root , image = photo6, bd = 5,activebackground = 'light green',height=120,width=120, command=shortener)
btn6.image = photo6
btn6.place(x=480,y=340)

cmd6 = Label(root , text="URL Shortener", font=(None,11))
cmd6.place(x='490',y='480')

## ----------------------------------------------------------------------------------------------

belbut2 = Button(root , text="Close the App", bd = 5, activebackground = 'yellow',command = root.destroy, bg='light yellow')
belbut2.place(x='580',y='550')

#######################################################################################################

root.config(menu = menubar) 
root.mainloop()

'''
1. task-notifier
2. recycle-bin cleaner
3. sort and store files
4. url shortener
5. pdf creator
6. pdf to docx

'''
