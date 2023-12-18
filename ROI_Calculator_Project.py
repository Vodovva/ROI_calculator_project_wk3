class Calc:
    def __init__(self, purchase_price, rental_income, expenses, flow, cash_deposit):
        self.purchase_price = purchase_price
        self.rental_income = rental_income
        self.expenses = expenses
        self.flow = flow
        self.cash_deposit = cash_deposit

    def cash_flow(self):
        return self.rental_income - self.expenses

    def ROI_with_cash_deposit(self):
        cash_flow = self.calculate_cash_flow()
        total_investment = self.purchase_price + self.ROI_with_cash_deposit
        roi = (cash_flow / total_investment) * 100
        return roi

def main():
    purchase_price = float(input("Enter the price of the property: "))
    rental_income = float(input("Enter your monthly rental income: "))
    expenses = float(input("Enter your total monthly expenses: "))
    cash_deposit = float(input("Enter the cash deposit: "))

    calc = main(purchase_price, rental_income, expenses, cash_deposit)

    cash_flow = calc.cash_flow()
    roi = calc.ROI_with_cash_deposit()

    print(f"Monthly Cash Flow: ${cash_flow:.2f}")
    print(f"ROI and Cash Deposit: {roi:.2f}%")

