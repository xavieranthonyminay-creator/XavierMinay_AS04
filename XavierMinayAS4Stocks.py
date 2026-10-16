def display_stock(symbol, shares, price):
    print(f"Stock: {symbol}")
    print(f"Shares: {shares}")
    print(f"Price per share: ${price:.2f}")

def compute_total(shares, price):
    return shares * price

def main():
    symbol = input("Enter stock symbol: ").upper()
    shares = int(input("Enter number of shares: "))
    price = float(input("Enter price per share: "))
    
    display_stock(symbol, shares, price)
    total = compute_total(shares, price)
    print(f"Total value: ${total:,.2f}")

if __name__ == "__main__":
    main()