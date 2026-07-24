from fastapi import APIRouter
from app.schemas import UserRequest, UserRequestResponse

router = APIRouter(
    prefix="/requests",
    tags=["Requests"],
)

@router.post(
    "",
    response_model=UserRequestResponse,
    status_code=201,
)

def create_request(user_request: UserRequest) -> UserRequestResponse:
    return UserRequestResponse(
        status="received",
        message=user_request.message,
    )