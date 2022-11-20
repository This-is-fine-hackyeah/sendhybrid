from pydantic import BaseModel
from typing import Optional

class Metadata(BaseModel):
    receiver_name: Optional[str]
    receiver_name2: Optional[str]
    receiver_last_name: Optional[str]
    receiver_address: Optional[str]
    receiver_pesel: Optional[str]

    sender_name: Optional[str]
    sender_name2: Optional[str]
    sender_phone: Optional[str]
    sender_email: Optional[str]
    sender_epuap: Optional[str]
    sender_address: Optional[str]

    unp: Optional[str]
    znak_sprawy: Optional[str]
    tytul_sprawy: Optional[str]
    date: Optional[str]
    nip: Optional[str]

    class Config:
        orm_mode=True

class MetadataCreate(Metadata):
    document_id: int


class Report(BaseModel):
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
