import customtkinter as ctk # type: ignore
from os import path as os_path
from PIL import ImageTk
from src.Components import Home, Endpoints, Help

ctk.set_default_color_theme("green")

class EndpointsJSON (ctk.CTk):
    def __init__(self) -> None:
        """Initialise the app by calling EndpointsJSON()"""
        super().__init__()
        
        self.title("Endpoints JSON")
        self.geometry("640x480")
        self.set_logo()
        
        self.frame: ctk.CTkFrame = ctk.CTkFrame(self)
        self.frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.content: str = "home"
        
        self.mainloop()
        
    @property
    def content(self) -> str:
        return self._content
    
    @content.setter
    def content(self, content: str) -> None:
        valid_content: list[str] = ["home", "endpoints"]
        if content in valid_content:
            self._content: str = content
            self.remove_content()
            self.load_content()
            
    def set_logo(self) -> None:
        """Sets the logo in the icon bar on Linux systems"""
        logo_dark_path: str = os_path.join(os_path.dirname(__file__), "Assets", "EndpointsJSONLogo-dark.png")
 
        logo_dark: ImageTk.PhotoImage = ImageTk.PhotoImage(file=logo_dark_path)
        
        self.iconphoto(False, logo_dark)
            
    def set_content(self, content: str) -> None:
        """Sets the content to be displayed to the user"""
        self.content: str = content
        
    def remove_content(self) -> None:
        """Removes the current loaded content"""
        widget: ctk.CTkFrame
        for widget in self.frame.winfo_children():
            widget.destroy()

    def load_content(self) -> None:
        """Loads the currently set content"""
        match self.content:
            case "home":
                self.home: Home = Home(self.frame, self.set_content)
            
            case "endpoints":
                self.endpoints: Endpoints = Endpoints(self.frame, self.set_content, self.home.file)
        
        self.help: Help = Help(self.frame)


if __name__ == "__main__":
    EndpointsJSON()