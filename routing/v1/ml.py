from io import BytesIO

from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import Response
from starlette import status
import imghdr

from starlette.responses import StreamingResponse

router = APIRouter(prefix="/api/v1/ml", tags=["company"])


def is_photo(file: UploadFile):
    image_types = ["jpeg", "png"]
    file_type = imghdr.what(file.file)
    return file_type in image_types if file_type else False


@router.post(
    "",
)
def predict(photos: list[UploadFile] = File(...)):
    for photo in photos:
        if not is_photo(photo):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="one or more file isn't photo")

    # тут работает модель

    # тут возвращается модель, должна быть в битовом представление[конвертить через BytesIO]
    return StreamingResponse(photos[0].file, media_type="image/png")
