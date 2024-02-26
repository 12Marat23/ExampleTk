import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import json
from difflib import get_close_matches
import pyttsx3

'''Это код, переделенной с применением ООП, 
из  https://www.youtube.com/watch?v=Oay2uUm8-zk&list=PLUgFQtEcQLl_TmkNjA-UHg-PNABqTuXPb&index=5 '''


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1000x626+150+50")
        self.title("Talking Dictionary")
        self.resizable(False, False)
        self.menu()

    def menu(self):
        self.bg_image = ImageTk.PhotoImage(Image.open('image/foliage1.jpg'))
        self.bg_Label = tk.Label(image=self.bg_image)
        self.bg_Label.place(x=0, y=0)

        self.enterwordLabel = tk.Label(text="Enter Word",
                                       font=('Castellar', 40),
                                       foreground='blue',
                                       bg='#fafafa')
        self.enterwordEntry = tk.Entry(width=25, font=('Californian FB', 24),
                                       justify="center", bd=5, relief="groove")
        self.enterwordLabel.place(x=530, y=20)
        self.enterwordEntry.place(x=532, y=100)

        self.searchImage = ImageTk.PhotoImage(Image.open("image/search.png"))
        self.searchButton = tk.Button(image=self.searchImage, bd=0, bg='#fafafa',
                                      cursor='hand2', activebackground='#fafafa', command=self.search)  #
        self.searchButton.place(x=650, y=170)

        self.micImage = ImageTk.PhotoImage(Image.open("image/mic.png"))
        self.micButton = tk.Button(image=self.micImage, bd=0, bg='#fafafa',
                                   cursor='hand2', activebackground='#fafafa', command=self.wordaudio)  #
        self.micButton.place(x=750, y=170)

        self.meaningLabel = tk.Label(text="Meaning",
                                     font=('Castellar', 40),
                                     foreground='blue',
                                     bd=5, bg='#fafafa')
        self.meaningText = tk.Text(width=40, font=('Californian FB', 14),
                                   bd=5, relief="groove", height=8)
        self.meaningLabel.place(x=580, y=230)
        self.meaningText.place(x=532, y=330)

        self.micImage2 = ImageTk.PhotoImage(Image.open("image/microphone.png"))
        self.micButton2 = tk.Button(image=self.micImage2, bd=0, bg='#fafafa',
                                    cursor='hand2', activebackground='#fafafa', command=self.dataaudio)  #
        self.micButton2.place(x=580, y=540)

        self.clearImage = ImageTk.PhotoImage(Image.open("image/clear.png"))
        self.clearButton = tk.Button(image=self.clearImage, bd=0, bg='#fafafa',
                                     cursor='hand2', activebackground='#fafafa', command=self.clear)  #
        self.clearButton.place(x=700, y=540)

        self.exitImage = ImageTk.PhotoImage(Image.open("image/exit.png"))
        self.exitButton = tk.Button(image=self.exitImage, bd=0, bg='#fafafa',
                                    cursor='hand2', activebackground='#fafafa', command=self.exitapp)  #
        self.exitButton.place(x=830, y=540)

        self.bind('<Return>', self.enter_function)


class Func(App):
    def __init__(self):
        super().__init__()
        self.engine = pyttsx3.init()
        self.voice = self.engine.getProperty('voice')
        self.engine.setProperty('voice', self.voice[1])
        self.engine.setProperty('rate', 150)

    def dataaudio(self):
        self.engine.say(self.meaningText.get(1.0, 'end'))
        self.engine.runAndWait()

    def wordaudio(self):
        self.engine.say(self.enterwordEntry.get())
        self.engine.runAndWait()

    def exitapp(self):
        close = messagebox.askyesno('Confirm', 'Do you want to exit?')
        if close:
            self.destroy()

    def clear(self):
        self.enterwordEntry.delete(0, "end")
        self.meaningText.delete(1.0, 'end')

    def enter_function(self, event):
        self.searchButton.invoke()

    def search(self):
        data = json.load(open('data.json'))
        word = self.enterwordEntry.get()
        word = word.lower()
        if word in data:
            meaning = data[word]
            self.meaningText.delete(1.0, 'end')
            for item in meaning:
                self.meaningText.insert('end', u'\u2022' + item + '\n\n')
        elif len(get_close_matches(word, data.keys())) > 0:
            close_match = get_close_matches(word, data.keys())[0]
            res = messagebox.askyesno('Confirm', f'Did you mean {close_match} instead?')
            if res:
                self.enterwordEntry.delete(0, "end")
                self.enterwordEntry.insert('end', close_match)
                self.meaningText.delete(1.0, 'end')
                meaning = data[close_match]
                for item in meaning:
                    self.meaningText.insert("end", u'\u2022' + item + '\n\n')
            else:
                messagebox.showerror('Error', 'The word doesnt exist.')
                self.deleteword()
        else:
            messagebox.showinfo('Info', 'The word doesnt exist.')
            self.deleteword()

    def deleteword(self):
        self.enterwordEntry.delete(0, "end")
        self.meaningText.delete(1.0, 'end')


if __name__ == '__main__':
    root = Func()
    root.mainloop()
