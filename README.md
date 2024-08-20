
# Crypto Trading Bot

This project is a simple cryptocurrency trading bot that fetches real-time market data and implements a basic trading strategy using the Relative Strength Index (RSI) indicator. The bot is designed to continuously fetch data and execute trades based on predefined conditions.

## Features

- **Continuous Data Fetching**: The bot fetches the latest market prices at regular intervals and stores them in a CSV file.
- **RSI Calculation**: The bot calculates the Relative Strength Index (RSI) over a specified period to determine overbought and oversold conditions.
- **Trading Strategy**: The bot generates buy and sell signals based on RSI thresholds and simulates trades.
- **Performance Visualization**: The bot compares the performance of the trading strategy against the market return and plots the results.

## Files

- `fetch_data.py`: This script is responsible for continuously fetching cryptocurrency data from the exchange and storing it in a CSV file.
- `strategy.py`: This script implements the RSI-based trading strategy, simulates trades, and visualizes the performance of the strategy.

## Usage

### 1. Fetching Data

To start fetching data, simply run the `fetch_data.py` script:

```bash
python fetch_data.py
```

This will start fetching the price data for the specified cryptocurrency (default: `BTC/USDT`) and store it in `crypto_data.csv`. The data is fetched at an interval of 3 seconds, but you can adjust this by modifying the `sleep_time` parameter.

### 2. Running the Trading Strategy

Once you have enough data, you can run the trading strategy by executing the `strategy.py` script:

```bash
python strategy.py
```

This will calculate the RSI for the fetched data, generate buy and sell signals, simulate trades, and plot the cumulative returns of the strategy compared to the market return.

### 3. Modifying Parameters

- **Cryptocurrency Pair**: You can change the cryptocurrency pair being fetched by modifying the `symbol` parameter in `fetch_data.py`.
- **RSI Period**: The default RSI period is 14, but this can be adjusted by modifying the `period` parameter in `strategy.py`.
- **RSI Thresholds**: The default buy and sell thresholds are set to 30 and 70, respectively. You can adjust these in `strategy.py` as well.

## Requirements

- Python 3.x
- pandas
- matplotlib
- ccxt

You can install the required Python libraries using:

```bash
pip install pandas matplotlib ccxt
```

## Contributing

Feel free to fork this repository and submit pull requests if you'd like to contribute to the project.

## License

This project is licensed under the MIT License.

---


