import customtkinter as ctk
import os

emoji_font_path = os.path.join(os.path.dirname(__file__), "Noto_Emoji", "NotoEmoji-VariableFont_wght.ttf")
ctk.FontManager.load_font(emoji_font_path)

class Fonts():
    def __init__(self):
        self.header = ctk.CTkFont(family="Helvetica", size=20)
        self.emoji = ctk.CTkFont(family="NotoEmoji-VariableFont_wght", size=20)
        self.body = ctk.CTkFont(family="Helvetica", size=13)
        self.footer = ctk.CTkFont(family="Helvetica", size=11)
        self.footer_link = ctk.CTkFont(family="Helvetica", size=12, underline=True, weight="bold")