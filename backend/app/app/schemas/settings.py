from typing import Optional
from pydantic import BaseModel


class Settings(BaseModel):
    id: int
    format: str
    orientation: str
    pdf_version: list
    min_margin_top: float
    min_margin_bottom: float
    min_margin_side: float

    protections_allowed: bool

    # filename
    name_banned_symbols: str
    allow_leading_space: bool
    allow_trailing_space: bool
    encoding: str
    filename_max_length: int

    # optim
    composite_pdf: bool
    allow_unused_links_etc: bool
    allow_hidden_layer_info: bool

    # fonts
    embedded_font: bool
    min_font_single_color_single_elem: float
    min_font_single_color_double_elem: float
    min_font_multi_color_single_elem: float
    min_font_multi_color_double_elem: float

    # lines
    min_line_thickness: float
    min_line_thickness_other: float

    active_forms: bool

    color_mode: str
    text_color: str

    # graphics
    min_dpi: float
    graphic_scale: float
    graphic_color_mode: str

    # address
    name_max_length: int
    name_cont_max_length: int
    street_max_length: int
    building_number_max_length: int
    local_number_max_length: int
    postal_code_max_length: int
    city_max_length: int
    country_max_length: int

    sender_info_max_length: int
    signature_act_max_length: int

    class Config:
        orm_mode=True

class SettingsUpdate(BaseModel):
    format: Optional[str]
    orientation: Optional[str]
    pdf_version: Optional[list]
    min_margin_top: Optional[float]
    min_margin_bottom: Optional[float]
    min_margin_side: Optional[float]

    protections_allowed: Optional[bool]

    # filename
    name_banned_symbols: Optional[str]
    allow_leading_space: Optional[bool]
    allow_trailing_space: Optional[bool]
    encoding: Optional[str]
    filename_max_length: Optional[int]

    # optim
    composite_pdf: Optional[bool]
    allow_unused_links_etc: Optional[bool]
    allow_hidden_layer_info: Optional[bool]

    # fonts
    embedded_font: Optional[bool]
    min_font_single_color_single_elem: Optional[float]
    min_font_single_color_double_elem: Optional[float]
    min_font_multi_color_single_elem: Optional[float]
    min_font_multi_color_double_elem: Optional[float]

    # lines
    min_line_thickness: Optional[float]
    min_line_thickness_other: Optional[float]

    active_forms: Optional[bool]

    color_mode: Optional[str]
    text_color: Optional[str]

    # graphics
    min_dpi: Optional[float]
    graphic_scale: Optional[float]
    graphic_color_mode: Optional[str]

    # address
    name_max_length: Optional[int]
    name_cont_max_length: Optional[int]
    street_max_length: Optional[int]
    building_number_max_length: Optional[int]
    local_number_max_length: Optional[int]
    postal_code_max_length: Optional[int]
    city_max_length: Optional[int]
    country_max_length: Optional[int]

    sender_info_max_length: Optional[int]
    signature_act_max_length: Optional[int]
