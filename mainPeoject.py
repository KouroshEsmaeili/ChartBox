import yfinance as yf
import pandas as pd


class StockAnalyzer:
    def __init__(self, symbol, start_date, end_date):
        self.symbol = symbol
        self.startDate = start_date
        self.endDate = end_date
        self.Data = None

    def download_data(self):
        self.Data = yf.download(self.symbol, start=self.startDate, end=self.endDate)

    def identify_candle_type(self):
        if self.Data is not None:
            self.Data['Candle_Type'] = 'Bearish'
            self.Data.loc[self.Data['Close'] > self.Data['Open'], 'Candle_Type'] = 'Bullish'
        else:
            print("Error: Data not downloaded. Call download_data() first.")

    def display_data(self):
        if self.Data is not None:
            print(self.Data)
        else:
            print("Error: Data not available. Call download_data() first.")


def main():
    symbol = "AAPL"
    start_date = pd.to_datetime("today") - pd.DateOffset(years=1)
    end_date = pd.to_datetime("today")

    stock_analyzer = StockAnalyzer(symbol, start_date, end_date)

    stock_analyzer.download_data()
    stock_analyzer.identify_candle_type()
    stock_analyzer.display_data()


if __name__ == "__main__":
    main()
    
