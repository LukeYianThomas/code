#EXCHANGE RATES
USD_EXCH_RATE = 1.40
EUR_EXCH_RATE = 1.14
BRL_EXCH_RATE = 4.77
JPY_EXCH_RATE = 151.05
TRY_EXCH_RATE = 5.68

# Discount for any orders over £20 before delivery cost is applied.
DISCOUNT_RATE = 0.95




def validate_moneys_range(money):
    while money < 1 or money > 2500:
        print("Not in range, please re-enter number of money.")
        money = int(input("Enter your number of money from 1-2500: "))
    return money


   # Determine base cost
def setExchangedAmount(currency):
    global amount
    if currency == "dollars":
        amount*USD_EXCH_RATE
    if currency == "euros":
        amount*EUR_EXCH_RATE
    if currency == "berlin":
        amount*BRL_EXCH_RATE
    if currency == "japan":
        amount*JPY_EXCH_RATE
    if currency == "turkey":
        amount*TRY_EXCH_RATE

def currencyExchangeFee(money):
    if money <= 300:
        print("test")
    if money <= 750:
        print("test")
    if money <= 1000:
        print("test")
    if money <= 2000:
        print("test")
    else:
        print("test")

amount = int(input("AAAAAAAAAAA"))
discountCost = 1
discount = input("art thou staff member? (Yes/No): ").capitalize()
if discount == "Yes":
    discount = DISCOUNT_RATE
exchanged = setExchangedAmount(amount)
print(f"Exchanged amount: £{exchanged}")