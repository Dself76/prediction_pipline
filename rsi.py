#should get complete history and list of 14 days rsi's so there should be ex. for bitcoin like 14 years worth
#set up for bitcoin right now but enter whatever ticker
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

class RSI:
    def __init__(self, ticker):
        self.ticker = ticker
        self.df = self.fetch_data()

    def fetch_data(self):
        """Fetch historical data for the stock over the past year."""
        stock = yf.Ticker(self.ticker)
        end_date = datetime.now()
        start_date = end_date - timedelta(days=365)
        hist_data = stock.history(start=start_date, end=end_date)
        return hist_data

    def calculate_rsi(self):
        """Extract the last 14 days of data and calculate gains, losses, and RSI."""
        data = self.df[['Open', 'Close']].tail(14)
        data['Difference'] = data['Close'] - data['Open']
        data['Result'] = data['Difference'].apply(lambda x: 'Gain' if x > 0 else 'Loss')
        total_gain = data[data['Result'] == 'Gain']['Difference'].sum()
        total_loss = abs(data[data['Result'] == 'Loss']['Difference'].sum())
        rsi = 100 - (100 / (1 + (total_gain / total_loss)))
        return round(rsi, 2)

def main():
    ticker_symbol = input("Enter the stock ticker symbol (e.g., AAPL for Apple): ").upper()
    try:
        rsi_calculator = RSI(ticker_symbol)
        rsi = rsi_calculator.calculate_rsi()
        print(f"RSI for the last 14 days of {ticker_symbol}: {rsi}")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check if the ticker symbol is correct and try again.")

if __name__ == "__main__":
    main()

'''#this is the code used for jupyter notebook
import pandas as pd
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
def data(ticker):
    stock = yf.Ticker(ticker)
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    hist_data = stock.history(start=start_date, end=end_date)
    
    return hist_data
user_ticker = input("Enter the stock ticker symbol (e.g., AAPL for Apple): ").upper()
try:# Fetch the data
    df = data(user_ticker)
    
    # Display basic information about the DataFrame
    print(f"\nHistorical data for {user_ticker}:")
    print(f"Date range: {df.index[0].date()} to {df.index[-1].date()}")
    print(f"Number of trading days: {len(df)}")
    print("\nFirst few rows of the data:")
    print(df.head())
    
    # Optional: Save to CSV
    csv_filename = f"{user_ticker}_1year_history.csv"
    df.to_csv(csv_filename)
    print(f"\nData saved to {csv_filename}")
except Exception as e:
    print(f"An error occurred: {e}")
    print("Please check if the ticker symbol is correct and try again.")
    # Extract the last 14 days of open and close prices
last_14_days = df[['Open', 'Close']].tail(14)

# Display the result
print(last_14_days)
# Create new columns to store the result (Gain/Loss) and the difference
last_14_days['Difference'] = 0.0  # Explicitly set the dtype to float
last_14_days['Result'] = ''

for index, row in last_14_days.iterrows():
    open_price = row['Open']
    close_price = row['Close']
    # Calculate the difference
    difference = close_price - open_price
    # Determine if it's a gain or loss
    result = 'Gain' if difference > 0 else 'Loss'
    # Store the result and the difference in the DataFrame
    last_14_days.at[index, 'Difference'] = difference
    last_14_days.at[index, 'Result'] = result

# Filter for gains and losses
gains = last_14_days[last_14_days['Result'] == 'Gain']
losses = last_14_days[last_14_days['Result'] == 'Loss']

# Sum the 'Difference' column for each filtered DataFrame
total_gain = gains['Difference'].sum()
total_loss = losses['Difference'].sum()

# Display the result
print(last_14_days)
print("Total Gain:", total_gain)
print("Total Loss:", total_loss)
# Sum the 'Difference' column for each filtered DataFrame
total_gain = gains['Difference'].sum()
total_loss = losses['Difference'].sum()

# Display the total gain and total loss
print("Total Gain:", total_gain)
print("Total Loss:", total_loss)
total_loss = abs(total_loss)

RSI = 100 - (100 / (1 + (total_gain / total_loss)))
RSI = round(RSI,2)
print(RSI)

    

'''