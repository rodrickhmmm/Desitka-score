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
        image = image.resize((500, 120))  # Změna velikosti zde
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

# header 
def header():
    canvas.create_rectangle(0,0,canvas_width,220+padding,fill="#545D63")
    canvas.create_image(canvas_width/2,50+padding,image=pic)
    canvas.create_text(canvas_width/2,160+padding,text="SCORE",fill="black", font=("Open Sans", 70, "bold" ))

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
        font=("Open Sans", 50),
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

# Scena(?) s hostovanim hry
def hostovani():
    global button4
    clearnutigui()
    
    header()
    
    canvas.create_text(canvas_width/2,300+padding,text="Hostování skóre",fill="white", font=("Open Sans", 40, "bold" ))
    canvas.create_text(canvas_width/2,350+padding,text="Počkej, než se napojí všichni hráči",fill="white", font=("Open Sans", 20,))
    button4 = vytvorit_tlacitko("Zpátky do menu",main_menu,900)

# Scena(?) s pripojenim do hry
def pripojeni():
    global button4, entry, button3
    clearnutigui()
    
    header()

    padding2=100
    
    entry = customtkinter.CTkEntry(canvas, placeholder_text="Jméno", width=455, fg_color="#677279",font=("Open Sans", 50),placeholder_text_color="#d6d6d6")
    entry.place(x=40,y=220+padding*3+padding2)
    
    canvas.create_rectangle(20,300,canvas_width-20,500+padding2,fill="#545D63")
    
    canvas.create_text(canvas_width/2,320+padding,text="Zadej své jméno",fill="white", font=("Open Sans", 40, "bold" ))
    
    button3 = vytvorit_tlacitko("Připojit se",0,570)
    
    button4 = vytvorit_tlacitko("Zpátky do menu",main_menu,900)
    
# Main scene
def main_menu():
    global button1, button2, button3, button4, entry
    
    clearnutigui()
    
    header()

    button1 = vytvorit_tlacitko("Hostuj hru",hostovani,300)

    button2 = vytvorit_tlacitko("Připoj se do hry",pripojeni,430)

    button3 = vytvorit_tlacitko("Vypni aplikaci",exit,600)

# vyvolá celý program
main_menu()

root.mainloop()