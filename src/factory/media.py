from typing import Optional

from aiogram.types import URLInputFile, FSInputFile

def create_media(
    static: str,
    filename: Optional[str] = "file"
    ) -> URLInputFile | FSInputFile:

    if static.startswith("https://") and "." in static:
        return URLInputFile(
            url=static, filename=filename
        )
    
    return FSInputFile(
        path=static, filename=filename
    )