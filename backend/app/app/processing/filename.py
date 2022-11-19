from app.schemas.settings import Settings


def validate_name(settings: Settings, filename: str) -> bool:
    """exclude extension!!"""
    if not settings.allow_leading_space:
        if filename.startswith(" "):
            return False
    if not settings.allow_trailing_space:
        if filename.endswith(" "):
            return False
    for c in filename:
        if c in settings.name_banned_symbols:
            return False
    return True


def fix_name(settings: Settings, filename: str) -> str:
    """exclude extension!!"""
    if not settings.allow_leading_space:
        if filename.startswith(" "):
            filename = filename[1:]
    if not settings.allow_trailing_space:
        if filename.endswith(" "):
            filename = filename[:-1]
    for c in settings.name_banned_symbols:
        filename = filename.replace(c, "")
    return filename
