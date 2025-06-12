# import yfinance as yf
# import pandas as pd

# # List of 20 stock ticker symbols (you can change/add more)
# tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'TSLA', 'NFLX', 'NVDA', 'JPM', 'BAC',
#            'TCS.NS', 'INFY.NS', 'RELIANCE.NS', 'HDFCBANK.NS', 'ICICIBANK.NS', 
#            'SBIN.NS', 'ITC.NS', 'HINDUNILVR.NS', 'WIPRO.NS', 'BHARTIARTL.NS']

# # Define time period
# start_date = "2015-01-01"
# end_date = "2024-12-31"

# # Dictionary to hold data
# all_data = {}

# for ticker in tickers:
#     print(f"Downloading {ticker}...")
#     data = yf.download(ticker, start=start_date, end=end_date)
#     data["Ticker"] = ticker
#     all_data[ticker] = data

# # Combine all data into one DataFrame
# combined_df = pd.concat(all_data.values())

# # Reset index and save to CSV
# combined_df.reset_index(inplace=True)
# combined_df.to_csv("20_stocks_data_2015_to_2024.csv", index=False)

# print("✅ Data download complete! Saved as '20_stocks_data_2015_to_2024.csv'")














# import yfinance as yf
# import pandas as pd

# # Base tickers (20 you had before)
# base_tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'TSLA', 'NFLX', 'NVDA', 'JPM', 'BAC',
#                 'TCS.NS', 'INFY.NS', 'RELIANCE.NS', 'HDFCBANK.NS', 'ICICIBANK.NS', 
#                 'SBIN.NS', 'ITC.NS', 'HINDUNILVR.NS', 'WIPRO.NS', 'BHARTIARTL.NS']

# # More Indian stocks
# more_indian_stocks = [
#     'AXISBANK.NS', 'MARUTI.NS', 'LT.NS', 'BAJAJFINSV.NS', 'BAJFINANCE.NS',
#     'KOTAKBANK.NS', 'HCLTECH.NS', 'ADANIENT.NS', 'ADANIPORTS.NS', 'TITAN.NS',
#     'DRREDDY.NS', 'CIPLA.NS', 'SUNPHARMA.NS', 'ULTRACEMCO.NS', 'COALINDIA.NS',
#     'POWERGRID.NS', 'NTPC.NS', 'TECHM.NS', 'VEDL.NS', 'ASIANPAINT.NS',
#     'M&M.NS', 'BRITANNIA.NS', 'DIVISLAB.NS', 'EICHERMOT.NS', 'HEROMOTOCO.NS'
# ]

# # More US stocks
# more_us_stocks = [
#     'ORCL', 'INTC', 'CSCO', 'PEP', 'KO', 'V', 'MA', 'PYPL', 'IBM', 'CRM',
#     'ADBE', 'AVGO', 'QCOM', 'TXN', 'AMD', 'BMY', 'JNJ', 'PFE', 'WMT', 'COST',
#     'DIS', 'NKE', 'XOM', 'CVX', 'BA'
# ]

# # Combine all tickers
# tickers = base_tickers + more_indian_stocks + more_us_stocks

# # Date range
# start_date = "2015-01-01"
# end_date = "2024-12-31"

# # Empty list to store data
# all_data = []

# # Downloading data
# for ticker in tickers:
#     print(f"📥 Downloading data for: {ticker}")
#     try:
#         data = yf.download(ticker, start=start_date, end=end_date)
#         if not data.empty:
#             data["Ticker"] = ticker
#             all_data.append(data)
#     except Exception as e:
#         print(f"❌ Failed to download {ticker}: {e}")

# # Combine all into one DataFrame
# combined_df = pd.concat(all_data)
# combined_df.reset_index(inplace=True)

# # Save to CSV
# combined_df.to_csv("all_80_stocks_2015_to_2024.csv", index=False)

# print("✅ All data downloaded and saved as 'all_80_stocks_2015_to_2024.csv'")
















# import yfinance as yf
# import pandas as pd
# import os

# # ✅ List of tickers (Indian + US stocks)
# tickers = [
#     'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'TSLA', 'NFLX', 'NVDA', 'JPM', 'BAC',
#     'TCS.NS', 'INFY.NS', 'RELIANCE.NS', 'HDFCBANK.NS', 'ICICIBANK.NS',
#     'SBIN.NS', 'ITC.NS', 'HINDUNILVR.NS', 'WIPRO.NS', 'BHARTIARTL.NS',
#     'AXISBANK.NS', 'MARUTI.NS', 'LT.NS', 'BAJAJFINSV.NS', 'BAJFINANCE.NS',
#     'KOTAKBANK.NS', 'HCLTECH.NS', 'ADANIENT.NS', 'ADANIPORTS.NS', 'TITAN.NS',
#     'DRREDDY.NS', 'CIPLA.NS', 'SUNPHARMA.NS', 'ULTRACEMCO.NS', 'COALINDIA.NS',
#     'POWERGRID.NS', 'NTPC.NS', 'TECHM.NS', 'VEDL.NS', 'ASIANPAINT.NS',
#     'M&M.NS', 'BRITANNIA.NS', 'DIVISLAB.NS', 'EICHERMOT.NS', 'HEROMOTOCO.NS',
#     'ORCL', 'INTC', 'CSCO', 'PEP', 'KO', 'V', 'MA', 'PYPL', 'IBM', 'CRM',
#     'ADBE', 'AVGO', 'QCOM', 'TXN', 'AMD', 'BMY', 'JNJ', 'PFE', 'WMT', 'COST',
#     'DIS', 'NKE', 'XOM', 'CVX', 'BA'
# ]

