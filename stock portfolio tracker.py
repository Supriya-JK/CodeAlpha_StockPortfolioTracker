# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 200,
    "MSFT": 400
}

total_investment = 0

print("===== Stock Portfolio Tracker =====")
print("Available stocks:", ", ".join(stock_prices.keys()))

while True:
    stock = input("\nEnter stock name (or type 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock] * quantity
        total_investment += investment

        print("Stock price:", stock_prices[stock])
        print("Investment for", stock, ":", investment)
    else:
        print("Stock not found. Please enter a valid stock.")

print("\n===== Portfolio Summary =====")
print("Total Investment Value: ₹", total_investment)
print("Thank you!")