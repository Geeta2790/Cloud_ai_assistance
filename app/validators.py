SUPPORTED_PROVIDERS = {
    "aws",
    "azure",
    "gcp",
    "google cloud",
}

SUPPORTED_SERVICES = {
    "ec2",
    "vm",
    "virtual machine",
    "rds",
    "database",
}


def validate_cloud_request(message: str) -> tuple[bool, str]:
    cleaned_message = message.strip().lower()

    if not cleaned_message:
        return False, "Request message cannot be empty."

    provider_found = any(
        provider in cleaned_message
        for provider in SUPPORTED_PROVIDERS
    )

    service_found = any(
        service in cleaned_message
        for service in SUPPORTED_SERVICES
    )

    if not provider_found:
        return False, "Please mention a supported cloud provider."

    if not service_found:
        return False, "Please mention a supported cloud service."

    return True, "Request is valid."
