from tkinter import *
from PIL import Image, ImageTk

bg = '#FFEBCD'
btnBg = '#FFFAFA'
height = '600'
width = '900'

#creating the main window
root = Tk()
root.configure(background=bg)
root.geometry(width + "x" + height + "+100+50")
root.title("Произведения искусства")

score = 0
question= 'Как называется эта картина?'
def interface1():
    global question
    im2 = Image.open("9вал.jpg")
    im2 = ImageTk.PhotoImage(im2)
    im2_label = Label(image=im2)
    im2_label.image = im2
    im2_label.place(x=250, y=50)

    lab = Label(root, text=question, font="Arial 18", width=40, height=2, bg = '#FFEBCD')
    lab.pack()
    name = StringVar()
    ent_name = Entry(root, textvariable=name, width=80)
    ent_name.place(x=230, y=420)

    btn = Button(root, text="Далее", width=25, height=1,
                     font=("Helvetica", "18"), command=lambda: count())
    btn["bg"] = btnBg
    btn.place(x=300, y=500)

    def count():
        global score
        lab.pack_forget()
        btn.place_forget()
        im2_label.place_forget()
        ent_name.place_forget()
        search_word = name.get()
        if search_word == "Девятый вал" :
            score = score + 1
            interface2()
            return score
        else:
            interface2()


def interface2():
    global question
    im3 = Image.open("девушка.jpg")
    im3 = im3.resize((300, 330))
    im3 = ImageTk.PhotoImage(im3)
    im3_label = Label(image=im3)
    im3_label.image = im3
    im3_label.place(x=330, y=50)

    lab = Label(root, text=question, font="Arial 18", width=40, height=2, bg = '#FFEBCD')
    lab.pack()
    name = StringVar()
    ent_name = Entry(root, textvariable=name, width=80)
    ent_name.place(x=230, y=420)

    btn = Button(root, text="Далее", width=25, height=1,
                      font=("Helvetica", "18"),  command=lambda: count())
    btn["bg"] = btnBg
    btn.place(x=300, y=500)

    def count():
        global score
        lab.pack_forget()
        btn.place_forget()
        im3_label.place_forget()
        ent_name.place_forget()
        search_word = name.get()
        if search_word == "Девушка с жемчужной сережкой":
            score = score + 1
            interface4()
            return score
        else:
            interface4()

def interface4():
    global question
    im3 = Image.open("помпея.jpg")
    im3 = im3.resize((400, 300))
    im3 = ImageTk.PhotoImage(im3)
    im3_label = Label(image=im3)
    im3_label.image = im3
    im3_label.place(x=250, y=70)

    lab = Label(root, text=question, font="Arial 18", width=40, height=2, bg = '#FFEBCD')
    lab.pack()
    name = StringVar()
    ent_name = Entry(root, textvariable=name, width=80)
    ent_name.place(x=230, y=420)

    btn = Button(root, text="Далее", width=25, height=1,
                     font=("Helvetica", "18"), command=lambda: count())
    btn["bg"] = btnBg
    btn.place(x=300, y=500)

    def count():
        global score
        lab.pack_forget()
        btn.place_forget()
        im3_label.place_forget()
        ent_name.place_forget()
        search_word = name.get()
        if search_word == "Последний день Помпеи":
            score = score + 1
            interface3()
            return score
        else:
            interface3()

def interface3():
    global question
    im2 = Image.open("танец.jpg")
    im2 = ImageTk.PhotoImage(im2)
    im2_label = Label(image=im2)
    im2_label.image = im2
    im2_label.place(x=230, y=70)

    lab = Label(root, text=question, font="Arial 18", width=40, height=2, bg = '#FFEBCD')
    lab.pack()
    name = StringVar()
    ent_name = Entry(root, textvariable=name, width=80)
    ent_name.place(x=230, y=420)

    btn = Button(root, text="Далее", width=25, height=1,
                     font=("Helvetica", "18"), command=lambda: count())
    btn["bg"] = btnBg
    btn.place(x=300, y=500)

    def count():
        global score
        lab.pack_forget()
        btn.place_forget()
        im2_label.place_forget()
        ent_name.place_forget()
        search_word = name.get()
        if search_word == "Танец":
            score = score + 1
            interface5()
            return score
        else:
            interface5()

def interface5():
    global question
    im2 = Image.open("ночь.jpg")
    im2 = ImageTk.PhotoImage(im2)
    im2_label = Label(image=im2)
    im2_label.image = im2
    im2_label.place(x=250, y=60)

    lab = Label(root, text=question, font="Arial 18", width=40, height=2, bg = '#FFEBCD')
    lab.pack()
    name = StringVar()
    ent_name = Entry(root, textvariable=name, width=80)
    ent_name.place(x=230, y=420)

    btn = Button(root, text="Далее", width=25, height=1,
                     font=("Helvetica", "18"), command=lambda: count())
    btn["bg"] = btnBg
    btn.place(x=300, y=500)

    def count():
        global score
        lab.pack_forget()
        btn.place_forget()
        im2_label.place_forget()
        ent_name.place_forget()
        search_word = name.get()
        if search_word == "Звёздная ночь":
            score = score + 1
            interface6()
            return score
        else:
            interface6()

