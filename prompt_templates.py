
def construct_prompt(total_income, needs, wants, leftover_income, electricity_bill, water_bill, phone_bill,
                     food_supplies, school_supplies, other_expenses, grocery_shopping, gas_refill, eating_out,
                     movie, clothing):
            
    template = f"""
    [INTRODUCTION]
    
    Based on the 50/30/20 rule, I will provide you with a detailed financial report using the information you have provided. This report will analyze your income, expenses, and savings allocation.
    
    [INCOME AND EXPENSE BREAKDOWN]
    
    Your financial details are as follows:
    
    
    - Monthly income: {total_income}
    
    - Monthly expenses: 
    
    1- Essential expenses: {needs}
    
    Electricity Bill: {electricity_bill}
    Water Bill: {water_bill}
    Phone Bill: {phone_bill}
    Food Supplies: {food_supplies}
    School Supplies: {school_supplies}
    Other Expenses: {other_expenses}
    
    2- Discretionary expenses: {wants}
    
    Grocery shopping: {grocery_shopping}
    Gas refill: {gas_refill}
    Eating out: {eating_out}
    Movie: {movie}
    Clothing: {clothing}
    
        
    
    [ALLOCATION ANALYSIS]
    
    Based on the provided information, let's analyze your financial situation:
    
    Essential expenses account for [X%] of your monthly income, which [exceeds/falls short of] the recommended 50%.
    Non-essential expenses represent [Y%] of your monthly income, which [meets/falls short of] the recommended 30%.
    
    [SAVINGS EVALUATION]
    
    Now, let's evaluate your savings and investment allocation:
    
    Monthly savings: {leftover_income}
    
    Your savings currently represent [Z%] of your monthly income, which [meets/falls short of] the recommended 20%.
    
    [RECOMMENDATIONS]
    
    Based on this analysis, here are my recommendations:
    
    Essential Expenses: [Provide specific suggestions for optimizing essential expenses]
    Discretionary Expenses: [Provide advice on finding balance within the recommended 30% range]
    Savings and Investments: [Provide recommendations for increasing savings, diversifying investments, or seeking professional advice]
    
    [CONCLUSION]
    
    In conclusion, by implementing the recommended adjustments and regularly reviewing your budget, you can achieve a well-balanced financial plan aligned with the 50/30/20 rule.
    
    """
    
    return template