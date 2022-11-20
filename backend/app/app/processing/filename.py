from app.schemas.settings import Settings


def validate_name(settings: Settings, filename: str):
    """exclude extension!!"""
    errors = {
        "name_banned_symbols": True,
        "allow_leading_space": True,
        "allow_trailing_space": True,
        "encoding": True,
        "filename_max_length": True,
    }

    if len(filename) > settings.filename_max_length:
        errors["filename_max_length"] = False

    if not settings.allow_leading_space:
        if filename.startswith(" "):
            errors["allow_leading_space"] = False
    if not settings.allow_trailing_space:
        if filename.endswith(" "):
            errors["allow_trailing_space"] = False

    for c in filename:
        if c in settings.name_banned_symbols:
            errors["name_banned_symbols"] = False
            break
    return errors


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
