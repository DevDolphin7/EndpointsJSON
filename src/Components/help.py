import customtkinter as ctk
import webbrowser
from typing import Type
from src.Fonts.fonts import Fonts

class Help ():
    def __init__(self, frame: Type[ctk.CTkFrame]) -> None:
        self.label = ctk.CTkLabel(frame,
                                  text='For help or to get in contact, visit ',
                                  font=Fonts().footer)
        
        self.hyperlink = ctk.CTkLabel(frame,
                                  text='DevDolphin7 on GitHub',
                                  font=Fonts().footer)
        self.hyperlink.bind("<Button-1>", lambda _: webbrowser.open_new("https://github.com/DevDolphin7/EndpointsJSON"))
        
        self.label.pack()
        self.hyperlink.pack()