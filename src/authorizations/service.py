import httpx
from pydantic import UUID4
from src.authorizations.schemas import PurchaseResponse
from src.authorizations.constants import ResponseStatus
from src.config import settings

CARD_BALANCE_URL = f"{settings.nawi_reports_api_url}/cards/"
DOCK_AUTHORIZATION_URL = settings.dock_authorization_url


async def get_card_detail(dock_card_id: UUID4) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{CARD_BALANCE_URL}{dock_card_id}")
        response.raise_for_status()
        return response.json()

async def send_authorization_to_dock(payload: dict) -> None:
    headers = {
        "client-id": "your-client-id",
        "uuid": "transaction-uuid",
        "x-apigw-api-id": "api-gateway-id",
    }
    async with httpx.AsyncClient() as client:
        response = await client.post(DOCK_AUTHORIZATION_URL, json=payload, headers=headers)
        response.raise_for_status()

async def authorize_purchase(account_id: UUID4, amount: int, purchase_request: dict) -> PurchaseResponse:
    """
    Authorize a purchase request.
    Decline the purchase if the card is inactive, the balance is insufficient, or the transaction is international.
    """
    if purchase_request['transaction_indicators']['is_international'] is True:
        return PurchaseResponse(response=ResponseStatus.DECLINED, reason="International transactions are not allowed")
    card_detail = await get_card_detail(account_id)
    if card_detail['data']['is_active'] is False:
        response = PurchaseResponse(response=ResponseStatus.DECLINED, reason="Card is inactive")
    elif card_detail['data']['balance']['amount'] >= amount:
        response = PurchaseResponse(response=ResponseStatus.APPROVED, reason="Sufficient balance")
    else:
        response = PurchaseResponse(response=ResponseStatus.DECLINED, reason="Insufficient balance")
    
    # Send the response to Dock
    authorization_payload = {
        "response": response.response,
        "reason": response.reason
    }
    await send_authorization_to_dock(authorization_payload)
    
    return response