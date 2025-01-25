import customtkinter as ctk # type: ignore
from os import path as os_path

emoji_font_path: str = os_path.join(os_path.dirname(__file__), "Noto_Emoji", "NotoEmoji-VariableFont_wght.ttf")
ctk.FontManager.load_font(emoji_font_path)

class Fonts():
    def __init__(self) -> None:
        self.header: ctk.CTkFont = ctk.CTkFont(family="Helvetica", size=20)
        self.emoji: ctk.CTkFont = ctk.CTkFont(family="NotoEmoji-VariableFont_wght", size=20)
        self.body: ctk.CTkFont = ctk.CTkFont(family="Helvetica", size=13)
        self.footer: ctk.CTkFont = ctk.CTkFont(family="Helvetica", size=11)
        self.footer_link: ctk.CTkFont = ctk.CTkFont(family="Helvetica", size=12, underline=True, weight="bold")