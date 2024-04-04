#WAF to convert USD to BDT

# 1 USD = 100 BDT


def usd_bdt(n):
    bdt = n*100
    print("USD:", n)
    print("BDT:", bdt)

usd_bdt(2)