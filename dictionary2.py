#-------------------------------------------------------------------------------
# Name:        dictionary app
# Purpose:      self-study
#
# Author:      Hata
#
# Created:     18/10/2018
# Copyright:   (c) Hata 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import*
import tkinter
import tkinter.messagebox


g = open('mydata.txt', encoding="utf-8")

x=g.read()
import ast
z=ast.literal_eval(x)
database=z


def add():
    word = Entry.get(entry_a)
    mean = Entry.get(entry_b)
    text.delete(1.0,END)
    data1 = { word : mean }
    display= "Added: " + "[" +word + ": " + mean + "]"
    text.insert(END,display)
    text.see(END)

    global database
    data=dict(database, **data1)
    database=data
    new_data=str(data)
##    print(new_data)
    f=open('mydata.txt', 'w+')
    f.write(new_data)
    f.close()

def find():
    word = Entry.get(entry_a)
    text.delete(1.0,END)
    global database
    if word in database:
        display= "Found it: [ %s, %s] " % (word, database[word])
        text.insert(END,display)
        text.see(END)

    else:
        display= "Cannot find this word: [ %s ] " % word

        text.insert(END,display)
        text.see(END)


def delete():
    word=Entry.get(entry_a)
    text.delete(1.0,END)
    global database
    if word in database:

        del database[word]
        display= "Deleted: [ %s ] " % (word, database[word])

        text.insert(END,display)
        text.see(END)

        data=database
        new_data=str(data)
##        print(new_data)
        f=open('mydata.txt', 'w+')
        f.write(new_data)
        f.close()
    else:

        display= "Cannot find this word: [ %s ] " % word
        text.insert(END,display)
        text.see(END)


def view_all():

    global database
    text.delete(1.0,END)

    if tkinter.messagebox.askokcancel('View all', 'Do you want to view all words?'):

        for word, mean in database.items():
            top="[ %s, %s] " % (word, database[word]) + '\n'
            text.insert(END, top)
            text.see(END)



def stop():
    if tkinter.messagebox.askokcancel('Exit', 'Are you sure you want to exit?'):
       tkinter.messagebox.showinfo('Bye', 'See you again')
       my_window.destroy()




my_window= Tk()
my_window.title("Eng-Bul App - @Hata")

width_of_window=800
height_of_window=680
screen_width=my_window.winfo_screenwidth()
screen_height=my_window.winfo_screenheight()
x_coordinate = (screen_width/2) - (width_of_window/2)
y_coordinate = (screen_height/2) - (height_of_window/2)

my_window.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))


## {Full screen

##width_value = my_window.winfo_screenwidth()
##height_value = my_window.winfo_screenheight()
##
##
##my_window.geometry("%dx%d+0+0" % (width_value, height_value))}

##my_window.configure(background="#aebd91")

label1= Label(my_window,text="ENGLISH - BULGARIAN DICTIONARY",
              fg="red",
              font="Times 20",
              height=2)


label_a= Label(my_window,text="Enter a word*:",
               fg="black",
               font="Times 18",
               height=2,
               justify=LEFT)

label_b= Label(my_window,text="Enter the meaning:",
               fg="black",
               font="Times 18",
               height=2,
               justify=LEFT)

label_c= Label(my_window,text="Result:",
               fg="black",
               font="Times 18",
               height=2,
               justify=LEFT)

label_d= Label(my_window,
            fg="blue",
            font="Times 18",
            width=30,
            height=5)




label2= Label(my_window,text="Press the buttons to select your choice:",
              fg="black",
              font="Times 18",
              width=30,
              height=2)


entry_a = Entry(my_window, bg="#aebd91", font="Times 18", width=15)
entry_b = Entry(my_window, bg="#aebd91", font="Times 18", width=15)
##entry_c = Entry(my_window, bg="#aebd91", font="Times 18", width=30)

button1= Button(my_window,text="Add", bg="#aebd91", fg="blue", font="Times 18", width=15, command=add)
button2= Button(my_window,text="Find", bg="#aebd91", fg="blue", font="Times 18",width=15, command=find)
button3= Button(my_window,text="Delete", bg="#aebd91", fg="blue", font="Times 18",width=15, command=delete)
button4= Button(my_window,text="View", bg="#aebd91", fg="blue", font="Times 18",width=15, command=view_all)
button5= Button(my_window,text="Exit", bg="#aebd91", fg="blue", font="Times 18",width=15, command=stop)

label1.grid(row=0,column=1)

label_a.grid(row=1,column=0)
label_b.grid(row=2,column=0)
label_c.grid(row=6,column=0)
label_d.grid(row=11,column=1)

entry_a.grid(row=1,column=1)
entry_b.grid(row=2,column=1)


label2.grid(row=3,column=1)

button1.grid(row=4,column=0)
button2.grid(row=4,column=1)
button3.grid(row=5,column=0)
button4.grid(row=5,column=1)
button5.grid(row=10,column=1)

text= Text(my_window,
              fg="black",
              font="Times 18",
              width=30,
              height=8)
text.grid(row=6,column=1)



entry_a.focus()

my_window.mainloop()


#
