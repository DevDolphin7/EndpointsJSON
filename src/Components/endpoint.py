import customtkinter as ctk
from typing import Type, Callable
from src.Fonts.fonts import Fonts

class Endpoint ():
    def __init__(self,
                 frame: Type[ctk.CTkFrame],
                 endpoint: str, data: dict[str, str|list|dict],
                 move_endpoint: Callable[[str, str, dict[str, str|list|dict]], None],
                 delete_endpoint: Callable[[str, dict[str, str|list|dict]], None]):
        self.full_endpoint = endpoint
        self.method, *self.endpoint = endpoint.split(" ")
        self.data = data
        self.move_endpoint = move_endpoint
        self.delete_endpoint = delete_endpoint
        
        self.frame = ctk.CTkFrame(frame, corner_radius=10)
        
        self.tab_view = ctk.CTkTabview(self.frame, height=70, anchor="e", border_width=2, border_color="green")
        self.endpoint_tab = self.tab_view.add("Overview")
        self.detail_tab = self.tab_view.add("Detail")
        self.set_tab = self.tab_view.add("Set")
        self.tab_view.set("Overview")
        
        self.load_tab_endpoint_info()
        self.load_detail_tab()
        self.load_set_tab()
        
        self.tab_view.pack(fill="x", padx=5, pady=5)
        self.frame.pack(fill="x", padx=5, pady=5)
        
    def load_tab_endpoint_info(self) -> None:
        self.method_menu_var = ctk.StringVar(self.frame, self.method)
        self.endpoint_entry_var = ctk.StringVar(self.frame, self.endpoint)
        
        for tab in [self.endpoint_tab, self.detail_tab, self.set_tab]:
            frame = ctk.CTkFrame(tab, corner_radius=10)
            
            self.method_menu = ctk.CTkOptionMenu(frame, values=["GET", "POST", "PATCH", "PUT", "DELETE"], variable=self.method_menu_var, font=Fonts().body)
            
            self.endpoint_entry = ctk.CTkEntry(frame, textvariable=self.endpoint_entry_var, width=200, font=Fonts().body)
            
            if tab.winfo_name() in ["!ctkframe", "!ctkframe3"]:
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
            info_entry = ctk.CTkEntry(frame, textvariable=info_var)
            
            title_entry.pack(side=ctk.LEFT, padx=5)
            info_entry.pack(side=ctk.LEFT, padx=5, fill="x", expand=True)
            frame.pack(fill="x", expand=True, ipady=5)
            
    def load_set_tab(self) -> None:
        up_button = ctk.CTkButton(self.set_tab,
                                  text="🔼",
                                  font=Fonts().emoji,
                                  width=50,
                                  corner_radius=10,
                                  command=lambda: self.move_endpoint("up", self.full_endpoint, self.data))
        up_button.pack(side=ctk.RIGHT)
        
        down_button = ctk.CTkButton(self.set_tab,
                                    text="🔽",
                                    font=Fonts().emoji,
                                    width=50,
                                    corner_radius=10,
                                    command=lambda: self.move_endpoint("down", self.full_endpoint, self.data))
        down_button.pack(side=ctk.RIGHT, padx=5)
        
        delete_button = ctk.CTkButton(self.set_tab,
                                      text="🗑️",
                                      font=Fonts().emoji,
                                      width=50,
                                      corner_radius=10,
                                      fg_color="#e8292e",
                                      hover_color="#b02024",
                                      command=lambda: self.delete_endpoint(self.full_endpoint, self.data))
        delete_button.pack(side=ctk.LEFT)