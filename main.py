import tkinter as tk
from PIL import Image,ImageTk

#nastavení grafiky
root = tk.Tk()
#root.geometry("1080x1920")
root.title("Desítka score")
canvas_width = 1080/2
canvas_height = 2210/2

image = Image.open("logo.png")
image = image.resize((400+100,120))
pic = ImageTk.PhotoImage(image)

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="darkgrey")
canvas.pack()

button1 = None
button2 = None

def hostovani():
    global button1, button2
    canvas.delete("all")
    if button1:
        button1.destroy()
    if button2:
        button2.destroy()

def pripojeni():
    global button1, button2
    canvas.delete("all")
    if button1:
        button1.destroy()
    if button2:
        button2.destroy()

def main_menu():
    global button1, button2

    canvas.create_rectangle(0,0,1080/2,200,fill="grey")
    canvas.create_text(canvas_width/2,150,text="Score",fill="white", font=("Helvetica", 50, "bold"))


    canvas.create_image(canvas_width/2,55,image=pic)

    button1 = tk.Button(canvas, text="Hostuj", bg='grey', fg='white', font=("Helvetica", 30, "bold"), width=20, command=hostovani)
    button1.place(x=25, y=300)

    button2 = tk.Button(canvas, text="Připoj", bg='grey', fg='white', font=("Helvetica", 30, "bold"), width=20, command=pripojeni)
    button2.place(x=25, y=400)

    button3 = tk.Button(canvas, text="Exit", bg='grey', fg='white', font=("Helvetica", 30, "bold"), width=20, command=exit)
    button3.place(x=25, y=600)

main_menu()


root.mainloop()