# # ✅ Download config
# start_date = "2001-01-01"
# end_date = "2024-12-31"

# # ✅ Download new data
# all_data = []
# for ticker in tickers:
#     print(f"📥 Downloading: {ticker}")
#     try:
#         df = yf.download(ticker, start=start_date, end=end_date)
#         if not df.empty:
#             df['Ticker'] = ticker
#             all_data.append(df)
#     except Exception as e:
#         print(f"❌ Failed: {ticker} — {e}")

# # ✅ Combine downloaded data
# new_data = pd.concat(all_data)
# new_data.reset_index(inplace=True)

# # ✅ Keep only required columns
# columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'Ticker']
# new_data = new_data[columns]

# # ✅ Check if old merged file exists
# file_path = "final_merged_stock_data.csv"
# if os.path.exists(file_path):
#     print("📂 Merging with old dataset...")
#     old_data = pd.read_csv(file_path)
#     combined = pd.concat([old_data, new_data])
#     combined.drop_duplicates(subset=['Date', 'Ticker'], keep='first', inplace=True)
# else:
#     print("🆕 No old data found. Using new data only.")
#     combined = new_data

# # ✅ Sort and save
# combined.sort_values(by=['Ticker', 'Date'], inplace=True)
# combined.to_csv(file_path, index=False)

# print("✅ Final merged data saved to 'final_merged_stock_data.csv'")















import yfinance as yf
import pandas as pd
import os

# ✅ List of tickers
tickers = [
   'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'META', 'TSLA', 'NFLX', 'NVDA', 'JPM', 'BAC',
    'TCS.NS', 'INFY.NS', 'RELIANCE.NS', 'HDFCBANK.NS', 'ICICIBANK.NS',
    'SBIN.NS', 'ITC.NS', 'HINDUNILVR.NS', 'WIPRO.NS', 'BHARTIARTL.NS',
    'AXISBANK.NS', 'MARUTI.NS', 'LT.NS', 'BAJAJFINSV.NS', 'BAJFINANCE.NS',
    'KOTAKBANK.NS', 'HCLTECH.NS', 'ADANIENT.NS', 'ADANIPORTS.NS', 'TITAN.NS',
    'DRREDDY.NS', 'CIPLA.NS', 'SUNPHARMA.NS', 'ULTRACEMCO.NS', 'COALINDIA.NS',
    'POWERGRID.NS', 'NTPC.NS', 'TECHM.NS', 'VEDL.NS', 'ASIANPAINT.NS',
    'M&M.NS', 'BRITANNIA.NS', 'DIVISLAB.NS', 'EICHERMOT.NS', 'HEROMOTOCO.NS',
    'ORCL', 'INTC', 'CSCO', 'PEP', 'KO', 'V', 'MA', 'PYPL', 'IBM', 'CRM',
    'ADBE', 'AVGO', 'QCOM', 'TXN', 'AMD', 'BMY', 'JNJ', 'PFE', 'WMT', 'COST',
    'DIS', 'NKE', 'XOM', 'CVX', 'BA'
]

start_date = "2001-01-01"
end_date = "2024-12-31"

# ✅ Download all data
all_data = []
for ticker in tickers:
    print(f"📥 Downloading: {ticker}")
    try:
        df = yf.download(ticker, start=start_date, end=end_date)
        if not df.empty:
            df["Ticker"] = ticker
            df.reset_index(inplace=True)
            
            # ✅ Fill missing columns if needed
            for col in ['Adj Close']:
                if col not in df.columns:
                    df[col] = df['Close']  # fallback to Close if Adj Close missing
            
            all_data.append(df)
    except Exception as e:
        print(f"❌ Error for {ticker}: {e}")

# ✅ Combine downloaded data
if all_data:
    new_data = pd.concat(all_data, ignore_index=True)

    # ✅ Clean columns (make sure all are present)
    columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume', 'Ticker']
    new_data = new_data[[col for col in columns if col in new_data.columns]]
else:
    print("🚫 No data downloaded.")
    exit()

# ✅ Merge with old data if exists
file_path = "final_merged_stock_data.csv"
if os.path.exists(file_path):
    print("📂 Merging with old dataset...")
    old_data = pd.read_csv(file_path)

    # Ensure same columns
    old_data = old_data[new_data.columns]  # match columns
    combined = pd.concat([old_data, new_data])
    combined.drop_duplicates(subset=['Date', 'Ticker'], keep='first', inplace=True)
else:
    print("🆕 No old data found. Using new data only.")
    combined = new_data

# ✅ Save clean merged file
combined.sort_values(by=['Ticker', 'Date'], inplace=True)
combined.to_csv(file_path, index=False)

print("✅ Final merged stock data saved at:", file_path)
