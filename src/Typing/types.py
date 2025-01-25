import customtkinter as ctk # type: ignore
from typing import Any

EndpointInfo = str|list[Any]|dict[str, Any]

EndpointData = dict[str, EndpointInfo]

AllEndpointsData = dict[str, EndpointData]

AnyCTkWidget = ctk.CTkButton| \
               ctk.CTkCheckBox| \
               ctk.CTkComboBox| \
               ctk.CTkEntry| \
               ctk.CTkFrame| \
               ctk.CTkLabel| \
               ctk.CTkOptionMenu| \
               ctk.CTkProgressBar| \
               ctk.CTkRadioButton| \
               ctk.CTkScrollableFrame| \
               ctk.CTkScrollbar| \
               ctk.CTkSegmentedButton| \
               ctk.CTkSlider| \
               ctk.CTkSwitch| \
               ctk.CTkTabview| \
               ctk.CTkTextbox