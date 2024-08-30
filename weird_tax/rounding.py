def modern_round(amount_c:float)->int:
    pennies_only_amount = amount_c % 100
    # Round to nearest penny if you are at .495-.994
    if pennies_only_amount >= 49.5:
        return round(amount_c)
    return round(amount_c/100)*100