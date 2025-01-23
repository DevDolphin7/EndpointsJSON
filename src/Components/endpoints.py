import customtkinter as ctk
import json
from typing import Type, Callable
from .endpoint import Endpoint
from .addnew import AddNewEndpoint
from src.Utils.utils import get_all_endpoints, get_endpoint_from_user_interaction, reorder_endpoints
from src.Fonts.fonts import Fonts

class Endpoints ():
    def __init__(self, frame: Type[ctk.CTkFrame], set_content: Callable[[str], None], file_path: str) -> None:
        self.set_content = set_content
        self.file_path = file_path
        self.endpoints = {}
        self.endpoints_data = {}
        
        self.utility_frame = ctk.CTkFrame(frame, corner_radius=10)        
        self.load_utility_buttons()
        
        self.file_path_label = ctk.CTkLabel(self.utility_frame, text=f"Path: {self.file_path}", font=Fonts().body)
        
        self.frame = ctk.CTkScrollableFrame(frame, corner_radius=10)
        self.frame.bind_all("<Button-4>", lambda e: self.frame._parent_canvas.yview("scroll", -1, "units"))
        self.frame.bind_all("<Button-5>", lambda e: self.frame._parent_canvas.yview("scroll", 1, "units"))
              
        self.load_endpoints()
        self.add_new = AddNewEndpoint(self.frame, self.save_file, self.reload)
        
        self.file_path_label.pack(side=ctk.LEFT, padx=5)      
        self.utility_frame.pack(fill="x", padx=5, pady=5)    
        self.frame.pack(fill="both", expand=True, padx=5, pady=5)
        
    def load_utility_buttons(self) -> None:        
        self.home_button = ctk.CTkButton(self.utility_frame,
                                         text="🏠",
                                         font=Fonts().emoji,
                                         width=50,
                                         corner_radius=10,
                                         command=lambda: self.set_content("home"))
        self.home_button.pack(side=ctk.LEFT, padx=5)
        
        self.save_button = ctk.CTkButton(self.utility_frame,
                                         text="💾",
                                         font=Fonts().emoji,
                                         width=50,
                                         corner_radius=10,
                                         command=self.save_file)
        self.save_button.pack(side=ctk.RIGHT, padx=5)
        
    def load_endpoints(self) -> None:
        with open(self.file_path) as json_contents:
            try:
                self.endpoints: dict = json.load(json_contents)
            except json.decoder.JSONDecodeError:
                self.endpoints: dict = {}
            json_contents.close()
            
        for endpoint, data in self.endpoints.items():
            Endpoint(self.frame, endpoint, data, self.move_endpoint, self.delete_endpoint)
    
    def save_file(self, data_to_save: dict[str, str|list|dict]=None) -> None:
        if data_to_save:
            self.data_to_save = data_to_save
        else:
            self.data_to_save = get_all_endpoints(self.frame)
        
        with open(self.file_path, "w") as endpoints_json:
            json.dump(self.data_to_save, endpoints_json, indent=2)
            endpoints_json.close()
                                    
    def reload(self) -> None:
        self.set_content("endpoints")
        
    def move_endpoint(self, direction: str, endpoint: str, data: dict[str, str|list|dict]) -> None:
        current_endpoint = get_endpoint_from_user_interaction(self.endpoints, endpoint, data)
        
        try:
            reordered_endpoints = reorder_endpoints(self.endpoints, current_endpoint, direction, self.frame)
        except IndexError:
            return
        
        self.save_file(data_to_save=reordered_endpoints)
        self.reload()              
                
    def delete_endpoint(self, endpoint: str, data: dict[str, str|list|dict]) -> None:
        current_endpoint = get_endpoint_from_user_interaction(self.endpoints, endpoint, data)
        
        all_endoints = get_all_endpoints(self.frame)
        all_endoints.pop(current_endpoint, None)
        
        self.save_file(data_to_save=all_endoints)
        self.reload() 