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
root.title("Пробный тест")

score = 0
question= 'Как называется эта картина?'
def prob1():
    global question
    im2 = Image.open("Мона.jpg")
    im2 = im2.resize((200, 300))
    im2 = ImageTk.PhotoImage(im2)
    im2_label = Label(image=im2)
    im2_label.image = im2
    im2_label.place(x=350, y=50)

    lab = Label(root, text=question, font="Arial 18", width=40, height=2, bg = '#FFEBCD')
    lab.pack()
    name = StringVar()
    ent_name = Entry(root, textvariable=name, width=80)
    ent_name.place(x=220, y=400)

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
        if search_word == "Мона Лиза":
            score = score + 1
            prob2()
            return score
        else:
            prob2()

def prob2():
    global question
    im3 = Image.open("девочка.jpg")
    im3 = im3.resize((300, 300))
    im3 = ImageTk.PhotoImage(im3)
    im3_label = Label(image=im3)
    im3_label.image = im3
    im3_label.place(x=300, y=50)

    lab = Label(root, text=question, font="Arial 18", width=40, height=2, bg = '#FFEBCD')
    lab.pack()
    name = StringVar()
    ent_name = Entry(root, textvariable=name, width=80)
    ent_name.place(x=220, y=400)

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
        if search_word == "Девочка с персиками":
            score = score + 1
            prob3()
            return score
        else:
            prob3()

def prob3():
    global question
    im3 = Image.open("венера.jpg")
    im3 = im3.resize((400, 300))
    im3 = ImageTk.PhotoImage(im3)
    im3_label = Label(image=im3)
    im3_label.image = im3
    im3_label.place(x=250, y=70)

    lab = Label(root, text=question, font="Arial 18", width=40, height=2, bg = '#FFEBCD')
    lab.pack()
    name = StringVar()
    ent_name = Entry(root, textvariable=name, width=80)
    ent_name.place(x=220, y=400)

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
        if search_word == "Рождение Венеры" :
            score = score + 1
            pr_sc()
            return score
        else:
            pr_sc()

def pr_sc():
    im1 = Image.open("1.jpg")
    im1 = im1.resize((500, 250))
    im1 = ImageTk.PhotoImage(im1)
    im_label = Label(image=im1)
    im_label.image = im1
    im_label.pack(side=BOTTOM, pady=60)
    global score
    lab = Label(root, text='Вы знаете  ', font="Arial 18", width=40, height=2, bg='#FFEBCD')
    lab.pack(side=TOP)
    lab1 = Label(root, text=score, font="Arial 18", width=40, height=2, bg='#FFEBCD')
    lab1.pack(side=TOP)
    btn1 = Button(root, text="Выход", width=20, height=1,
                  font=("Helvetica", "18"), command=lambda: close_window())
    btn1["bg"] = btnBg
    btn1.pack()

    def close_window():
        root.destroy()

prob1()
root.mainloop()