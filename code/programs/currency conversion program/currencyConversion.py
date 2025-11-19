#EXCHANGE RATES
USD_EXCH_RATE = 1.40
EUR_EXCH_RATE = 1.14
BRL_EXCH_RATE = 4.77
JPY_EXCH_RATE = 151.05
TRY_EXCH_RATE = 5.68

EXCH_RATES = [USD_EXCH_RATE,EUR_EXCH_RATE,BRL_EXCH_RATE,JPY_EXCH_RATE,TRY_EXCH_RATE]
EXCH_NAMES = ["USD","EUR","BRL","JPY","TRY"]
valid = ["y","n"]

#MAXIMUM TRANSFER
MAX_TRANSFER = 2500
MIN_TRANSFER = 0

#TRANSACTION FEE CONSTANTS
TRANSACTION_FEE_BOUNDRIES = [300,750,1000,2000,10000000000000]
TRANSACTION_FEE_AMOUNT = [0.035,0.030,0.025,0.020,0.015]
TRANSACTION_FEE_BOUNDRIES.reverse()

#functions
def inputValidation(x,lower,upper):
    if x.isnumeric():
        if int(x) in range(lower,upper+1):return True


def transactionFee(qty):
    temp = len(EXCH_RATES)
    for _ in range(len(TRANSACTION_FEE_BOUNDRIES)):
        if qty < TRANSACTION_FEE_BOUNDRIES[_]:temp-=1
    return qty*TRANSACTION_FEE_AMOUNT[temp]

print(f"""==========================
CURRENT EXCHANGE RATES
1 - American Dollars: {USD_EXCH_RATE}
2 - Euros: {EUR_EXCH_RATE}
3 - Brazilian Real: {BRL_EXCH_RATE}
4 - Japanese Yen: {JPY_EXCH_RATE}
5 - Turkish Lira: {TRY_EXCH_RATE}
==========================
""")

while True:
    amount = input(f"Please enter the amount you wish to transfer up to a maximum of £{MAX_TRANSFER}:")
    while not inputValidation(amount,MIN_TRANSFER,MAX_TRANSFER):amount = input(f"""Invalid Data
    Please re-enter the amount you wish to transfer up to a maximum of £{MAX_TRANSFER}:""")
    amount = int(amount)
    currency = input("Please select a currency: ")
    while not inputValidation(currency,1,len(EXCH_RATES)):currency = input("""Invalid Data
    Please re-select a currency:""")
    currency = int(currency)
    discount = input("Are you a member of staff Y/N: ")
    while not discount.lower() in valid: discount = input("""Invalid Data
    Please re-enter:""")
    converted_amount = amount*EXCH_RATES[currency-1]
    currency_name = EXCH_NAMES[currency-1]
    commission = transactionFee(amount)
    print(f"""You have selected to transfer £{amount:.2f} to {converted_amount:.2f} {currency_name}
The transaction fee will be: £{commission:.2f}""")
    check = input("Is this correct? Y/N: ")
    while not check.lower() in valid: check = input("""Invalid Data
    Please re-enter:""")
    if check == "y":break
print(f"""Transferred £{amount:.2f} to {converted_amount} {currency_name}
Commission: £{commission:.2f}
Thank you for using N/A travel agency""")


