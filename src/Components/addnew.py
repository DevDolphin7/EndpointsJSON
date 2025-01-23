import customtkinter as ctk
from typing import Type, Callable, Any
from src.Fonts.fonts import Fonts

class AddNewEndpoint ():
    def __init__(self, frame: Type[ctk.CTkFrame], save_file: Callable[[None], None], reload: Callable[[None], None]) -> None:
        self.save_file = save_file
        self.reload = reload
        self.text_vars = []
        
        self.frame = ctk.CTkFrame(frame)
        
        self.add_button = self.load_add_button(self.frame, self.check_add_new_endpoint)
        
        self.add_button.pack(side=ctk.TOP, padx=5)        
        self.frame.pack(fill="x", expand=True, padx=5, pady=5)  
        
    def load_add_button(self, frame: Type[ctk.CTkFrame], callback: Callable[[Any], Any]) -> Type[ctk.CTkButton]:
        return ctk.CTkButton(frame,
                             text="➕",
                             font=Fonts().emoji,
                             width=50,
                             corner_radius=10,
                             command=callback)
        
    def check_add_new_endpoint(self) -> None:
        for widget in self.frame.winfo_children():
            if isinstance(widget, ctk.CTkFrame):
                self.save_file()
                self.reload()
                return
        
        self.load_add_new_endpoint()
        
    def load_add_new_endpoint(self) -> None:
        self.text_vars.append(ctk.StringVar(self.frame, "GET"))
        self.text_vars.append(ctk.StringVar(self.frame))
        
        frame = ctk.CTkFrame(self.frame, corner_radius=10)
            
        self.method_menu = ctk.CTkOptionMenu(frame, values=["GET", "POST", "PATCH", "PUT", "DELETE"], variable=self.text_vars[len(self.text_vars) - 2], font=Fonts().body)
        
        self.endpoint_entry = ctk.CTkEntry(frame, textvariable=self.text_vars[len(self.text_vars) - 1], width=200, font=Fonts().body)
        
        self.add_info_button = self.load_add_button(frame, self.load_add_new_info)
            
        self.method_menu.pack(side=ctk.LEFT, padx=5)
        self.endpoint_entry.pack(side=ctk.LEFT, padx=5)
        self.add_info_button.pack(side=ctk.RIGHT)
        frame.pack(fill="x", expand=True, padx=5, ipady=5)
        
        
    def load_add_new_info(self) -> None:
        for _ in range(2):
            self.text_vars.append(ctk.StringVar(self.frame))
        
        frame = ctk.CTkFrame(self.frame)
        
        title_index = len(self.text_vars) - 2
        title = ctk.CTkEntry(frame, textvariable=self.text_vars[title_index], width=140, font=Fonts().body)
        info = ctk.CTkEntry(frame, textvariable=self.text_vars[title_index + 1], font=Fonts().body)
        remove_button = ctk.CTkButton(frame,
                                      text="🗑️",
                                      font=Fonts().emoji,
                                      width=50,
                                      corner_radius=10,
                                      fg_color="#e8292e",
                                      hover_color="#b02024",
                                      command=lambda: self.delete_info(frame, title_index))
        
        title.pack(side=ctk.LEFT, padx=5)
        info.pack(side=ctk.LEFT, fill="x", expand=True, padx=5)
        remove_button.pack(side=ctk.RIGHT)
        frame.pack(fill="x", expand=True, padx=5, ipady=5)
        
    def delete_info(self, frame: Type[ctk.CTkFrame], starting_index: int):      
        for _ in range(2):
            self.text_vars.pop(starting_index)
        
        frame.destroy()