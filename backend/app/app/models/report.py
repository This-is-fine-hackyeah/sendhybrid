from sqlalchemy import Boolean, Column, Integer, String, Float, ARRAY, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Report(Base):
    """What checks failed"""
    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey("document.id"), nullable=False)
    document = relationship("Document")

    format = Column(Boolean, nullable=False)
    orientation = Column(Boolean, nullable=False)
    pdf_version = Column(Boolean, nullable=False)
    min_margin_top = Column(Boolean, nullable=False)
    min_margin_bottom = Column(Boolean, nullable=False)
    min_margin_side = Column(Boolean, nullable=False)

    protections_allowed = Column(Boolean, nullable=False)

    # filename
    name_banned_symbols = Column(Boolean, nullable=False)
    allow_leading_space = Column(Boolean, nullable=False)
    allow_trailing_space = Column(Boolean, nullable=False)
    encoding = Column(Boolean, nullable=False)
    filename_max_length = Column(Boolean, nullable=False)

    # optim
    composite_pdf = Column(Boolean, nullable=False)
    allow_unused_links_etc = Column(Boolean, nullable=False)
    allow_hidden_layer_info = Column(Boolean, nullable=False)

    # fonts
    embedded_font = Column(Boolean, nullable=False)
    min_font_single_color_single_elem = Column(Boolean, nullable=False)
    min_font_single_color_double_elem = Column(Boolean, nullable=False)
    min_font_multi_color_single_elem = Column(Boolean, nullable=False)
    min_font_multi_color_double_elem = Column(Boolean, nullable=False)

    # lines
    min_line_thickness = Column(Boolean, nullable=False)
    min_line_thickness_other = Column(Boolean, nullable=False)

    active_forms = Column(Boolean, nullable=False)

    color_mode = Column(Boolean, nullable=False)
    text_color = Column(Boolean, nullable=False)

    # graphics
    min_dpi = Column(Boolean, nullable=False)
    graphic_scale = Column(Boolean, nullable=False)
    graphic_color_mode = Column(Boolean, nullable=False)

    # address
    name_max_length = Column(Boolean, nullable=False)
    name_cont_max_length = Column(Boolean, nullable=False)
    street_max_length = Column(Boolean, nullable=False)
    building_number_max_length = Column(Boolean, nullable=False)
    local_number_max_length = Column(Boolean, nullable=False)
    postal_code_max_length = Column(Boolean, nullable=False)
    city_max_length = Column(Boolean, nullable=False)
    country_max_length = Column(Boolean, nullable=False)

    sender_info_max_length = Column(Boolean, nullable=False)
    signature_act_max_length = Column(Boolean, nullable=False)
