import os
from tempfile import TemporaryDirectory
from typing import Optional

from PyPDF2 import PdfReader
from pdfCropMargins import crop

from app.processing.size import get_page_size


def verify_size_after_crop(
    file: str,
    left: int = 0, bottom: int = 0, right: int = 0, top: int = 0,
    max_width: Optional[float] = None, max_height: Optional[float] = None
) -> bool:
    """Crop margins of given PDF file and verify if the size matches the required."""
    with TemporaryDirectory() as tmpdir:
        out_file = os.path.join(tmpdir, file)
        crop(["-p4", str(left), str(bottom), str(right), str(top), "-o", out_file, file])
        pdf = PdfReader(str(out_file))
        for page in pdf.pages:
            width, height = get_page_size(page)
            if max_width is not None and width > max_width:
                return False
            if max_height is not None and height > max_height:
                return False
    return True


def verify_left_margin(file: str, width: float, min_left: float = 1.5) -> bool:
    """Check if left margin is OK."""
    return verify_size_after_crop(file, left=100, max_width=width - min_left)


def verify_bottom_margin(file, height: float, min_bottom: float = 0.8) -> bool:
    """Check if bottom margin is OK."""
    return verify_size_after_crop(file, bottom=100, max_height=height - min_bottom)


def verify_right_margin(file, width: float, min_right: float = 1.5) -> bool:
    """Check if right margin is OK."""
    return verify_size_after_crop(file, right=100, max_width=width - min_right)


def verify_top_margin(file, height: float, min_top: float = 1.0) -> bool:
    """Check if top margin is OK."""
    return verify_size_after_crop(file, top=100, max_height=height - min_top)
