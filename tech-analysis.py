import ccxt
import pandas as pd
import time

class TechIndicatorEngine:
    def __init__(self, symbol='BTC/USDT'):
        self.exchange = ccxt.binance()
        self.symbol = symbol

    def fetch_historical_ohlcv(self, timeframe='1h', limit=100):
        """Fetch historical candle data"""
        print(f"Fetching {limit} candles for {self.symbol}...")
        rows = self.exchange.fetch_ohlcv(self.symbol, timeframe, limit=limit)
        df = pd.DataFrame(rows, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        return df

    def apply_indicators(self, df):
        df['sma_fast'] = df['close'].rolling(window=9).mean()
        df['sma_slow'] = df['close'].rolling(window=21).mean()

        delta = df['close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        df['rsi'] = 100 - (100 / (1 + rs))
        
        return df

    def get_signal(self, df):
        last_row = df.iloc[-1]
        
        if last_row['sma_fast'] > last_row['sma_slow'] and last_row['rsi'] < 70:
            return "BUY (Trend Up + Not Overbought)"
        elif last_row['sma_fast'] < last_row['sma_slow'] or last_row['rsi'] > 70:
            return "SELL (Trend Down or Overbought)"
        else:
            return "HOLD"
        
    def generate_signals(self, df):
        df['signal'] = 'HOLD'
        df.loc[(df['sma_fast'] > df['sma_slow']) & (df['rsi'] < 70), 'signal'] = 'BULLISH'
        df.loc[(df['sma_fast'] < df['sma_slow']) | (df['rsi'] > 70), 'signal'] = 'BEARISH'
        return df

engine = TechIndicatorEngine('BTC/USDT')
data = engine.fetch_historical_ohlcv()
data_with_indicators = engine.apply_indicators(data)

print("\n--- Latest Analysis ---")
print(data_with_indicators[['timestamp', 'close', 'sma_fast', 'rsi']].tail(5))
print(f"\nCURRENT SIGNAL: {engine.get_signal(data_with_indicators)}")

data = engine.fetch_historical_ohlcv()
data = engine.apply_indicators(data)
data = engine.generate_signals(data)
data.to_csv("btc_history.csv", index=False)
print("Saved 100 candles with signals to btc_history.csv")