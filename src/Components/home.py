import customtkinter as ctk

class Home ():
    def __init__(self, frame, set_content):
        self.label = ctk.CTkLabel(frame,
                                  text='This app is designed to help you keep an "endpoints.json" file up to date while developing a back-end / server!',
                                  fg_color="transparent")
        self.label.pack()

        self.button = ctk.CTkButton(frame, text="In home", command=lambda: set_content("endpoints"))
        self.button.pack()