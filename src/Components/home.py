from os import path as os_path
import customtkinter as ctk
from typing import Type, Callable
from src.Fonts.fonts import Fonts

class Home ():
    def __init__(self, frame: Type[ctk.CTkFrame], set_content: Callable[[str], None]) -> None:
        self.set_content = set_content
        self.file = ""
        
        self.frame = ctk.CTkFrame(frame, corner_radius=10)
        
        self.label = ctk.CTkLabel(self.frame,
                                  text='Keep your "endpoints.json" file up to date while developing an API!',
                                  font=Fonts().header,
                                  wraplength=500)
        

        self.button = ctk.CTkButton(self.frame, text="Open file", font=Fonts().body, command=self.select_file, width=100, height=100, corner_radius=50)
        
        self.label.pack(pady=10)
        self.button.pack(pady=10)
        self.frame.pack(fill="x", expand=True, padx=20)
        
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