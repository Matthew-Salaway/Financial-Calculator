import math
import sys

# List of functions for user to choose from.
print("\n\n\n\n\n-------Choose from the list of Equations---------\n")
print("---Investment---")
print("1: Simple Interest")
print("2: Compound Interest")

print("3: Continuously Compounded Interest")
print("4: Time to Double an Investment (Real, not rule of 72)")
print("5: Present Value of an Ordinary Annuity")
print("6: Future Value of an Ordinary Annuity")
print("7: Compound Annual Growth Rate")
print("8: Expected Return of a Portfolio")
print("9: Inflation Adjusted Return")
print("10: Percent Gain/Loss on Investment")
print("26: Continously Compounded Interest Making Yearly Contributions")

print("\n---Debt---")
print("11: Amortization")
print("12: Leverage Ratio")
print("13: Time to Pay Off Credit Card")

print("\n---Real Estate---")
print("14: Present Value of Cash Flows")
print("15: Capitalization Rate")
print("16: Gross Scheduled Income")
print("17: Gross Operating Income")
print("18: Net Operating Income")
print("19: Cash on Cash Return")
print("20: Equity Build-Up Rate")
print("21: Price to Rent Ratio")
print("22: Price per Square Foot")
print("23: Return on Investment")
print("24: Gross Rent Multiplier")
print("25: Debt Service Coverage Ratio")


# Asks user to input number from the list
numberSelected = int(input("\nEnter number from list: "))
print("\n\n\n-----------------------------------------------------------------------------")
print("* Rate as a decimal * Time in years *")
print("-----------------------------------------------------------------------------\n")


def simpleInterest():
    print("Simple Interest: A = P(1+rt)\n")
    principle = float(input("Principle: "))
    rate = float(input("Rate: "))
    time = float(input("Time: "))
    a = principle * (1+rate*time)
    print("Future Value : $" + str(a))

def compoundIntrest():
    print("Compound Interest: A = P(1+r/m)^mt\n")
    principle = float(input("Principle: "))
    rate = float(input("Rate: "))
    period = float(input("Number of Compounding Periods per Year: "))
    time = float(input("Time: "))
    a = principle * pow((1 + rate / period), period*time)
    print("Future Value : $" + str(a))

def continouslyCompoundedInterest():
    print("Continuously Compounded Interest: A = P*e^rt\n")
    principle = float(input("Principle: "))
    rate = float(input("Rate: "))
    time = float(input("Time: "))
    a = principle * pow(math.e, rate * time)
    print("Future Value : $" + str(a))

def timeToDoubleMoney():
    print("Time to Double an Investment: T = ln(2)/[n*ln(1+r/n)]\n")
    print("**** n = number of compounding periods per year, r = rate of annual return")
    rate = float(input("Rate: "))
    compoundingPeriod = float(input("Number of Compounding Periods per Year: "))
    t = math.log(2)/(compoundingPeriod * math.log(1 + rate/compoundingPeriod))
    print("Number of years: " + str(t))

def presentValueOfAnOrdinaryAnnuity():
    print("Present Value of an Ordinary Annuity: PV = PMT * ((1/r) - (1/r(1+r)^n))\n")
    print("**** PV = present value, PMT = payment, r = interest rate, n = number of years with annual payment intervals")
    payment = float(input("Payment: "))
    rate = float(input("Rate: "))
    number = float(input("Number of Years with Annual Payment Intervals: "))
    pv = payment * ((1/rate) - (1/(rate * math.pow(1+rate, number))))
    print("Present Value: $" + str(pv))

def futureValueOfAnOrdinaryAnnuity():
    print("Future Value of an Ordinary Annuity: FV = PMT * (((1+r)^n)/r - (1/r))\n")
    print("**** FV = future value, PMT = payment, r = interest rate, n = number of years with annual payment intervals")
    payment = float(input("Payment: "))
    rate = float(input("Rate: "))
    number = float(input("Number of Years with Annual Payment Intervals: "))
    fv = payment * ((math.pow(1+rate, number)/rate) - (1 / rate))
    print("Future Value: $" + str(fv))

def compoundAnnualGrowthRate():
    print("Compound Annual Growth Rate: CAGR = (EV/BV)^(1/n) - 1\n")
    print("**** CAGR = Compound Annual Growth Rate, EV = Ending Value, BV = Beginning Value, n = number of periods\n")
    BV = float(input("Beginning Value: "))
    EV = float(input("Ending Value: "))
    number = float(input("Number of Periods: "))
    CAGR = math.pow((EV/BV), (1/number)) - 1
    print("\nCompound Annual Growth Rate: " + str(CAGR * 100) + "%")

def expectedReturnOfAPortfolio():
    print("Expected Return of a Portfolio: ERp = Summation (i=1,n): Wi * ERi \n")
    print("**** n = Number of Assets, ERp = Expected Return of the portfolio, Wi = Weight of Asset i, ERi = Expected Return of Asset i\n")
    n = int(input("Number of Assets in Portfolio: "))
    ERp = 0
    for i in range(1, n+1):
        print("\n-----------------------------------")
        print("Asset #" + str(i))
        Wi = float(input("Weight of Asset #" + str(i) +": "))
        ERi = float(input("Expected Return of Asset #" + str(i) +": "))
        ERp = ERp + (Wi * ERi)
        print("-----------------------------------")
    print("\nExpected Return of the Portfolio: $" + str(ERp))

