from fastapi import APIRouter, Depends, HTTPException, status


import backend_app.schemas as schemas
from backend_app.api.pixabay_utils import download_image


router = APIRouter()


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_image(
    query: schemas.QueryEnum,
) -> dict:
    """
    랜덤 이미지 다운로드
    """

    result = await download_image(query.name)

    if not result:
        return HTTPException(status_code=404, detail="Item not found")

    return {"message": f"Save {result}"}
