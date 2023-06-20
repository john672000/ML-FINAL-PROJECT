import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
from ADD_DATA import add_data, face_data
from RECOG_DATA import recog_data
import pickle
import os.path

window = tk.Tk()
window.title("Command Center")
window.geometry("900x750")
image_path = "data/face_recognition_image.png"
image = Image.open(image_path)
image = image.resize((800,500), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(window, image=photo)
image_label.pack(pady=20)

button_frame = tk.Frame(window)
button_frame.pack()

def total_names():
    path = 'C:/Users/John/Desktop/ML FINAL PROJECT/Final Project_Face-Recognition-using-KNN-main/Face-Recognition-using-KNN-main/data/names.pkl'
    check_file = os.path.exists(path)
    if check_file == False:
        messagebox.showinfo('ERROR', 'NO INFORMATION IN THE DATABASE TO SHOW NAMES, ADD NEW FACE TO BEGIN')
    else:
        messagebox.showinfo('Sucessfull','Check in the Console')
        face_data()
def add():
    messagebox.showinfo('Attention!!', 'Enter your name in the console')
    add_data()
def iftru():
    path = 'C:/Users/John/Desktop/ML FINAL PROJECT/Final Project_Face-Recognition-using-KNN-main/Face-Recognition-using-KNN-main/data/names.pkl'
    check_file = os.path.exists(path)
    if check_file == False:
        messagebox.showinfo('ERROR','NO INFORMATION IN THE DATABASE TO START TO BEGIN, ADD NEW FACE')
    else:
        recog_data()


animate_button = tk.Button(button_frame, text="START RECOGNIZING", command=iftru, width=25,fg="white", bg="green")
animate_button.grid(row=0, column=1, padx=20, pady=10)

click_button = tk.Button(button_frame, text="ADD NEW FACE DATA", command=add, width=25,fg="white", bg="green")
click_button.grid(row=2, column=1, padx=10, pady=10)

click_button = tk.Button(button_frame, text="NAMES IN DATABASE", command=total_names, width=25,fg="white", bg="green")
click_button.grid(row=3, column=1, padx=10, pady=10)


click_button = tk.Button(button_frame, text="EXIT THE COMMAND CENTER", command=exit, width=25,fg="white", bg="red")
click_button.grid(row=4, column=1, padx=10, pady=10)



window.mainloop()
