import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import json
from difflib import get_close_matches
import pyttsx3

'''Этот пример взять из: https://www.youtube.com/watch?v=Oay2uUm8-zk&list=PLUgFQtEcQLl_TmkNjA-UHg-PNABqTuXPb&index=5'''

engine = pyttsx3.init()
voice = engine.getProperty('voice')
engine.setProperty('voice', voice[1])
engine.setProperty('rate', 150)


def dataaudio():
    engine.say(meaningText.get(1.0, 'end'))
    engine.runAndWait()

def wordaudio():
    engine.say(enterwordEntry.get())
    engine.runAndWait()

def exitapp():
    close = messagebox.askyesno('Confirm', 'Do you want to exit?')
    if close:
        root.destroy()


def clear():
    enterwordEntry.delete(0, "end")
    meaningText.delete(1.0, 'end')


def enter_function(event):
    searchButton.invoke()


def search():
    data = json.load(open('data.json'))
    word = enterwordEntry.get()
    word = word.lower()
    if word in data:
        meaning = data[word]
        meaningText.delete(1.0, 'end')
        for item in meaning:
            meaningText.insert('end', u'\u2022' + item + '\n\n')
    elif len(get_close_matches(word, data.keys())) > 0:
        close_match = get_close_matches(word, data.keys())[0]
        res = messagebox.askyesno('Confirm', f'Did you mean {close_match} instead?')
        if res:
            enterwordEntry.delete(0, "end")
            enterwordEntry.insert('end', close_match)
            meaningText.delete(1.0, 'end')
            meaning = data[close_match]
            for item in meaning:
                meaningText.insert("end", u'\u2022' + item + '\n\n')
        else:
            messagebox.showerror('Error', 'The word doesnt exist.')
            enterwordEntry.delete(0, "end")
            meaningText.delete(1.0, 'end')
    else:
        messagebox.showinfo('Info', 'The word doesnt exist.')
        enterwordEntry.delete(0, "end")
        meaningText.delete(1.0, 'end')


root = tk.Tk()
root.geometry("1000x626+150+50")
root.title("Talking Dictionary")
root.resizable(False, False)

bg_image = ImageTk.PhotoImage(Image.open('image/foliage1.jpg'))
bg_Label = tk.Label(root, image=bg_image)
bg_Label.place(x=0, y=0)

enterwordLabel = tk.Label(root, text="Enter Word",
                          font=('Castellar', 40),
                          foreground='blue',
                          bg='#fafafa')
enterwordEntry = tk.Entry(root, width=25, font=('Californian FB', 24),
                          justify="center", bd=5, relief="groove")
enterwordLabel.place(x=530, y=20)
enterwordEntry.place(x=532, y=100)

searchImage = ImageTk.PhotoImage(Image.open("image/search.png"))
searchButton = tk.Button(root, image=searchImage, bd=0, bg='#fafafa',
                         cursor='hand2', activebackground='#fafafa', command=search)
searchButton.place(x=650, y=170)

micImage = ImageTk.PhotoImage(Image.open("image/mic.png"))
micButton = tk.Button(root, image=micImage, bd=0, bg='#fafafa',
                      cursor='hand2', activebackground='#fafafa', command=wordaudio)
micButton.place(x=750, y=170)

meaningLabel = tk.Label(root, text="Meaning",
                        font=('Castellar', 40),
                        foreground='blue',
                        bd=5, bg='#fafafa')
meaningText = tk.Text(root, width=40, font=('Californian FB', 14),
                      bd=5, relief="groove", height=8)
meaningLabel.place(x=580, y=230)
meaningText.place(x=532, y=330)

micImage2 = ImageTk.PhotoImage(Image.open("image/microphone.png"))
micButton2 = tk.Button(root, image=micImage2, bd=0, bg='#fafafa',
                       cursor='hand2', activebackground='#fafafa', command=dataaudio)
micButton2.place(x=580, y=540)

clearImage = ImageTk.PhotoImage(Image.open("image/clear.png"))
clearButton = tk.Button(root, image=clearImage, bd=0, bg='#fafafa',
                        cursor='hand2', activebackground='#fafafa', command=clear)
clearButton.place(x=700, y=540)

exitImage = ImageTk.PhotoImage(Image.open("image/exit.png"))
exitButton = tk.Button(root, image=exitImage, bd=0, bg='#fafafa',
                       cursor='hand2', activebackground='#fafafa', command=exitapp)
exitButton.place(x=830, y=540)

root.bind('<Return>', enter_function)

if __name__ == '__main__':
    root.mainloop()
