from fastapi import APIRouter, HTTPException, status

from app.schemas import ServiceRequest, ServiceRequestResponse


router = APIRouter(
    prefix="/service-requests",
    tags=["Service Requests"],
)



SUPPORTED_REGIONS = {
    "aws": {
        "ap-south-1",
        "us-east-1",
        "eu-west-1",
    },
    "azure": {
        "centralindia",
        "eastus",
        "westeurope",
    },
    "gcp": {
        "asia-south1",
        "us-central1",
        "europe-west1",
    },
}


@router.post(
    "",
    response_model=ServiceRequestResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_service_request(
    service_request: ServiceRequest,
) -> ServiceRequestResponse:
    valid_regions = SUPPORTED_REGIONS.get(service_request.provider.value, set())
    if service_request.region not in valid_regions:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                f"Region '{service_request.region}' is not supported for "
                f"provider '{service_request.provider.value}'."
            ),
        )

    return ServiceRequestResponse(
        status="created",
        request_id="req-0001",
        provider=service_request.provider,
        service=service_request.service,
        environment=service_request.environment,
        operating_system=service_request.operating_system,
        region=service_request.region,
        disk_size_gb=service_request.disk_size_gb,
    )