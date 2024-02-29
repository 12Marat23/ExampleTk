import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import sqlite3


class Registration:
    ''' Т.к. база данных уже существует,
    мы присваиваем бд переменную db_name'''
    db_name = "project_database.db"

    # Инициализация проекта
    def __init__(self, window):
        self.window = window
        self.window.title("                         Registration form")
        self.window.geometry("390x640")
        self.window.resizable(False, False)
        self.window.config(bd=10)

        # Создаем заголовок
        tk.Label(window, text="Registration form", fg="black", font=("Comic Sans ", 13, "bold"), pady=7).pack()

        # Подключаем картинку
        image = Image.open("new_user.png")
        new_image = image.resize((40, 40))
        render = ImageTk.PhotoImage(new_image)
        label_image = tk.Label(window, image=render)
        label_image.image = render
        label_image.pack(pady=4)

        # Создаем рамку с надписью
        frame = tk.LabelFrame(window, text="Personal data", font=("Comic Sans MS", 13, "bold"))
        frame.config(bd=2)
        frame.pack()

        # Создаем лейблы и поля ввода
        "Fields"
        # passport
        label_passport = tk.Label(frame, text="Passport:", font=("Comic Sans MS", 10, "bold"))
        label_passport.grid(row=0, column=0, sticky="s", padx=5, pady=7)
        self.passport = tk.Entry(frame, width=25)
        self.passport.grid(row=0, column=1, padx=10, pady=10)

        # first name
        label_name = tk.Label(frame, text="First name:", font=("Comic Sans MS", 10, "bold"))
        label_name.grid(row=1, column=0, sticky="s", padx=5, pady=7)
        self.names = tk.Entry(frame, width=25)
        self.names.grid(row=1, column=1, padx=10, pady=10)

        # last name
        label_last_name = tk.Label(frame, text="Last name:", font=("Comic Sans MS", 10, "bold"))
        label_last_name.grid(row=2, column=0, sticky="s", padx=5, pady=7)
        self.last_names = tk.Entry(frame, width=25)
        self.last_names.grid(row=2, column=1, padx=10, pady=10)

        # sex
        label_sex = tk.Label(frame, text="Sex:", font=("Comic Sans MS", 10, "bold"))
        label_sex.grid(row=3, column=0, sticky="s", padx=5, pady=7)
        self.sex = ttk.Combobox(frame, values=["Male", "Female"], width=22, state="readonly")
        self.sex.current(0)
        self.sex.grid(row=3, column=1, padx=10, pady=10)

        # age
        label_age = tk.Label(frame, text="Age:", font=("Comic Sans MS", 10, "bold"))
        label_age.grid(row=4, column=0, sticky="s", padx=5, pady=7)
        self.age = tk.Entry(frame, width=25)
        self.age.grid(row=4, column=1, padx=10, pady=10)

        # Email
        label_email = tk.Label(frame, text="Email:", font=("Comic Sans MS", 10, "bold"))
        label_email.grid(row=5, column=0, sticky="s", padx=5, pady=8)
        self.email = tk.Entry(frame, width=25)
        self.email.grid(row=5, column=1, padx=10, pady=10)

        # Password
        label_password = tk.Label(frame, text="Password:", font=("Comic Sans MS", 10, "bold"))
        label_password.grid(row=6, column=0, sticky="s", padx=5, pady=8)
        self.password = tk.Entry(frame, width=25, show="*")
        self.password.grid(row=6, column=1, padx=10, pady=10)

        # Reaction
        label_password_repeat = tk.Label(frame, text="Reaction:", font=("Comic Sans MS", 10, "bold"))
        label_password_repeat.grid(row=7, column=0, sticky="s", padx=5, pady=8)
        self.password_repeat = tk.Entry(frame, width=25, show="*")
        self.password_repeat.grid(row=7, column=1, padx=10, pady=10)

        # Создаем рамку с надписями для вопросов подтверждение пользователя
        # Question
        question_frame = tk.LabelFrame(window, text="If you forget your password", font=("Comic Sans MS", 13, "bold"))
        question_frame.config(bd=2, pady=5)
        question_frame.pack()
        # Question label
        label_question = tk.Label(question_frame, text='Question', font=("Comic Sans MS", 10, "bold"))
        label_question.grid(row=0, column=0, sticky='s', padx=10, pady=1)
        self.combo_question = ttk.Combobox(question_frame,
                                           values=["Name of your first pet?", "Place where did you go to school?",
                                                   "What city were you born in?",
                                                   "What is the name of your favorite team?"],
                                           width=30, state='readonly')
        self.combo_question.current(0)
        self.combo_question.grid(row=0, column=1, padx=10, pady=7)

        # answer
        label_answer = tk.Label(question_frame, text='Answer', font=("Comic Sans MS", 10, "bold"))
        label_answer.grid(row=1, column=0, padx=10, pady=7)
        self.answer = tk.Entry(question_frame, width=33)
        self.answer.grid(row=1, column=1, padx=10, pady=7)

        # note
        label_note = tk.Label(question_frame, text='*This answer will allow you to recover your password.',
                              font=("Comic Sans MS", 10, "bold"),
                              foreground='green')
        label_note.grid(row=2, column=0, columnspan=2, sticky='s', padx=10)

        # Рамка для кнопок
        frame_button = tk.Frame(window)
        frame_button.pack()

        #  button
        button_registration = tk.Button(frame_button, text='REGISTRATION', height=2, width=11,
                                        bg='green', fg='white', command=self.user_registration)
        button_clear = tk.Button(frame_button, text='CLEAR', height=2, width=11, bg='grey',
                                 fg='white', command=self.clean_formulary)
        button_close = tk.Button(frame_button, text='CLOSE', height=2, width=11,
                                 bg='red', fg='white', command=frame.quit)
        button_registration.grid(row=0, column=0, padx=5)
        button_clear.grid(row=0, column=1, padx=5)
        button_close.grid(row=0, column=3, padx=5)

    def run_query(self, query, parameters=()):
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            result = cursor.execute(query, parameters)
            connection.commit()
        return result

    def clean_formulary(self):
        """Фунция очистки полей ввода данных"""
        self.passport.delete(0, 'end')
        self.names.delete(0, 'end')
        self.last_names.delete(0, 'end')
        self.sex.delete(0, 'end')
        self.age.delete(0, 'end')
        self.email.delete(0, 'end')
        self.password.delete(0, 'end')
        self.password_repeat.delete(0, 'end')

    def check_formular_full(self):
        """
        Проверка заполнены ли все поля. Если да, возвращает True
        иначе, возвращает сообщение об ошибке
        """
        if (len(self.passport.get()) != 0 and len(self.names.get()) != 0 and len(self.last_names.get()) != 0 and
                len(self.sex.get()) != 0 and len(self.age.get()) != 0 and len(self.email.get()) != 0 and len(
                    self.passport.get()) != 0 and len(self.password_repeat.get()) != 0 and len(self.answer.get()) != 0):
            return True
        else:
            messagebox.showerror("Registration error", "Complete all the fields of the form")
            pass

    def password_validation(self):
        """
        Проверяет совпадают ли пароль с повтором пароли.
        Если да то возвращает True, иначе выводить сообщение с ошибкой
        """
        if str(self.password.get()) == str(self.password_repeat.get()):
            return True
        else:
            messagebox.showerror("Registration error", "Passwords don't match")

    def search_passport(self, passport):
        """
        Ищет в базе данных совпадение с введенным значением passport.
        Если есть совпадение, то возвращает значения этой строки в виде списка.
        Иначе возвращает пустой список
        """
        with sqlite3.connect(self.db_name) as connection:
            cursor = connection.cursor()
            sql = "SELECT * FROM Usuarios WHERE passport = {}".format(passport)
            cursor.execute(sql)
            pspt = cursor.fetchall()
            cursor.close()
            return pspt

    def passport_validation(self):
        """
        Проверяет пуст ли список который вернул search_passport.
        Если список пуст, функция возвращает True, иначе выводит сообщение об ошибке
        """
        psp = self.passport.get()
        data = self.search_passport(psp)
        if data == []:
            return True
        else:
            messagebox.showerror("Registration error", "Passport previously registered")

    # Регистрация пользователя

    def user_registration(self):
        """Регистрация пользователя.
        Если if self.check_formular_full() and self.passport_validation() and self.password_validation() == True,
        то введенные  данные записываются в БД и и выводится сообщение об удачной регистрации.
        """
        if self.check_formular_full() and self.passport_validation() and self.password_validation():
            query = 'INSERT INTO Usuarios VALUES(NULL,?,?,?,?,?,?,?,?)'
            parameters = (self.passport.get(), self.names.get(), self.last_names.get(), self.sex.get(), self.age.get(),
                          self.email.get(), self.password.get(), self.answer.get())
            self.run_query(query, parameters)
            messagebox.showinfo("SUCCESSFUL REGISTRATION", f'Wellcome {self.names.get()} {self.last_names.get()}')
            self.clean_formulary()


if __name__ == '__main__':
    window = tk.Tk()
    app = Registration(window)
    window.mainloop()
