from datetime import date

from pydantic import BaseModel, ConfigDict


class CertificationBase(BaseModel):
    certificate_name: str
    issuing_organization: str
    issue_date: date
    expiry_date: date | None = None
    credential_id: str | None = None
    credential_url: str | None = None


class CertificationCreate(CertificationBase):
    pass


class CertificationUpdate(BaseModel):
    certificate_name: str | None = None
    issuing_organization: str | None = None
    issue_date: date | None = None
    expiry_date: date | None = None
    credential_id: str | None = None
    credential_url: str | None = None


class CertificationResponse(CertificationBase):
    id: int
    user_id: int

    model_config = ConfigDict(
        from_attributes=True
    )