import ast
from typing import Type
from customtkinter import CTkFrame, CTkTabview, CTkOptionMenu, CTkEntry

def get_all_endpoints(frame: CTkFrame) -> dict[str, str|dict|list]:
    data_to_save = {}
    method, current_endpoint, current_info = "", "", ""
    
    for app_widget in frame.winfo_children():
        if isinstance(app_widget, CTkFrame):
            tabview: Type[CTkTabview]
            for tabview in app_widget.winfo_children():
                tabview_frame: Type[CTkFrame]
                for tabview_frame in tabview.tab("Detail").winfo_children():
                    for widget in tabview_frame.winfo_children():
                        if isinstance(widget, CTkOptionMenu):
                            method = widget.get()
                        elif isinstance(widget, CTkEntry):
                            if method != "":
                                current_endpoint = f"{method} {widget.get()}"
                                data_to_save[current_endpoint] = {}
                                method, current_info = "", ""
                            elif current_info == "":
                                current_info = widget.get()
                                data_to_save[current_endpoint][current_info] = None
                            else:
                                data = widget.get()
                                                                    
                                if data[0] in ["{", "[", "("]:
                                    data = ast.literal_eval(data)

                                data_to_save[current_endpoint][current_info] = data
                                current_info = ""
    
    return data_to_save