def interface6():
    global question
    im2 = Image.open("крик.jpg")
    im2 = im2.resize((300, 340))
    im2 = ImageTk.PhotoImage(im2)
    im2_label = Label(image=im2)
    im2_label.image = im2
    im2_label.place(x=300, y=50)

    lab = Label(root, text=question, font="Arial 18", width=40, height=2, bg = '#FFEBCD')
    lab.pack()
    name = StringVar()
    ent_name = Entry(root, textvariable=name, width=80)
    ent_name.place(x=230, y=420)

    btn = Button(root, text="Далее", width=25, height=1,
                     font=("Helvetica", "18"), command=lambda: count())
    btn["bg"] = btnBg
    btn.place(x=300, y=500)

    def count():
        global score
        lab.pack_forget()
        btn.place_forget()
        im2_label.place_forget()
        ent_name.place_forget()
        search_word = name.get()
        if search_word == "Крик":
            score = score + 1
            interface7()
            return score
        else:
            interface7()

def interface7():
    question
    im2 = Image.open("поцелуй.jpg")
    im2 = im2.resize((300, 350))
    im2 = ImageTk.PhotoImage(im2)
    im2_label = Label(image=im2)
    im2_label.image = im2
    im2_label.place(x=300, y=50)

    lab = Label(root, text=question, font="Arial 18", width=40, height=2, bg = '#FFEBCD')
    lab.pack()
    name = StringVar()
    ent_name = Entry(root, textvariable=name, width=80)
    ent_name.place(x=230, y=420)

    btn = Button(root, text="Далее", width=25, height=1,
                     font=("Helvetica", "18"), command=lambda: count())
    btn["bg"] = btnBg
    btn.place(x=300, y=500)

    def count():
        global score
        lab.pack_forget()
        btn.place_forget()
        im2_label.place_forget()
        ent_name.place_forget()
        search_word = name.get()
        if search_word == "Поцелуй":
            score = score + 1
            interface8()
            return score
        else:
            interface8()

def interface8():
    question
    im2 = Image.open("медведи.jpg")
    im2 = im2.resize((400, 300))
    im2 = ImageTk.PhotoImage(im2)
    im2_label = Label(image=im2)
    im2_label.image = im2
    im2_label.place(x=270, y=70)

    lab = Label(root, text=question, font="Arial 18", width=40, height=2, bg = '#FFEBCD')
    lab.pack()
    name = StringVar()
    ent_name = Entry(root, textvariable=name, width=80)
    ent_name.place(x=230, y=420)

    btn = Button(root, text="Далее", width=25, height=1,
                     font=("Helvetica", "18"), command=lambda: count())
    btn["bg"] = btnBg
    btn.place(x=300, y=500)

    def count():
        global score
        lab.pack_forget()
        btn.place_forget()
        im2_label.place_forget()
        ent_name.place_forget()
        search_word = name.get()
        if search_word == "Утро в сосновом лесу":
            score = score + 1
            interface9()
            return score
        else:
            interface9()

def interface9():
    question
    im2 = Image.open("память.jpg")
    im2 = im2.resize((400, 300))
    im2 = ImageTk.PhotoImage(im2)
    im2_label = Label(image=im2)
    im2_label.image = im2
    im2_label.place(x=270, y=70)

    lab = Label(root, text=question, font="Arial 18", width=40, height=2, bg = '#FFEBCD')
    lab.pack()
    name = StringVar()
    ent_name = Entry(root, textvariable=name, width=80)
    ent_name.place(x=230, y=420)

    btn = Button(root, text="Далее", width=25, height=1,
                     font=("Helvetica", "18"), command=lambda: count())
    btn["bg"] = btnBg
    btn.place(x=300, y=500)

    def count():
        global score
        lab.pack_forget()
        btn.place_forget()
        im2_label.place_forget()
        ent_name.place_forget()
        search_word = name.get()
        if search_word == "Постоянство памяти":
            score = score + 1
            vscore()
            return score
        else:
            vscore()

def vscore():
    im1 = Image.open("1.jpg")
    im1 = im1.resize((500, 250))
    im1 = ImageTk.PhotoImage(im1)
    im_label = Label(image=im1)
    im_label.image = im1
    im_label.pack(side=BOTTOM, pady=60)
    global score
    lab = Label(root, text='Из 9 картин вы знаете  ', font="Arial 18", width=40, height=2, bg = '#FFEBCD')
    lab.pack(side=TOP)
    lab1 = Label(root, text=score, font="Arial 18", width=40, height=2, bg = '#FFEBCD')
    lab1.pack(side=TOP)
    btn1 = Button(root, text="Выход", width=20, height=1,
                      font=("Helvetica", "18"), command=lambda: close_window())
    btn1["bg"] = btnBg
    btn1.pack()

    def close_window():
        root.destroy()

interface1()
root.mainloop()