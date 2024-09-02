from pydantic import BaseModel

class CreditScoreRequest(BaseModel):
    payment_history: float
    credit_utilization: float
    credit_history_length: int
    credit_mix: int
    recent_inquiries: int
    total_debt: float
    income: float
    employment_status: bool
    age: int