def inflationAdjustedReturn():
    print("Inflation Adjusted Return: Real Return = [(1 + ITR)/(1 + IFR) - 1] * 100\n")
    print("**** ITR = Investment Return, IFR = Inflation Rate\n")
    ITR = float(input("Investment Return Rate: "))
    IFR = float(input("Inflation Rate: "))
    RR = ((1+ITR)/(1+IFR) - 1) * 100
    print("\nReal Return: " + str(RR) + "%")

def percentGainOrLoss():
    print("Percent Gain or Loss on an Investment: Percentage = (MP - PP)/PP * 100\n")
    print("**** MP = Market Price, PP = Purchase Price\n")
    MP = float(input("Market Price: "))
    PP = float(input("Purchase Price: "))
    P = (MP - PP)/PP * 100
    print("\nPercent Gain/Loss: " + str(P) + "%")


def continouslyCompoundedInterestMakingYearlyContrabutions():
    print("Continuously Compounded Interest: A = P*e^rt\n")
    time = float(input("Number of yearly contributions after initial payment: "))



    principle = float(input("Initial Principle: "))
    rate = float(input("Initial Rate: "))
    a = principle * pow(math.e, rate * time)

    principle = float(input("Amount contributed per year after initial payment: "))
    rate = float(input("Rate for investments after initial payment: "))
    for i in range(1, int(time + 1)):
        year = principle * pow(math.e, rate * i)
        a = a + year
    print("Future Value : $" + str(a))




def amortization():
    print("Amortization: Monthly Payment = (P * (r/n)) / (1 - (1 + r/n)^-nt)\n")
    print("**** P = principle, r = interest rate, t = number of periods, n = payments per period\n")
    p = float(input("Principle: "))
    r = float(input("Interest Rate: "))
    t = float(input("Number of Periods: "))
    n = float(input("Payments Per Period: "))
    MP = (p * (r/n)) / (1 - math.pow((1 + r/n), n*t*-1))
    print("\nMonthly Payment: $" + str(MP))

def leverageRatio():
    print("Leverage Ratio: Ratio = (TL + TD) / TI\n")
    print("**** TL = Total Liabilities, TD = Total Debts, TI = Total Income\n")
    TL = float(input("Total Liabilities: "))
    TD = float(input("Total Debts: "))
    TI = float(input("Total Income: "))
    ratio = (TL + TD) / TI
    print("\nLeverage Ratio: " + str(ratio))

def timeToPayCreditCard():
    print("Time to Pay Off Credit Card: Years = (-1/30) * ln(1 + (b/p)(1 - (1+i)^30)) / ln(1 + i)\n")
    print("**** b = balance, p = monthly payment, i = daily interest rate\n")
    b = float(input("Balance: "))
    p = float(input("Monthly Payment: "))
    i = float(input("Annual Credit Card Interest Rate: "))
    i = i/365
    months = (-1/30) * math.log(1 + (b/p) * (1 - math.pow((1 + i), 30))) / math.log(1 + i)
    print("\nMonths: " + str(months))

def presentValueOfCashFlows():
    print("Present Value of Cash Flows: Present Value = CF0 + CF1 x (1 / (1 + R)1) + CF2 x (1 / (1 + R)2) + CF2 x (1 / (1 + R)3)......\n")
    print( "**** CF = Cash Flow, R = Chosen Discount Rate\n")
    n = int(input("Number of Years: "))
    CF0 = float(input("Current Cash Flow: "))
    pv = CF0
    for i in range(1, n + 1):
        print("\n-----------------------------------")
        print("Year #" + str(i))
        CFi = float(input("Cash Flow of Year #" + str(i) + ": "))
        DR = float(input("Chosen Discount Rate for Year #" + str(i) + ": "))
        thatYear = CFi * (1 / math.pow(1+DR, i))
        pv = pv + (thatYear)
        print("-----------------------------------")
    print("\nPresent Value of Cash Flows: $" + str(pv))

def grossScheduledIncome():
    print("Gross Scheduled Income: GSI = Rental Income + Lost Income from Vacant Units\n")
    RI = float(input("Rental Income: "))
    LI = float(input("Lost Income from Vacant Units: "))
    GSI = RI + LI
    print("\nGross Scheduled Income: $" + str(GSI))

def grossOperatingIncome():
    print("Gross Operating Income: GOI = Rental Income + Other Income\n")
    RI = float(input("Rental Income: "))
    OI = float(input("Other Income: "))
    GOI = RI + OI
    print("\nGross Operating Income: $" + str(GOI))

def netOperatingIncome():
    print("Net Operating Income: NOI = Rental Income + Other Income - Total Operating Expenses\n")
    RI = float(input("Rental Income: "))
    OI = float(input("Other Income: "))
    TOE = float(input("Total Operating Expenses: "))
    NOI = RI + OI - TOE
    print("\nNet Operating Income: $" + str(NOI))

