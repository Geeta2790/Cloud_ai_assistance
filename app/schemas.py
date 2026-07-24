from pydantic import BaseModel, Field

class UserRequest(BaseModel):
    message: str = Field(
        ...,
        min_leanth=3,
        description="Cloud provisioning request entered by the user",
        examples=["I need an AWS EC2 Linux server"],
    )
    
class UserRequestResponse(BaseModel):
    status: str
    message: str