from enum import Enum
from pydantic import BaseModel

class ResponseStatus(str, Enum):
    APPROVED = "APPROVED"
    DECLINED = "DECLINED"

class PurchaseResponse(BaseModel):
    response: ResponseStatus
    reason: str
