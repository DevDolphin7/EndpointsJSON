import customtkinter as ctk
import webbrowser
from typing import Type
from src.Fonts.fonts import Fonts

class Help ():
    def __init__(self, frame: Type[ctk.CTkFrame]) -> None:
        self.frame = ctk.CTkFrame(frame, corner_radius=10)
        
        self.label = ctk.CTkLabel(self.frame,
                                  text='For help or to get in contact, visit ',
                                  font=Fonts().footer)
        
        self.hyperlink = ctk.CTkLabel(self.frame,
                                  text='DevDolphin7 on GitHub',
                                  font=Fonts().footer_link)
        self.hyperlink.bind("<Button-1>", lambda _: webbrowser.open_new("https://github.com/DevDolphin7/EndpointsJSON"))
        
        self.light_dark_mode_var = ctk.StringVar(value="light")
        self.light_dark_mode = ctk.CTkSwitch(self.frame,
                                             text="🌒 / 🔆",
                                             font=Fonts().emoji,
                                             command=self.set_light_dark_mode,
                                             variable=self.light_dark_mode_var,
                                             onvalue="light",
                                             offvalue="dark")
        
        self.label.pack(side=ctk.LEFT, padx=5)
        self.hyperlink.pack(side=ctk.LEFT)
        self.light_dark_mode.pack(side=ctk.RIGHT, padx=10)
        
        self.frame.pack(side=ctk.BOTTOM, fill="x")
        
    def set_light_dark_mode(self) -> None:
        ctk.set_appearance_mode(self.light_dark_mode_var.get())