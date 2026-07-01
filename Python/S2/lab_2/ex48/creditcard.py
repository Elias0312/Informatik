def credit(loan, interest, repayment, years):
    if years <= 0:
        return loan
    
    rest = loan + (loan * (interest/100)) - repayment
    return credit(rest, interest, repayment, years - 1)


