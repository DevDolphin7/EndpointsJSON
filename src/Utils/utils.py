import ast
from src.Typing import AllEndpointsData, EndpointData, AnyCTkWidget
import customtkinter as ctk # type: ignore

def get_all_endpoints(frame: ctk.CTkFrame) -> AllEndpointsData:
    """Gets and compiles the data of all the endpoints currently shown in the app"""
    all_endpoints: AllEndpointsData = {}
    method: str; current_endpoint: str; current_info: str
    method, current_endpoint, current_info = [""] * 3
    
    def get_endpoint_data(frame: ctk.CTkFrame) -> AllEndpointsData:
        """Extracts and formats the endpoints data from widgets inside a CKtFrame"""
        nonlocal all_endpoints, method, current_endpoint, current_info
        
        widget: ctk.CTkOptionMenu|ctk.CTkEntry
        for widget in frame.winfo_children():
            if isinstance(widget, ctk.CTkOptionMenu):
                method = widget.get()
            elif isinstance(widget, ctk.CTkEntry):
                if method != "":
                    current_endpoint = f"{method} {widget.get()}"
                    all_endpoints[current_endpoint] = {}
                    method, current_info = [""] * 2
                elif current_info == "":
                    current_info = widget.get()
                    all_endpoints[current_endpoint][current_info] = ""
                else:
                    data: str = widget.get()
                                                    
                    if data != "" and data[0] in ["{", "[", "("]:
                        data = ast.literal_eval(data)

                    all_endpoints[current_endpoint][current_info] = data
                    current_info = ""
        
        return all_endpoints
    
    app_widget: AnyCTkWidget
    for app_widget in frame.winfo_children():
        if isinstance(app_widget, ctk.CTkFrame):
            endpoints_widget: AnyCTkWidget
            for endpoints_widget in app_widget.winfo_children():
                if isinstance(endpoints_widget, ctk.CTkTabview):
                    tabview_frame: ctk.CTkFrame
                    for tabview_frame in endpoints_widget.tab("Detail").winfo_children():
                        all_endpoints = get_endpoint_data(tabview_frame)
                elif isinstance(endpoints_widget, ctk.CTkFrame):
                    all_endpoints = get_endpoint_data(endpoints_widget)
                    
    return all_endpoints

def get_endpoint_from_user_interaction(endpoints: AllEndpointsData, endpoint: str, data: EndpointData) -> str:
    """Defines the endpoint that the user interacted with"""
    for original_endpoint, original_data in endpoints.items():
        if endpoint == original_endpoint and data == original_data:
            return endpoint
    raise ValueError("The requested endpoint has been modified before trying to move it. Please save the changes first!")

def reorder_endpoints(endpoints: AllEndpointsData, current_endpoint: str, direction: str, frame: ctk.CTkFrame) -> AllEndpointsData:
    """Moves an endpoint up or down within all endpoints"""
    if direction == "up":
        index_direction = -1
    elif direction == "down":
        index_direction = 1
    
    endpoint_keys: list[str] = list(endpoints.keys())
    current_index = endpoint_keys.index(current_endpoint)
    new_index = current_index + index_direction
    
    if (new_index < 0) or (new_index == len(endpoint_keys)):
        raise IndexError(f"The new index {new_index} is our of range 0-{len(endpoint_keys)-1}")
    
    all_endoints = get_all_endpoints(frame)
    
    endpoint_key = endpoint_keys.pop(current_index)
    endpoint_keys.insert(new_index, endpoint_key)
    
    reordered_endpoints: AllEndpointsData = {key: all_endoints[key] for key in endpoint_keys}
    
    return reordered_endpoints