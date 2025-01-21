from os import path as os_path
import customtkinter as ctk
from typing import Type, Callable
from src.Fonts.fonts import Fonts

class Home ():
    def __init__(self, frame: Type[ctk.CTkFrame], set_content: Callable[[str], None]) -> None:
        self.set_content = set_content
        self.file = ""
        
        self.label = ctk.CTkLabel(frame,
                                  text='This app is designed to help you keep an "endpoints.json" file up to date while developing a back-end / server!',
                                  font=Fonts().header,
                                  wraplength=600)
        self.label.pack()

        self.button = ctk.CTkButton(frame, text="In home", font=Fonts().body, command=self.select_file)
        self.button.pack()
        
    @property
    def file(self) -> str:
        return self._file
    
    @file.setter
    def file(self, path: str) -> None:
        if path == "" or not os_path.exists(path) or path[-5:].lower() != ".json":
            self._file = ""
        else:
            self._file = path
            
        
    def select_file(self) -> None:
        self.file = ctk.filedialog.askopenfilename(
            title="Select or create the endpoints file",
            initialfile="endpoints.json",
            filetypes=[("JSON", ".JSON .json")]
        )
        
        if self.file != "":
            self.set_content("endpoints")