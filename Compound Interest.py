'''COMPUND INTEREST'''
# p=int(input("Enter the Capital amount: "))
# r=int(input("Enter the Interest: "))
# t=int(input("Enter the Time: "))
# A= p(1+(r/100))**t
# amount= A-p
# print("Compund Interest is: ", amount)

def compound_interest(principle, rate, time):
    Amount = principle * (pow((1 + rate / 100), time))
    CI = Amount - principle
    print("Compound interest is", CI)
compound_interest(10000, 10.25, 5)
