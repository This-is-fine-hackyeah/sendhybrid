from pydantic import BaseModel
from typing import Optional


class Report(BaseModel):
    format: bool
    orientation: bool
    pdf_version: bool
    min_margin_top: bool
    min_margin_bottom: bool
    min_margin_side: bool

    protections_allowed: bool

    # filename
    name_banned_symbols: bool
    allow_leading_space: bool
    allow_trailing_space: bool
    encoding: bool
    filename_max_length: bool

    # optim
    composite_pdf: bool
    allow_unused_links_etc: bool
    allow_hidden_layer_info: bool

    # fonts
    embedded_font: bool
    min_font_single_color_single_elem: bool
    min_font_single_color_double_elem: bool
    min_font_multi_color_single_elem: bool
    min_font_multi_color_double_elem: bool

    # lines
    min_line_thickness: bool
    min_line_thickness_other: bool

    active_forms: bool

    color_mode: bool
    text_color: bool

    # graphics
    min_dpi: bool
    graphic_scale: bool
    graphic_color_mode: bool

    # address
    name_max_length: bool
    name_cont_max_length: bool
    street_max_length: bool
    building_number_max_length: bool
    local_number_max_length: bool
    postal_code_max_length: bool
    city_max_length: bool
    country_max_length: bool

    sender_info_max_length: bool
    signature_act_max_length: bool

    class Config:
        orm_mode=True

class ReportUpdate(BaseModel):
    format: Optional[bool]
    orientation: Optional[bool]
    pdf_version: Optional[bool]
    min_margin_top: Optional[bool]
    min_margin_bottom: Optional[bool]
    min_margin_side: Optional[bool]

    protections_allowed: Optional[bool]

    # filename
    name_banned_symbols: Optional[bool]
    allow_leading_space: Optional[bool]
    allow_trailing_space: Optional[bool]
    encoding: Optional[bool]
    filename_max_length: Optional[bool]

    # optim
    composite_pdf: Optional[bool]
    allow_unused_links_etc: Optional[bool]
    allow_hidden_layer_info: Optional[bool]

    # fonts
    embedded_font: Optional[bool]
    min_font_single_color_single_elem: Optional[bool]
    min_font_single_color_double_elem: Optional[bool]
    min_font_multi_color_single_elem: Optional[bool]
    min_font_multi_color_double_elem: Optional[bool]

    # lines
    min_line_thickness: Optional[bool]
    min_line_thickness_other: Optional[bool]

    active_forms: Optional[bool]

    color_mode: Optional[bool]
    text_color: Optional[bool]

    # graphics
    min_dpi: Optional[bool]
    graphic_scale: Optional[bool]
    graphic_color_mode: Optional[bool]

    # address
    name_max_length: Optional[bool]
    name_cont_max_length: Optional[bool]
    street_max_length: Optional[bool]
    building_number_max_length: Optional[bool]
    local_number_max_length: Optional[bool]
    postal_code_max_length: Optional[bool]
    city_max_length: Optional[bool]
    country_max_length: Optional[bool]

    sender_info_max_length: Optional[bool]
    signature_act_max_length: Optional[bool]
