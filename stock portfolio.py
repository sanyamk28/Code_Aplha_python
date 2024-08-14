import yfinance as yf

# Class for managing the stock portfolio
class StockPortfolio:
    def __init__(self):
        self.portfolio = {}

    def add_stock(self, ticker, shares):
        """Add stock to the portfolio."""
        if ticker in self.portfolio:
            self.portfolio[ticker] += shares
        else:
            self.portfolio[ticker] = shares
        print(f"Added {shares} shares of {ticker} to the portfolio.")

    def remove_stock(self, ticker, shares):
        """Remove stock from the portfolio."""
        if ticker in self.portfolio:
            if self.portfolio[ticker] > shares:
                self.portfolio[ticker] -= shares
                print(f"Removed {shares} shares of {ticker} from the portfolio.")
            elif self.portfolio[ticker] == shares:
                del self.portfolio[ticker]
                print(f"Removed all shares of {ticker} from the portfolio.")
            else:
                print(f"Error: You don't own that many shares of {ticker}.")
        else:
            print(f"Error: {ticker} is not in the portfolio.")

    def view_portfolio(self):
        """View the current portfolio and its value."""
        print("Current Portfolio:")
        total_value = 0
        for ticker, shares in self.portfolio.items():
            stock = yf.Ticker(ticker)
            price = stock.history(period="1d")['Close'][0]
            value = shares * price
            total_value += value
            print(f"{ticker}: {shares} shares @ ${price:.2f} each = ${value:.2f}")

        print(f"\nTotal Portfolio Value: ${total_value:.2f}")

# Example usage
portfolio = StockPortfolio()

# Add stocks
portfolio.add_stock("AAPL", 10)  # Add 10 shares of Apple
portfolio.add_stock("GOOGL", 5)  # Add 5 shares of Google

# View portfolio
portfolio.view_portfolio()

# Remove stocks
portfolio.remove_stock("AAPL", 5)  # Remove 5 shares of Apple

# View portfolio again
portfolio.view_portfolio()
