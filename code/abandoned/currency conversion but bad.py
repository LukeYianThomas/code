x=[1.35,1.15,1.35,32.45,1308.54,65.30,85.54,217.12]
_ = input()#us dollar = 1 ,euro = 2 ,bahemian dollar = 3 ,cuban peso = 4 ,chilian peso = 5 ,egyption pound = 6 ,dominican peso = 7 ,liberian dollar = 8
a,b = _.split(",")
print(int(a)*x[int(b)-1])

CurrencyMulti = [1.35,1.15,20,1.35,32.45]
def ConvToEuro(pound):
    Euro=float(pound*1.15)
    print(f"{Euro:.2f}")
def ConvToDollar(pound):
    Dollar=float(pound*1.35)
    print(f"{Dollar:.2f}")
def ConvToYen(pound):
    Yen=float(pound*20)
    print(f"{Yen:.2f}")
def ConvToBahemianDollar(pound):
    BahemianDollar=float(pound*1.35)
    print(f"{BahemianDollar:.2f}")
def ConvToCubanPeso(pound):
    CubanPeso=float(pound*32.45)
    print(f"{CubanPeso:.2f}")
def ConvToPound(amount,currency):
    pound=float(amount/currency)
    print(f"{pound:.2f}")

