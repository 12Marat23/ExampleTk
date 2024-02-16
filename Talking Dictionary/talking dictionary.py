import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.geometry("1000x626+150+50")
root.title("Talking Dictionary")
root.resizable(False, False)
root.wm_attributes('-transparentcolor')
bg_image = ImageTk.PhotoImage(Image.open('image/foliage.jpg'))
bg_Label = tk.Label(root, image=bg_image)
bg_Label.place(x=0, y=0)

enterwordLabel = tk.Label(root, text="Enter Word",
                          font=('Castellar', 40),
                          foreground='blue')

enterwordLabel.place(x=530, y=20)

if __name__ == '__main__':
    root.mainloop()
