
def main(income, car_price, loan_amount,interest,loan_years):
    min = int(income*0.1)
    emi = emi_calculator(loan_amount,interest,loan_years)

    print(f"\nYour Down payment should be 20 % almost ₹ {car_price*0.2}")
    print(f"\nYour monthly Emi is ₹ {emi:.2f}")

    if(emi < min):
        print("\nAnkur warikoo(Fack GURU) : You can afford car 😊😊😊\n")
    else:
        print("\nAnkur warikoo(Fack GURU) : You can't afford car 😔😔😔\n")
    

def emi_calculator(loan_amount,interest,loan_years):
    year = loan_years
    monthly_rate = (interest / 100) / 12
    
    emi = loan_amount * (monthly_rate * (1 + monthly_rate) ** (year*12)) / \
        ((1 + monthly_rate) ** (year*12) - 1)
    return emi


if __name__ == "__main__":
    income       =  int(input("\nwhat is your monthly income ₹ : \n"))
    car_price    =  int(input("\nHow many ₹ do you want to buy a car? : \n"))
    loan_amount  =  int(input("\nhow much loan to you have : \n"))
    loan_years   =  int(input("\nhow many year to have loan : \n"))
    interest     =  int(input("\nwhat is interest rate for car loan % : \n"))

    main(income, loan_amount, loan_amount, interest, loan_years)