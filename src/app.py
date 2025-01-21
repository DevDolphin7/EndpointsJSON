import customtkinter as ctk
from Components import Home, Endpoints, Help

class EndpointsJSON (ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Endpoints JSON")
        self.geometry("640x480")
        
        self.frame = ctk.CTkFrame(self)
        self.frame.pack(fill="both", padx=20, pady=20)
        
        self.content = "home"
        
        self.mainloop()
        
    @property
    def content(self):
        return self._content
    
    @content.setter
    def content(self, content):
        valid_content = ["home", "endpoints"]
        if content in valid_content:
            self._content = content
            self.remove_content()
            self.load_content()
            
    def set_content(self, content):
        self.content = content
        
    def remove_content(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def load_content(self):
        match self.content:
            case "home":
                self.home = Home(self.frame, self.set_content)
            
            case "endpoints":
                self.endpoints = Endpoints(self.frame, self.set_content)
        
        self.help = Help(self.frame)


if __name__ == "__main__":
    EndpointsJSON()