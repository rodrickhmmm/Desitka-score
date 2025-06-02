import tkinter as tk
from PIL import Image,ImageTk
from tkinter.colorchooser import askcolor
import customtkinter
import urllib.request
#import base64
import io

#do tadytoho nejlépe nešahat!!!
root = tk.Tk()
root.title("Desítka score")
canvas_width = 1080
canvas_height = 2210
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="#32373B")
canvas.pack()

link = "https://mindok.cz/wp-content/uploads/2022/03/desitka-logo.png"

class WebImage:
    def __init__(self, url):
        with urllib.request.urlopen(url) as u:
            raw_data = u.read()
        image = Image.open(io.BytesIO(raw_data))
        image = image.resize((840, 200))  # Změna velikosti zde
        self.image = ImageTk.PhotoImage(image)

    def get(self):
        return self.image
    
#image (předělám na url)
pic = WebImage(link).get()

# definovani buttonu
button1 = None
button2 = None
button3 = None
button4 = None
entry = None

#padding - idk proč ale jo
padding = 40
paddingfromheader=80
padding2=140

android=50
# header 
def header():
    canvas.create_rectangle(0,0,canvas_width,340+padding,fill="#545D63")
    canvas.create_image(canvas_width/2,50+padding+10,image=pic)
    canvas.create_text(canvas_width/2+3,249+padding,text="SCORE",fill="white", font=("Roboto Medium", 83-android, "bold"))
    canvas.create_text(canvas_width/2,250+padding,text="SCORE",fill="#101b1f", font=("Roboto Medium", 83-android, "bold"))

#clearne cely gui
def clearnutigui():
    global button1, button2, button3, button4, entry
    canvas.delete("all")
    if button1:
        button1.destroy()
    if button2:
        button2.destroy()
    if button3:
        button3.destroy()
    if button4:
        button4.destroy()
    if entry:
        entry.destroy()

# funkce na vytvoreni tlacitka - abych nemusel davat porad ctrlc a ctrlv
def vytvorit_tlacitko(text, command, y):
    btn = customtkinter.CTkButton(
        canvas,
        text=text,
        fg_color='#677279',
        font=("Open Sans", 70+android),
        width=canvas_width / 1.05,
        height=200,
        command=command,
        cursor="hand2",
        corner_radius=100000,
        hover_color="#4B5358",
        border_width=5
    )
    btn.place(x=25, y=y + padding)
    return btn

# Scena(?) s hostovanim hry
def hostovani():
    global button4
    clearnutigui()
    
    header()
    
    canvas.create_text(canvas_width/2,320+padding+padding2,text="Hostování skóre",fill="white", font=("Roboto Medium", 25, "bold" ))
    canvas.create_text(canvas_width/2,420+padding+padding2,text="Počkej, než se napojí všichni hráči",fill="white", font=("Open Sans", 10,))
    button4 = vytvorit_tlacitko("Zpátky do menu",main_menu,canvas_height/1.3)

# Scena(?) s pripojenim do hry
def pripojeni():
    global button4, entry, button3
    clearnutigui()
    
    header()

    padding3=100
    
    entry = customtkinter.CTkEntry(canvas, placeholder_text="Jméno", width=canvas_width/1.1, height=100, fg_color="#677279",font=("Open Sans", 50),placeholder_text_color="#d6d6d6")
    entry.place(x=40,y=220+padding*3+padding3+padding2)
    
    canvas.create_rectangle(20,300+padding2,canvas_width-20,500+padding3+padding2,fill="#545D63")
    
    canvas.create_text(canvas_width/3.2,370+padding+padding3,text="Zadej své jméno",fill="white", font=("Open Sans", 15, "bold" ))
    
    button3 = vytvorit_tlacitko("Připojit se",0,570+padding2+padding3/2)
    
    button4 = vytvorit_tlacitko("Zpátky do menu",main_menu,canvas_height/1.3)
    
# Main scene
def main_menu():
    global button1, button2, button3, button4, entry
    
    clearnutigui()
    
    header()

    button1 = vytvorit_tlacitko("Hostuj hru",hostovani,300+padding*3)

    button2 = vytvorit_tlacitko("Připoj se do hry",pripojeni,430+padding*7)

    button3 = vytvorit_tlacitko("Vypni aplikaci",exit,canvas_height/1.3)

# vyvolá celý program
main_menu()

root.mainloop()
