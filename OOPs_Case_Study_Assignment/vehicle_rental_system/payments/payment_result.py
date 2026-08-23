from dataclasses import dataclass


@dataclass(frozen=True)
class PaymentResult:
    transaction_id: str
    amount: float
    method: str
    status: str = "SUCCESS"
