import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        fontsize=80
        
        def vytvorit_tlacitko(text,command,y):
            btn = customtkinter.CTkButton(self, text=text,
                                             fg_color='#677279',
                                             font=("Open Sans", fontsize),
                                             height=fontsize+50,
                                             width=fontsize+100,
                                             corner_radius=150,
                                             command=command,
                                             cursor="hand2",
                                             hover_color="#4B5358",
                                             border_width=5).grid(row=1, column=0, padx=0, pady=y)
            return btn
        
        customtkinter.set_appearance_mode("system")
        self.title("Desítka score")
        self.geometry("540x960")
        self.grid_columnconfigure(0, weight=1)
        
        vytvorit_tlacitko("Připoj se",0,100)
app = App()

app.mainloop()

