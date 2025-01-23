import ast
from typing import Type
from customtkinter import CTkFrame, CTkTabview, CTkOptionMenu, CTkEntry

def get_all_endpoints(frame: CTkFrame) -> dict[str, str|dict|list]:
    data_to_save = {}
    method, current_endpoint, current_info = "", "", ""
    
    def format_endpoint_data(widget, data_to_save, method, current_endpoint, current_info):
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
        
        return [data_to_save, method, current_endpoint, current_info]
    
    for app_widget in frame.winfo_children():
        if isinstance(app_widget, CTkFrame):
            for endpoints_widget in app_widget.winfo_children():
                if isinstance(endpoints_widget, CTkTabview):
                    tabview_frame: Type[CTkFrame]
                    for tabview_frame in endpoints_widget.tab("Detail").winfo_children():
                        for widget in tabview_frame.winfo_children():
                            data_to_save, method, current_endpoint, current_info = format_endpoint_data(widget, data_to_save, method, current_endpoint, current_info)
                else:
                    if isinstance(endpoints_widget, CTkFrame):
                        widget: CTkOptionMenu|CTkEntry
                        for widget in endpoints_widget.winfo_children():
                            data_to_save, method, current_endpoint, current_info = format_endpoint_data(widget, data_to_save, method, current_endpoint, current_info)
                    
    return data_to_save

def get_endpoint_from_user_interaction(endpoints: dict[str, str|list|dict], endpoint: str, data: dict[str, str|list|dict]) -> str:
    for original_endpoint, original_data in endpoints.items():
        if endpoint == original_endpoint and data == original_data:
            return endpoint

def reorder_endpoints(endpoints: dict[str, str|list|dict], current_endpoint: str, direction: str, frame: Type[CTkFrame]) -> Type[IndexError]|dict[str, str|list|dict]:
    if direction == "up":
        index_direction = -1
    elif direction == "down":
        index_direction = 1
    
    endpoints: list[str] = list(endpoints.keys())
    current_index = endpoints.index(current_endpoint)
    new_index = current_index + index_direction
    
    if (new_index < 0) or (new_index == len(endpoints)):
        raise IndexError(f"The new index {new_index} is our of range 0-{len(endpoints)-1}")
    
    all_endoints = get_all_endpoints(frame)
    
    endpoint_key = endpoints.pop(current_index)
    endpoints.insert(new_index, endpoint_key)
    
    reordered_endpoints = {key: all_endoints[key] for key in endpoints}
    
    return reordered_endpoints