import pandas as pd
import time
import os
import ccxt #lib for crypto


exchange = ccxt.coinbase()

#Fetch data

'''
symbol ='DOGE/USDT' #
ticker = exchange.fetch_ticker(symbol)
print(ticker)
'''

#fetch crypto data and store it in an interval
def continous_fetch_and_store(sleep_time, filename='crypto_data.csv',symbol ='BTC/USDT'):

    while True:
        try: 
            ticker = exchange.fetch_ticker(symbol)
            current_date = time.strftime("%Y-%m-%d")
            current_time = time.strftime('%H:%M:%S')
            price= ticker['last']

            # Combine date and time into a single datetime string
            datetime_str = f"{current_date} {current_time}"


            data=[[current_date,current_time,price]]

            # Create a DataFrame with the new data
            data = [[datetime_str, price]]
            dataframe = pd.DataFrame(data, columns=['Datetime', 'Price'])

            # Check if file exists to determine if headers should be written
            file_exists = os.path.isfile(filename)

            #convert to csv and append
            dataframe.to_csv(filename, index=False, mode='a', header=not file_exists)
            print(price)

            time.sleep(sleep_time)

        except Exception as e:
            print(f"Error fetching data: {e}")    

continous_fetch_and_store(3) #fetch and store every 3 secs



