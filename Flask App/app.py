from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from subprocess import Popen
import pickle

bg = '#FFEBCD'
btnBg = '#FFFAFA'
height = '600'
width = '900'

root = Tk()
root.configure(background=bg)
root.geometry(width + "x" + height + "+100+50")
root.title("Произведения искусства")


def menu():
    im1 = Image.open("1.jpg")
    im1 = ImageTk.PhotoImage(im1)
    im_label = Label(image = im1)
    im_label.image = im1
    im_label.place(x=100, y=200)

    loginBtn = Button(root, text="Войти", width=15, height=1, command=lambda: go(2), font=("Helvetica", "30"))
    loginBtn["bg"] = btnBg; loginBtn.pack(side=BOTTOM, pady = 40, padx = 50, anchor=E)
    int1Btn = Button(root, text="Пробный тест", width=15, height=1, command=lambda: go(1), font=("Helvetica", "30"))
    int1Btn["bg"] = btnBg; int1Btn.pack(side=BOTTOM, pady=40, padx = 50, anchor=E)
    regBtn = Button(root, text="Регистрация", width=15, height=1, command=lambda: go(0), font=("Helvetica", "30"))
    regBtn["bg"] = btnBg; regBtn.pack(side=BOTTOM, pady=40, padx = 50, anchor=E)


    def go(num):
        loginBtn.pack_forget()
        int1Btn.pack_forget()
        regBtn.pack_forget()
        if num == 0:
            interface2()
        elif num == 1:
            Popen('python prob_test.py')
        else:
            interface4()

    def interface2():
        name = Label(root, text='Имя', font=("Helvetica", "20"), bg='#FFEBCD')
        name.place(x=450, y=100)
        mail = Label(root, text='Email', font=("Helvetica", "20"), bg='#FFEBCD')
        mail.place(x=450, y=200)
        passw = Label(root, text='Пароль', font=("Helvetica", "20"), bg='#FFEBCD')
        passw.place(x=450, y=300)
        entry_name = Entry(root, width = 30)
        entry_name.place(x=600, y=100)
        entry_email = Entry(root, width = 30)
        entry_email.place(x=600, y=200)
        entry_passw = Entry(root, show='*', width = 30)
        entry_passw.place(x=600, y=300)

        regbtn = Button(root, text="Регистрация", width=15, height=1, command=lambda: save(), font=("Helvetica", "30"))
        regbtn["bg"] = btnBg;
        regbtn.place(x=500, y=500)
        reg1btn = Button(root, text="Назад", width=15, height=1, command=lambda: back(),
                        font=("Helvetica", "30"))
        reg1btn["bg"] = btnBg;
        reg1btn.place(x=100, y=500)

        def back():
            name.place_forget()
            mail.place_forget()
            passw.place_forget()
            entry_name.place_forget()
            entry_email.place_forget()
            entry_passw.place_forget()
            reg1btn.place_forget()
            regbtn.place_forget()
            menu()

        def save():
            ml=entry_email.get()
            login_passw_save = {}
            login_passw_save[ml] = entry_passw.get()
            f = open('login.txt', 'wb')
            pickle.dump(login_passw_save, f)
            f.close()
            name.place_forget()
            mail.place_forget()
            passw.place_forget()
            entry_name.place_forget()
            entry_email.place_forget()
            entry_passw.place_forget()
            reg1btn.place_forget()
            regbtn.place_forget()
            interface4()


    def interface3():
        name_label = Label(root, text="Добро пожаловать", width=40, height=1, font=("Helvetica", "20"),
                           bg='#FFEBCD')
        name_label.pack(side=TOP)
        stBtn = Button(root, text="Начать тест", width=15, height=1, command=lambda: go(2), font=("Helvetica", "25"))
        stBtn["bg"] = btnBg;
        stBtn.pack(side=BOTTOM, pady=40, padx=50, anchor=E)
        statBtn = Button(root, text="Статистика", width=15, height=1, command=lambda: go(1), font=("Helvetica", "25"))
        statBtn["bg"] = btnBg;
        statBtn.pack(side=BOTTOM, pady=50, padx=50, anchor=E)
        outBtn = Button(root, text="Выйти", width=15, height=1, command=lambda: go(0), font=("Helvetica", "25"))
        outBtn["bg"] = btnBg;
        outBtn.pack(side=BOTTOM, pady=70, padx=50, anchor=E)

        def go(num):
            name_label.pack_forget()
            stBtn.pack_forget()
            statBtn.pack_forget()
            outBtn.pack_forget()
            if num == 0:
                menu()
            elif num == 1:
                stat()
            else:
                Popen('python test.py')


    def interface4():
        mail = Label(root, text='Email', font=("Helvetica", "20"), bg ='#FFEBCD')
        mail.place(x=450, y=200)
        passw = Label(root, text='Пароль', font=("Helvetica", "20"), bg ='#FFEBCD')
        passw.place(x=450, y=300)
        entry_mail = Entry(root, width=30)
        entry_mail.place(x=600, y=200)
        entry_passw = Entry(root, show='*', width=30)
        entry_passw.place(x=600, y=300)

        regbtn = Button(root, text="Вход", width=15, height=1, command=lambda: login(), font=("Helvetica", "30"))
        regbtn["bg"] = btnBg;
        regbtn.place(x=500, y=500)
        reg1btn = Button(root, text="Назад", width=15, height=1, command=lambda: back(),
                         font=("Helvetica", "30"))
        reg1btn["bg"] = btnBg;
        reg1btn.place(x=100, y=500)

        def back():
            mail.place_forget()
            passw.place_forget()
            entry_mail.place_forget()
            entry_passw.place_forget()
            reg1btn.place_forget()
            regbtn.place_forget()
            menu()

        def login():
            f = open('login.txt', 'rb')
            a = pickle.load(f)
            f.close()
            mail.place_forget()
            passw.place_forget()
            entry_mail.place_forget()
            entry_passw.place_forget()
            reg1btn.place_forget()
            regbtn.place_forget()
            if entry_mail.get() in a:
                if entry_passw.get() == a[entry_mail.get()]:
                    interface3()
                else:
                    messagebox.showerror('Ошибка!', 'Неверный логин или пароль')
            else:
                messagebox.showerror('Ошибка!', 'Неверный логин или пароль')

    def stat():
        im_label.place_forget()
        im2 = Image.open("1.jpg")
        im2 = ImageTk.PhotoImage(im2)
        im2_label = Label(image=im2)
        im2_label.image = im2
        im2_label.pack(side=BOTTOM, pady=10)
        best_sc = 7
        w_sc = 4
        stat_label = Label(root, text="Ваша статистика:", width=40, height=1, font=("Helvetica", "20"),
                          bg='#FFEBCD')
        stat_label.pack(side=TOP, pady=10)
        lab = Label(root, text='Ваш лучший результат:  ', font="Arial 18", width=40, height=2, bg='#FFEBCD')
        lab.pack(side=TOP)
        lab1 = Label(root, text=best_sc, font="Arial 18", width=40, height=2, bg='#FFEBCD')
        lab1.pack(side=TOP)
        lab2 = Label(root, text='Ваш худший результат:  ', font="Arial 18", width=40, height=2, bg='#FFEBCD')
        lab2.pack(side=TOP)
        lab3 = Label(root, text=w_sc, font="Arial 18", width=40, height=2, bg='#FFEBCD')
        lab3.pack(side=TOP)

        btn1 = Button(root, text="Выход", width=20, height=1,
                      font=("Helvetica", "18"), command=lambda: go(0))
        btn1["bg"] = btnBg
        btn1.pack()

        def go(num):
            stat_label.pack_forget()
            lab.pack_forget()
            lab1.pack_forget()
            lab2.pack_forget()
            lab3.pack_forget()
            btn1.pack_forget()
            if num == 0:
                interface3()

menu()
root.mainloop()