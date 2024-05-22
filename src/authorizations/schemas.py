from enum import Enum
from typing import Optional

from pydantic import BaseModel, UUID4, Field

class CardEntry(BaseModel):
    code: str
    mode: str
    pin: str

class Processing(BaseModel):
    type: str
    destiny_account_type: str
    origin_account_type: str
    code: str

class Values(BaseModel):
    billing_conversion_rate: str
    billing_currency_code: str
    billing_value: str
    settlement_currency_code: str
    settlement_value: str
    source_currency_code: str
    source_value: str
    credit_line_usage_fee: Optional[str] = None

class AdditionalAmount(BaseModel):
    account_type: str
    amount_type: str
    currency_code: str
    amount: str

class TransactionIndicators(BaseModel):
    card_present: bool
    cardholder_present: bool
    password_present: bool
    cvv1_present: bool
    cvv2_present: bool
    cvv3_present: bool
    token_present: bool
    is_3ds_present: bool
    is_3ds_valid: bool
    recurring: bool
    allows_partial_approval: bool
    pin_validated_offline: bool
    partially_reversed: bool
    preauthorization: bool
    is_crossborder: bool
    is_dcc: bool
    only_supports_purchase: bool
    is_international: bool
    is_funds_transfer: bool
    is_automated_fuel_dispenser: bool
    is_ecommerce: bool

class PurchaseRequest(BaseModel):
    account_id: UUID4
    account_status: str
    person_id: UUID4
    product_id: UUID4
    product_status: str
    card_id: UUID4
    card_status: str
    card_number: str
    card_expiration_date: str
    card_entry: CardEntry
    bank_account_number: Optional[str] = None
    bank_branch_number: Optional[str] = None
    transmission_date_time_gmt: str
    terminal_date: str
    terminal_time: str
    terminal_code: str
    mti: str
    processing: Processing
    transaction_type_indicator: str
    nsu: str
    authorization_code: str
    transaction_origin: str
    installment_type: Optional[str] = None
    installments: int
    merchant_category_code: str
    establishment_code: str
    establishment: str
    retrieval_reference_number: str
    pos_postal_code: str
    acquirer_country_code: str
    values: Values
    preauthorization: Optional[str] = None
    token_data: Optional[str] = None
    funds_transfer: Optional[str] = None
    additional_amount: AdditionalAmount
    transaction_indicators: TransactionIndicators

class PurchaseResponse(BaseModel):
    response: str
    reason: str
