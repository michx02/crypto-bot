import pandas as pd
import numpy as np


# Load historical data
df = pd.read_csv('crypto_data.csv')

# Sort by datetime
df.sort_values(by='Datetime', inplace=True)

#Calculate RSI(relative strength Index) for a period of 14
def calculate_rsi(df, period=14):
    delta = df['Price'].diff()
    print(delta)
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss  #relative strength
    rsi = 100 - (100 / (1 + rs))
    return rsi

df['RSI'] = calculate_rsi(df)

# Define Strategy Parameters
rsi_buy_threshold = 30
rsi_sell_threshold = 70

# Generate Buy/Sell Signals
df['Signal'] = 0  # Default to no signal
df.loc[df['RSI'] < rsi_buy_threshold, 'Signal'] = 1  # Buy Signal
df.loc[df['RSI'] > rsi_sell_threshold, 'Signal'] = -1  # Sell Signal

# Simulate Trades
df['Position'] = df['Signal'].replace(0, np.nan).ffill().shift()
df['Daily_Return'] = df['Price'].pct_change()
df['Strategy_Return'] = df['Position'] * df['Daily_Return']

# Performance Metrics
df['Cumulative_Strategy_Return'] = (1 + df['Strategy_Return']).cumprod() - 1
df['Cumulative_Market_Return'] = (1 + df['Daily_Return']).cumprod() - 1

# Print Results
print(df[['Datetime', 'Price', 'RSI', 'Signal', 'Cumulative_Strategy_Return', 'Cumulative_Market_Return']].tail(30))

# Plot Performance
import matplotlib.pyplot as plt

plt.figure(figsize=(14, 7))
plt.plot(df['Datetime'], df['Cumulative_Market_Return'], label='Market Return')
plt.plot(df['Datetime'], df['Cumulative_Strategy_Return'], label='Strategy Return')
plt.xlabel('Date')
plt.ylabel('Cumulative Return')
plt.title('Strategy vs Market Return')
plt.legend()
plt.show()


