

def calculate_credit_score(
    payment_history: float,
    credit_utilization: float,
    credit_history_length: int,
    credit_mix: int,
    recent_inquiries: int,
    total_debt: float,
    income: float,
    employment_status: bool,
    age: int
) -> float:
    """
    Calculate a credit score based on various financial and personal factors.
    
    Args:
        payment_history (float): Score based on payment history (0-100)
        credit_utilization (float): Percentage of available credit used (0-100)
        credit_history_length (int): Length of credit history in months
        credit_mix (int): Number of different types of credit accounts
        recent_inquiries (int): Number of recent credit inquiries
        total_debt (float): Total amount of debt
        income (float): Annual income in dollars
        employment_status (bool): True if employed, False if unemployed
        age (int): Age of the individual in years
    
    Returns:
        float: Calculated credit score (300-850)
    """
    # Initialize base score
    score: float = 600
    
    score += payment_history * 1.5
    score -= min(credit_utilization * 1.2, 100)
    score += min(credit_history_length / 12 * 5, 50)
    score += min(credit_mix * 10, 40)
    score -= recent_inquiries * 5
    debt_to_income: float = (total_debt / income) * 100 if income > 0 else 100
    score -= min(debt_to_income, 50)
    score += 10 if employment_status else 0
    score += min((age - 18) * 0.5, 10) if age >= 18 else 0

    return max(300, min(score, 850))
