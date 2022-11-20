from typing import Tuple

from PyPDF2 import PageObject, PdfReader


def dots_to_cm(dots: float, dpi: int = 72, cms_inch: float = 2.54):
    """Convert dots to cm"""
    return float(dots / dpi) * cms_inch


def get_page_size(page: PageObject) -> Tuple[float, float]:
    """Get PDF size (width, height) in cm"""
    width = dots_to_cm(page.mediaBox.getWidth())
    height = dots_to_cm(page.mediaBox.getHeight())
    return width, height


def verify_size(
    page: PageObject,
    expected_width: float = 21.0,
    expected_height: float = 29.7,
    tolerance: float = 1e-1,
) -> bool:
    """Check if page fits the requirements."""
    width, height = get_page_size(page)
    return (
        abs(width - expected_width) < tolerance and abs(height - expected_height) < tolerance
    )


def verify_page_size(
    reader: PdfReader,
    expected_width: float = 21.0,
    expected_height: float = 29.7,
    tolerance: float = 1e-1
) -> bool:
    """Check if PDF file fits the requirements."""
    for page in reader.pages:
        if not verify_size(page, expected_width, expected_height, tolerance):
            return False
    return True
