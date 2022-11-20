from sqlalchemy import Boolean, Column, Integer, String, Float, ARRAY, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base


class Report(Base):
    """What checks failed"""
    id = Column(Integer, primary_key=True)
    document_id = Column(Integer, ForeignKey("document.id"), nullable=False)
    document = relationship("Document", back_populates="report")

    format = Column(Boolean, nullable=True)
    orientation = Column(Boolean, nullable=True)
    pdf_version = Column(Boolean, nullable=True)
    min_margin_top = Column(Boolean, nullable=True)
    min_margin_bottom = Column(Boolean, nullable=True)
    min_margin_side = Column(Boolean, nullable=True)

    protections_allowed = Column(Boolean, nullable=True)

    # filename
    name_banned_symbols = Column(Boolean, nullable=True)
    allow_leading_space = Column(Boolean, nullable=True)
    allow_trailing_space = Column(Boolean, nullable=True)
    encoding = Column(Boolean, nullable=True)
    filename_max_length = Column(Boolean, nullable=True)

    # optim
    composite_pdf = Column(Boolean, nullable=True)
    allow_unused_links_etc = Column(Boolean, nullable=True)
    allow_hidden_layer_info = Column(Boolean, nullable=True)

    # fonts
    embedded_font = Column(Boolean, nullable=True)
    min_font_single_color_single_elem = Column(Boolean, nullable=True)
    min_font_single_color_double_elem = Column(Boolean, nullable=True)
    min_font_multi_color_single_elem = Column(Boolean, nullable=True)
    min_font_multi_color_double_elem = Column(Boolean, nullable=True)

    # lines
    min_line_thickness = Column(Boolean, nullable=True)
    min_line_thickness_other = Column(Boolean, nullable=True)

    active_forms = Column(Boolean, nullable=True)

    color_mode = Column(Boolean, nullable=True)
    text_color = Column(Boolean, nullable=True)

    # graphics
    min_dpi = Column(Boolean, nullable=True)
    graphic_scale = Column(Boolean, nullable=True)
    graphic_color_mode = Column(Boolean, nullable=True)

    # address
    name_max_length = Column(Boolean, nullable=True)
    name_cont_max_length = Column(Boolean, nullable=True)
    street_max_length = Column(Boolean, nullable=True)
    building_number_max_length = Column(Boolean, nullable=True)
    local_number_max_length = Column(Boolean, nullable=True)
    postal_code_max_length = Column(Boolean, nullable=True)
    city_max_length = Column(Boolean, nullable=True)
    country_max_length = Column(Boolean, nullable=True)

    sender_info_max_length = Column(Boolean, nullable=True)
    signature_act_max_length = Column(Boolean, nullable=True)
