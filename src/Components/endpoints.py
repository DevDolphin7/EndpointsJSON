import customtkinter as ctk

class Endpoints ():
    def __init__(self, frame, set_content):
        self.button = ctk.CTkButton(frame, text="In endpoints", command=lambda: set_content("home"))
        self.button.pack()