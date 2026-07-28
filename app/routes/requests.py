from fastapi import APIRouter, HTTPException, status

from app.schemas import UserRequest, UserRequestResponse
from app.validators import validate_cloud_request


router = APIRouter(
    prefix="/requests",
    tags=["Requests"],
)


@router.post(
    "",
    response_model=UserRequestResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_request(
    user_request: UserRequest,
) -> UserRequestResponse:
    is_valid, validation_message = validate_cloud_request(
        user_request.message
    )

    if not is_valid:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=validation_message,
        )

    return UserRequestResponse(
        status="received",
        message=user_request.message,
        validation_message=validation_message,
    )