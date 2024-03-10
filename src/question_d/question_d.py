#write functions here, don't add input('') statements here!

def get_bonus_pay_amount(sales):
    if sales < 0 or sales > 1999:
        return "Invalid arguments"
    elif 0 <= sales < 500:
        return sales * 0.05
    elif 500 <= sales < 1000:
        return sales * 0.06
    elif 1000 <= sales < 1500:
        return sales * 0.07
    else: 
        1500 <= sales <= 1999
    return sales * 0.08