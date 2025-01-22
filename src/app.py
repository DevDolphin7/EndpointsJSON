import customtkinter as ctk
from Components import Home, Endpoints, Help

ctk.set_default_color_theme("green")

class EndpointsJSON (ctk.CTk):
    def __init__(self) -> None:
        super().__init__()
        
        self.title("Endpoints JSON")
        self.geometry("640x480")
        self.resizable(width=False, height=False)
        
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.content = "home"
        
        self.mainloop()
        
    @property
    def content(self) -> str:
        return self._content
    
    @content.setter
    def content(self, content: str) -> None:
        valid_content = ["home", "endpoints"]
        if content in valid_content:
            self._content = content
            self.remove_content()
            self.load_content()
            
    def set_content(self, content: str) -> None:
        self.content = content
        
    def remove_content(self) -> None:
        for widget in self.frame.winfo_children():
            widget.destroy()

    def load_content(self) -> None:
        match self.content:
            case "home":
                self.home = Home(self.frame, self.set_content)
            
            case "endpoints":
                self.endpoints = Endpoints(self.frame, self.set_content, self.home.file)
        
        self.help = Help(self.frame)


if __name__ == "__main__":
    EndpointsJSON()