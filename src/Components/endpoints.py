import customtkinter as ctk
from typing import Type, Callable
from src.Fonts.fonts import Fonts

class Endpoints ():
    def __init__(self, frame: Type[ctk.CTkFrame], set_content: Callable[[str], None], file_path: str) -> None:
        self.file_path = file_path
        self.button = ctk.CTkButton(frame, text=f"In endpoints {file_path}", font=Fonts().body, command=lambda: set_content("home"))
        self.button.pack()