def capitalizationRate():
    print("Capitalization Rate: CR = Net Operating Income / Market Value of Property\n")
    RI = float(input("Rental Income: "))
    OI = float(input("Other Income: "))
    TOE = float(input("Total Operating Expenses: "))
    MV = float(input("Market Value of Property: "))
    CR = (RI + OI - TOE) / MV
    print("\nCapitalization Rate: " + str(CR))

def cashOnCashReturn():
    print("Cash on Cash Return: Return = Net Operating Income / Total Cash Investment\n")
    RI = float(input("Rental Income: "))
    OI = float(input("Other Income: "))
    TOE = float(input("Total Operating Expenses: "))
    TCI = float(input("Total Cash Investment: "))
    CoC = (RI + OI - TOE) / TCI
    print("\nCash on Cash Return: " + str(CoC))

def equityBuildUpRate():
    print("Equity Build-Up Rate: Rate = Mortgage Principle Paid (Year 1) / Initial Cash Invested (Year 1)\n")
    MPP = float(input("Mortgage Principle Paid (Year 1): "))
    ICI = float(input("Initial Cash Invested (Year 1): "))
    rate = MPP / ICI
    print("\nEquity Build-Up Rate: " + str(rate))

def priceToRentRatio():
    print("Price to Rent Ratio: Ratio = Purchase Price of Property / Annual Rental Revenue\n")
    pp = float(input("Purchase Price of Property: "))
    arr = float(input("Annual Rental Revenue: "))
    ratio = pp / arr
    print("\nPrice to Rent Ratio: " + str(ratio))

def pricePerSquareFoot():
    print("Price Per Square Foot: Price Per Square Foot = Market Value of Property / Property Square Footage\n")
    mv = float(input("Market Value of Property: "))
    sf = float(input("Property Square Footage: "))
    ratio = mv / sf
    print("\nPrice Per Square Foot: $" + str(ratio))

def returnOnInvestment():
    print("Return on Investment: Annual Returns / Cost of Investment\n")
    ar = float(input("Annual Returns: "))
    coi = float(input("Cost of Investment: "))
    roi = ar / coi
    print("\nReturn on Investment: " + str(roi))

def grossRentMultiplier():
    print("Gross Rent Multiplier: Market Value / Gross Scheduled Income\n")
    mv = float(input("Market Value: "))
    RI = float(input("Rental Income: "))
    LI = float(input("Lost Income from Vacant Units: "))
    GSI = RI + LI
    grm = mv / (GSI)
    print("\nGross Rent Multiplier: " + str(grm))

def debtServiceCoverageRatio():
    print("Debt Service Coverage Ratio: Net Operating Income / Annual Debt Service\n")
    RI = float(input("Rental Income: "))
    OI = float(input("Other Income: "))
    TOE = float(input("Total Operating Expenses: "))
    NOI = RI + OI - TOE
    ADS = float(input("Annual Dept Service: "))
    grm = NOI / (ADS)
    print("\nDebt Service Coverage Ratio: " + str(grm))

def chooseFunc(numSelected):        # Runs function of inputted equation number
    if numSelected == 1:
        simpleInterest()
    if numSelected == 2:
        compoundIntrest()
    if numSelected == 3:
        continouslyCompoundedInterest()
    if numSelected == 4:
        timeToDoubleMoney()
    if numSelected == 5:
        presentValueOfAnOrdinaryAnnuity()
    if numSelected == 6:
        futureValueOfAnOrdinaryAnnuity()
    if numSelected == 7:
        compoundAnnualGrowthRate()
    if numSelected == 8:
        expectedReturnOfAPortfolio()
    if numSelected == 9:
        inflationAdjustedReturn()
    if numSelected == 10:
        percentGainOrLoss()
    if numSelected == 11:
        amortization()
    if numSelected == 12:
        leverageRatio()
    if numSelected == 13:
        timeToPayCreditCard()
    if numSelected == 14:
        presentValueOfCashFlows()
    if numSelected == 15:
        capitalizationRate()
    if numSelected == 16:
        grossScheduledIncome()
    if numSelected == 17:
        grossOperatingIncome()
    if numSelected == 18:
        netOperatingIncome()
    if numSelected == 19:
        cashOnCashReturn()
    if numSelected == 20:
        equityBuildUpRate()
    if numSelected == 21:
        priceToRentRatio()
    if numSelected == 22:
        pricePerSquareFoot()
    if numSelected == 23:
        returnOnInvestment()
    if numSelected == 24:
        grossRentMultiplier()
    if numSelected == 25:
        debtServiceCoverageRatio()
    if numSelected == 26:
        continouslyCompoundedInterestMakingYearlyContrabutions()


chooseFunc(numberSelected)      # Initial Start

while 0 == 0:                   # Either continues of exits program
    x = int(input("\n\nExit: -1 || Continue: 0     -  "))
    if x == -1:
        sys.exit()
    if x == 0:
        n = int(input("\nEnter number from list: "))
        chooseFunc(n)
