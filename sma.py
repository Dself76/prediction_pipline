import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

class StockDataFetcher:
    def __init__(self, ticker):
        self.ticker = ticker.upper()
        self.stock = yf.Ticker(self.ticker)
        self.end_date = datetime.now()
        self.start_date = self.end_date - timedelta(days=365)
        self.hist_data = None
        self.sma_results = {}

    def fetch_data(self):
        """Fetch historical stock data for the past year."""
        try:
            self.hist_data = self.stock.history(start=self.start_date, end=self.end_date)
            print(f"\nHistorical data for {self.ticker}:")
            print(self.hist_data)
            self.save_to_csv()
            self.calculate_sma()
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please check if the ticker symbol is correct and try again.")

    def save_to_csv(self):
        """Save the historical data to a CSV file."""
        if self.hist_data is not None:
            csv_filename = f"{self.ticker}_1year_history.csv"
            self.hist_data.to_csv(csv_filename)
            print(f"\nData saved to {csv_filename}")

    def calculate_sma(self):
        """Calculate the sum of closing prices for each 14-day period."""
        if self.hist_data is not None:
            df = self.hist_data.sort_index(ascending=False)
            for i in range(0, len(df) - 14 + 1, 14):
                current_closes = df['Close'].iloc[i:i+14]
                sum_of_closes = current_closes.sum()
                end_date = df.index[i].strftime('%Y-%m-%d')
                start_date = df.index[min(i+13, len(df)-1)].strftime('%Y-%m-%d')
                self.sma_results[f'{start_date} to {end_date}'] = sum_of_closes
            self.print_sma_results()

    def print_sma_results(self):
        """Print the calculated SMA results."""
        for period, sum_value in self.sma_results.items():
            print(f"Sum of closing prices for {period}: {sum_value}")

# Example usage
user_ticker = input("Enter the stock ticker symbol (e.g., AAPL for Apple or BTC-USD for bitcoin): ")
stock_fetcher = StockDataFetcher(user_ticker)
stock_fetcher.fetch_data()
