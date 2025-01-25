import customtkinter as ctk # type: ignore
from os import path as os_path
from PIL import Image
from collections.abc import Callable
from src.Fonts.fonts import Fonts

class Home ():
    def __init__(self, frame: ctk.CTkFrame, set_content: Callable[[str], None]) -> None:
        """Creates the home component"""
        self.set_content = set_content
        self.file: str = ""
        
        self.frame: ctk.CTkFrame = ctk.CTkFrame(frame, corner_radius=10)
        
        self.load_logo_image()
                
        self.description_label: ctk.CTkLabel = ctk.CTkLabel(self.frame,
                                                            text='Keep your "endpoints.json" file up to date while developing an API!',
                                                            font=Fonts().header,
                                                            wraplength=500)

        self.open_file_button: ctk.CTkLabel = ctk.CTkButton(self.frame,
                                                            text="Open File",
                                                            font=Fonts().header,
                                                            command=self.select_file,
                                                            width=100,
                                                            height=100,
                                                            corner_radius=50)
        
        self.description_label.pack(pady=10)
        self.open_file_button.pack(pady=10)
        self.logo_label.pack()
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
            
    def load_logo_image(self) -> None:
        """Loads and displays the logo"""
        start_light_path: str = os_path.join(os_path.dirname(__file__), "..", "Assets", "EndpointsJSONLogo-light.png")   
        start_dark_path: str = os_path.join(os_path.dirname(__file__), "..", "Assets", "EndpointsJSONLogo-dark.png")
        
        logo_image: ctk.CTkImage = ctk.CTkImage(light_image=Image.open(start_light_path),
                                                dark_image=Image.open(start_dark_path),
                                                size=(100, 100))
        
        self.logo_label = ctk.CTkLabel(self.frame, image=logo_image, text="")
        
        self.logo_label.pack(pady=10)
            
        
    def select_file(self) -> None:
        """Allows the user to select a file and, if an appropriate file is chosen, displays the data"""
        self.file: str = ctk.filedialog.askopenfilename(title="Select or create the endpoints file",
                                                        initialfile="endpoints.json",
                                                        filetypes=[("JSON", ".JSON .json")])
        
        if self.file != "":
            self.set_content("endpoints")