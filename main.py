import tkinter as tk
from PIL import Image,ImageTk
from tkinter.colorchooser import askcolor
import customtkinter

#nastavení grafiky
root = tk.Tk()
#root.geometry("1080x1920")
root.title("Desítka score")
canvas_width = 1080/2
canvas_height = 2210/2

image = Image.open("logo.png")
image = image.resize((400+100,120))
pic = ImageTk.PhotoImage(image)

canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="#32373B")
canvas.pack()

button1 = None
button2 = None
button3 = None

def clearnutigui():
    global button1, button2, button3
    #canvas.destroy("all")
    if button1:
        button1.destroy()
    if button2:
        button2.destroy()
    if button3:
        button3.destroy()
        
def vytvorit_tlacitko(text, command, y):
    btn = customtkinter.CTkButton(
        canvas,
        text=text,
        fg_color='#677279',
        font=("Poppins", 50),
        width=canvas_width / 1.1,
        height=90,
        command=command,
        cursor="hand2",
        corner_radius=100000,
        hover_color="#4B5358",
        border_width=5
    )
    btn.place(x=25, y=y + padding)
    return btn

def hostovani():
    clearnutigui()
    canvas.create_text(canvas_width/2,300+padding,text="Hostování skóre",fill="white", font=("Poppins", 40, "bold" ))
    canvas.create_text(canvas_width/2,350+padding,text="Počkej, než se napojí všichni hráči",fill="white", font=("Poppins", 20,))
    button4 = vytvorit_tlacitko("Zpátky do menu",main_menu,900)

def pripojeni():
    clearnutigui()

padding = 20
    
def main_menu():
    global button1, button2, button3

    canvas.create_rectangle(0,0,canvas_width,220+padding,fill="#545D63")
    canvas.create_image(canvas_width/2,50+padding,image=pic)
    canvas.create_text(canvas_width/2,160+padding,text="SCORE",fill="black", font=("Poppins", 70, "bold" ))

    button1 = vytvorit_tlacitko("Hostuj",hostovani,300)

    button2 = vytvorit_tlacitko("Připoj",pripojeni,430)

    button3 = vytvorit_tlacitko("Exit",exit,600)
    
main_menu()


root.mainloop()