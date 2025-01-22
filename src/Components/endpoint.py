import customtkinter as ctk
from typing import Type, Callable
from src.Fonts.fonts import Fonts

class Endpoint ():
    def __init__(self, frame: Type[ctk.CTkFrame], endpoint: str, data: dict[str, str|list|dict]) -> None:
        self.method, self.endpoint = endpoint.split(" ")
        self.data = data
        
        self.frame = ctk.CTkFrame(frame, corner_radius=10)
        
        self.tab_view = ctk.CTkTabview(self.frame, height=70, anchor="e")
        self.endpoint_tab = self.tab_view.add("Overview")
        self.detail_tab = self.tab_view.add("Detail")
        self.tab_view.set("Overview")
        
        self.load_tab_endpoint_info()
        self.load_detail_tab()
        
        
        self.tab_view.pack(fill="x", padx=5, pady=5)
        self.frame.pack(fill="x", padx=5, pady=5)
        
    def load_tab_endpoint_info(self) -> None:
        self.method_menu_var = ctk.StringVar(self.frame, self.method)
        self.endpoint_entry_var = ctk.StringVar(self.frame, self.endpoint)
        
        for tab in [self.endpoint_tab, self.detail_tab]:
            frame = ctk.CTkFrame(tab, corner_radius=10)
            
            self.method_menu = ctk.CTkOptionMenu(frame, values=["GET", "POST", "PATCH", "PUT", "DELETE"], variable=self.method_menu_var)
            
            self.endpoint_entry = ctk.CTkEntry(frame, textvariable=self.endpoint_entry_var, width=200)
            
            if tab.winfo_name() == "!ctkframe":
                self.method_menu.configure(state="disabled")
                self.endpoint_entry.configure(state="disabled")
                
            self.method_menu.pack(side=ctk.LEFT, padx=5)
            self.endpoint_entry.pack(side=ctk.LEFT, padx=5)
            frame.pack(fill="x", expand=True, ipady=5)
            
    def load_detail_tab(self) -> None:
        for title, info in self.data.items():       
            title_var = ctk.StringVar(self.frame, title)
            info_var = ctk.StringVar(self.frame, str(info))

            frame = ctk.CTkFrame(self.detail_tab, corner_radius=10)            
            title_entry = ctk.CTkEntry(frame, textvariable=title_var, width=140)
            info_entry = ctk.CTkEntry(frame, textvariable=info_var, width=360)
            
            title_entry.pack(side=ctk.LEFT, padx=5)
            info_entry.pack(side=ctk.LEFT, padx=5)
            frame.pack(fill="x", expand=True, ipady=5)