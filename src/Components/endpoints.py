import customtkinter as ctk
import json, ast
from typing import Type, Callable
from .endpoint import Endpoint
from src.Fonts.fonts import Fonts

class Endpoints ():
    def __init__(self, frame: Type[ctk.CTkFrame], set_content: Callable[[str], None], file_path: str) -> None:
        self.set_content = set_content
        self.file_path = file_path
        self.endpoints = {}
        self.endpoints_data = {}
        
        self.utility_frame = ctk.CTkFrame(frame, corner_radius=10)        
        self.load_utility_buttons()
        
        self.frame = ctk.CTkScrollableFrame(frame, corner_radius=10)
              
        self.load_endpoints()
        
        self.utility_frame.pack(fill="x", padx=5, pady=5)    
        self.frame.pack(fill="both", expand=True, padx=5, pady=5)
        
    def load_utility_buttons(self) -> None:        
        self.home_button = ctk.CTkButton(self.utility_frame, text="🏠", font=Fonts().emoji, width=50, command=lambda: self.set_content("home"))
        self.home_button.pack(side=ctk.LEFT, padx=5)
        
        self.save_button = ctk.CTkButton(self.utility_frame, text="💾", font=Fonts().emoji, width=50, command=self.save_file)
        self.save_button.pack(side=ctk.RIGHT, padx=5)
        
    def load_endpoints(self) -> None:
        with open(self.file_path) as json_contents:
            self.endpoints: dict = json.load(json_contents)
            json_contents.close()
            
        print(self.endpoints)
            
        for endpoint, data in self.endpoints.items():
            Endpoint(self.frame, endpoint, data)
            
    def remove_endpoints(self) -> None:
        pass
    
    def save_file(self) -> None:
        self.get_data_to_save()
        
        with open(self.file_path, "w") as endpoints_json:
            json.dump(self.data_to_save, endpoints_json, indent=4)
            endpoints_json.close()
        
    def get_data_to_save(self) -> None:
        self.data_to_save = {}
        method, current_endpoint, current_info = "", "", ""
        
        for app_widget in self.frame.winfo_children():
            if isinstance(app_widget, ctk.CTkFrame):
                tabview: Type[ctk.CTkTabview]
                for tabview in app_widget.winfo_children():
                    tabview_frame: Type[ctk.CTkFrame]
                    for tabview_frame in tabview.tab("Detail").winfo_children():
                        for widget in tabview_frame.winfo_children():
                            if isinstance(widget, ctk.CTkOptionMenu):
                                method = widget.get()
                            if isinstance(widget, ctk.CTkEntry):
                                if method != "":
                                    current_endpoint = f"{method} {widget.get()}"
                                    self.data_to_save[current_endpoint] = {}
                                    method, current_info = "", ""
                                elif current_info == "":
                                    current_info = widget.get()
                                    self.data_to_save[current_endpoint][current_info] = None
                                else:
                                    data = widget.get()
                                                                      
                                    if data[0] in ["{", "[", "("]:
                                        data = ast.literal_eval(data)

                                    self.data_to_save[current_endpoint][current_info] = data
                                    current_info = ""