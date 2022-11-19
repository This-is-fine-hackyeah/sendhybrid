from sqlalchemy import Boolean, Column, Integer, String, Float, ARRAY

from app.db.base_class import Base


class Settings(Base):
    """Parameters for PDF validation, changable by superusers"""
    id = Column(Integer, primary_key=True, index=True)
    format = Column(String, default="A4", nullable=False)
    orientation = Column(String, default="vertical", nullable=False)
    pdf_version = Column(ARRAY(String), default=["PDF A-2", "PDF A-4"], nullable=False)
    min_margin_top = Column(Float, default=10.0, nullable=False)
    min_margin_bottom = Column(Float, default=8.0, nullable=False)
    min_margin_side = Column(Float, default=15.0, nullable=False)

    protections_allowed = Column(Boolean, default=False, nullable=False)

    # filename
    name_banned_symbols = Column(String, default="~\"#%&*:<>?!/\\{|}", nullable=False)
    allow_leading_space = Column(Boolean, default=False, nullable=False)
    allow_trailing_space = Column(Boolean, default=False, nullable=False)
    encoding = Column(String, default="utf-8", nullable=False)
    filename_max_length = Column(Integer, default=255, nullable=False)

    # optim
    composite_pdf = Column(Boolean, default=True, nullable=False)
    allow_unused_links_etc = Column(Boolean, default=False, nullable=False)
    allow_hidden_layer_info = Column(Boolean, default=False, nullable=False)

    # fonts
    embedded_font = Column(Boolean, default=True, nullable=False)
    min_font_single_color_single_elem = Column(Float, default=5.0, nullable=False)
    min_font_single_color_double_elem = Column(Float, default=6.0, nullable=False)
    min_font_multi_color_single_elem = Column(Float, default=8.0, nullable=False)
    min_font_multi_color_double_elem = Column(Float, default=10.0, nullable=False)

    # lines
    min_line_thickness = Column(Float, default=0.1, nullable=False)
    min_line_thickness_other = Column(Float, default=0.5, nullable=False)

    active_forms = Column(Boolean, default=False, nullable=False)

    color_mode = Column(String, default="CMYK", nullable=False)
    text_color = Column(String, default="black", nullable=False)

    # graphics
    min_dpi = Column(Float, default=150.0, nullable=False)
    graphic_scale = Column(Float, default=1.0, nullable=False)
    graphic_color_mode = Column(String, default="CMYK", nullable=False)

    # address
    name_max_length = Column(Integer, default=50, nullable=False)
    name_cont_max_length = Column(Integer, default=100, nullable=False)
    street_max_length = Column(Integer, default=35, nullable=False)
    building_number_max_length = Column(Integer, default=10, nullable=False)
    local_number_max_length = Column(Integer, default=10, nullable=False)
    postal_code_max_length = Column(Integer, default=20, nullable=False)
    city_max_length = Column(Integer, default=20, nullable=False)
    country_max_length = Column(Integer, default=30, nullable=False)

    sender_info_max_length = Column(Integer, default=40, nullable=False)
    signature_act_max_length = Column(Integer, default=40, nullable=False)
