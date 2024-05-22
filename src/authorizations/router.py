import httpx
from fastapi import APIRouter, HTTPException, status

from src.authorizations.schemas import PurchaseRequest, PurchaseResponse
from src.authorizations.service import authorize_purchase

router = APIRouter(
    prefix="/authorizations",
    tags=["Authorizations"],
)

@router.post("/purchase", response_model=PurchaseResponse, status_code=status.HTTP_201_CREATED)
async def purchase(purchase_request: PurchaseRequest):
    """
    Endpoint to authorize a purchase.
    """
    amount = purchase_request.values.source_value
    amount_in_cents = int(float(amount) * 100)
    try:
        response = await authorize_purchase(purchase_request.account_id, amount_in_cents, purchase_request.model_dump())
        return response
    except httpx.HTTPStatusError as exc:
        raise HTTPException(status_code=exc.response.status_code, detail=str(exc))