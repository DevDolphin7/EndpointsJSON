import customtkinter as ctk # type: ignore
from collections.abc import Callable
from src.Fonts.fonts import Fonts

class AddNewEndpoint ():
    def __init__(self, frame: ctk.CTkFrame, save_file: Callable[[], None], reload: Callable[[], None]) -> None:
        """Adds a component to allow the user to create a new endpoint"""
        self.save_file = save_file
        self.reload = reload
        self.text_vars: list[ctk.StringVar] = []
        
        self.frame: ctk.CTkFrame = ctk.CTkFrame(frame)
        
        self.add_button: ctk.CTkButton = self.load_add_button(self.frame, self.check_add_new_endpoint)
        
        self.add_button.pack(side=ctk.TOP, padx=5)        
        self.frame.pack(fill="x", expand=True, padx=5, pady=5)  
        
    def load_add_button(self, frame: ctk.CTkFrame, callback: Callable) -> ctk.CTkButton:
        """Returns the add new button"""
        return ctk.CTkButton(frame,
                             text="➕",
                             font=Fonts().emoji,
                             width=50,
                             corner_radius=10,
                             command=callback)
        
    def check_add_new_endpoint(self) -> None:
        """Check if the add_new_endpoint frame already exists when the add button is clicked,
           either create the add new endpoint frame OR add the endpoint instead"""
        widget: ctk.CTkFrame|ctk.CTkButton|ctk.CTkEntry|ctk.CTkOptionMenu|ctk.CTkLabel
        for widget in self.frame.winfo_children():
            if isinstance(widget, ctk.CTkFrame):
                # If the add_new_endpoint frame already exists and the button is clicked again,
                # add the endpoint instead of creating the frame
                self.save_file()
                self.reload()
                return
        
        self.load_add_new_endpoint()
        
    def load_add_new_endpoint(self) -> None:
        """If the add button is clicked for the first time, create the frame to add a new endpoint."""
        self.text_vars.append(ctk.StringVar(self.frame, "GET"))
        self.text_vars.append(ctk.StringVar(self.frame))
        
        frame: ctk.CTkFrame = ctk.CTkFrame(self.frame, corner_radius=10)
        
        last_text_var_index: int = len(self.text_vars) - 1
            
        self.method_menu: ctk.CTkOptionMenu = ctk.CTkOptionMenu(frame,
                                                                values=["GET", "POST", "PATCH", "PUT", "DELETE"],
                                                                variable=self.text_vars[last_text_var_index - 1],
                                                                font=Fonts().body)
        
        self.endpoint_entry: ctk.CTkEntry = ctk.CTkEntry(frame,
                                                         textvariable=self.text_vars[last_text_var_index],
                                                         width=200,
                                                         font=Fonts().body)
        
        self.add_info_button: ctk.CTkButton = self.load_add_button(frame, self.load_add_new_info)
            
        self.method_menu.pack(side=ctk.LEFT, padx=5)
        self.endpoint_entry.pack(side=ctk.LEFT, padx=5)
        self.add_info_button.pack(side=ctk.RIGHT)
        frame.pack(fill="x", expand=True, padx=5, ipady=5)
     
    def load_add_new_info(self) -> None:
        """Add ability for user to insert further information about the new endpoint"""
        for _ in range(2):
            self.text_vars.append(ctk.StringVar(self.frame))
        
        frame: ctk.CTkFrame = ctk.CTkFrame(self.frame)
        
        title_index: int = len(self.text_vars) - 2
        
        title: ctk.CTkEntry = ctk.CTkEntry(frame, textvariable=self.text_vars[title_index], width=140, font=Fonts().body)
        
        info: ctk.CTkEntry = ctk.CTkEntry(frame, textvariable=self.text_vars[title_index + 1], font=Fonts().body)
        
        remove_button: ctk.CTkButton = ctk.CTkButton(frame,
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
        
    def delete_info(self, frame: ctk.CTkFrame, starting_index: int) -> None:
        """Delete a frame where the user could insert further information about the new endpoint"""      
        for _ in range(2):
            self.text_vars.pop(starting_index)
        
        frame.destroy()