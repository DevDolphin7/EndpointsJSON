import customtkinter as ctk # type: ignore
import json
from collections.abc import Callable
from src.Typing import AllEndpointsData, EndpointData
from .endpoint import Endpoint
from .addnew import AddNewEndpoint
from src.Utils.utils import get_all_endpoints, get_endpoint_from_user_interaction, reorder_endpoints
from src.Fonts.fonts import Fonts

class Endpoints ():
    def __init__(self, frame: ctk.CTkFrame, set_content: Callable[[str], None], file_path: str) -> None:
        """Creates an endpoints page for the user to view, modify and add endpoints"""
        self.set_content = set_content
        self.file_path = file_path
        self.endpoints: AllEndpointsData = {}
        
        self.utility_frame: ctk.CTkFrame = ctk.CTkFrame(frame, corner_radius=10)        
        self.load_utility_buttons()
        
        self.file_path_label: ctk.CTkLabel = ctk.CTkLabel(self.utility_frame, text=f"Path: {self.file_path}", font=Fonts().body)
        
        self.frame: ctk.CTkScrollableFrame = ctk.CTkScrollableFrame(frame, corner_radius=10)
        self.frame.bind_all("<Button-4>", lambda _: self.frame._parent_canvas.yview("scroll", -1, "units"))
        self.frame.bind_all("<Button-5>", lambda _: self.frame._parent_canvas.yview("scroll", 1, "units"))
              
        self.load_endpoints()
        self.add_new: AddNewEndpoint = AddNewEndpoint(self.frame, self.save_file, self.reload)
        
        self.file_path_label.pack(side=ctk.LEFT, padx=5)      
        self.utility_frame.pack(fill="x", padx=5, pady=5)    
        self.frame.pack(fill="both", expand=True, padx=5, pady=5)
        
    def load_utility_buttons(self) -> None:
        """Loads the home and save buttons"""
        self.home_button: ctk.CTkButton = ctk.CTkButton(self.utility_frame,
                                                              text="🏠",
                                                              font=Fonts().emoji,
                                                              width=50,
                                                              corner_radius=10,
                                                              command=lambda: self.set_content("home"))
        self.home_button.pack(side=ctk.LEFT, padx=5)
        
        self.save_button: ctk.CTkButton = ctk.CTkButton(self.utility_frame,
                                                              text="💾",
                                                              font=Fonts().emoji,
                                                              width=50,
                                                              corner_radius=10,
                                                              command=self.save_file)
        self.save_button.pack(side=ctk.RIGHT, padx=5)
        
    def load_endpoints(self) -> None:
        """Loads all the existing endpoints from the json file and displays them to the user"""
        with open(self.file_path) as json_contents:
            try:
                self.endpoints = json.load(json_contents)
            except json.decoder.JSONDecodeError:
                self.endpoints = {}
            json_contents.close()
        
        endpoint: str; data: EndpointData
        for endpoint, data in self.endpoints.items():
            Endpoint(self.frame, endpoint, data, self.move_endpoint, self.delete_endpoint)
    
    def save_file(self, data_to_save: AllEndpointsData|None=None) -> None:
        """Saves the current state of the app to the json file"""
        if data_to_save:
            self.data_to_save = data_to_save
        else:
            self.data_to_save = get_all_endpoints(self.frame)
        
        with open(self.file_path, "w") as endpoints_json:
            json.dump(self.data_to_save, endpoints_json, indent=2)
            endpoints_json.close()
                                    
    def reload(self) -> None:
        """Reloads the endpoints page to display changes"""
        self.set_content("endpoints")
        
    def move_endpoint(self, direction: str, endpoint: str, data: EndpointData) -> None:
        """Allows the user to move an endpoint"""
        try:
            current_endpoint: str = get_endpoint_from_user_interaction(self.endpoints, endpoint, data)
        except ValueError:
            return
        
        try:
            reordered_endpoints: AllEndpointsData = reorder_endpoints(self.endpoints, current_endpoint, direction, self.frame)
        except IndexError:
            return
        
        self.save_file(data_to_save=reordered_endpoints)
        self.reload()              
                
    def delete_endpoint(self, endpoint: str, data: EndpointData) -> None:
        """Allows the user to delete an endpoint"""
        current_endpoint = get_endpoint_from_user_interaction(self.endpoints, endpoint, data)
        
        all_endoints = get_all_endpoints(self.frame)
        all_endoints.pop(current_endpoint, None)
        
        self.save_file(data_to_save=all_endoints)
        self.reload() 