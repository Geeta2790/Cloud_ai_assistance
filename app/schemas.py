
from enum import Enum

from pydantic import BaseModel, Field


class CloudProvider(str, Enum):
    AWS = "aws"
    AZURE = "azure"
    GCP = "gcp"


class UserRequest(BaseModel):
    message: str = Field(
        ...,
        min_length=3,
        description="Cloud provisioning request entered by the user",
        examples=["I need an AWS EC2 Linux server"],
    )


class UserRequestResponse(BaseModel):
    status: str
    message: str
    validation_message: str




class CloudService(str, Enum):
    EC2 = "ec2"
    VM = "vm"
    RDS = "rds"


class Environment(str, Enum):
    DEV = "dev"
    QA = "qa"
    PROD = "prod"


class OperatingSystem(str, Enum):
    LINUX = "linux"
    WINDOWS = "windows"


class ServiceRequest(BaseModel):
    provider: CloudProvider
    service: CloudService
    environment: Environment
    operating_system: OperatingSystem
    region: str = Field(
        ...,
        min_length=3,
        description="Cloud region selected by the user",
        examples=["ap-south-1"],
    )
    disk_size_gb: int = Field(
        default=20,
        ge=20,
        le=500,
        description="Root disk size between 20 GB and 500 GB",
    )

class ServiceRequestResponse(BaseModel):
    status: str
    request_id: str
    provider: CloudProvider
    service: CloudService
    environment: Environment
    operating_system: OperatingSystem
    region: str
    disk_size_gb: int