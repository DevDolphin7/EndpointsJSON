import customtkinter as ctk
import webbrowser

class Help ():
    def __init__(self, frame):
        self.label = ctk.CTkLabel(frame,
                                  text='For help or to get in contact, visit ',
                                  fg_color="transparent")
        
        self.hyperlink = ctk.CTkLabel(frame,
                                  text='DevDolphin7 on GitHub',
                                  fg_color="transparent")
        self.hyperlink.bind("<Button-1>", lambda event: webbrowser.open_new("https://github.com/DevDolphin7/EndpointsJSON"))
        
        self.label.pack()
        self.hyperlink.pack()