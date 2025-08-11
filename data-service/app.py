from flask import Flask, jsonify
from binance.client import Client
import os
import pandas as pd

app = Flask(__name__)

# Load Binance API Key/Secret from environment variables (security best practice)
BINANCE_API_KEY = os.environ.get("BINANCE_API")
BINANCE_API_SECRET = os.environ.get("BINANCE_SECRET")

# Initialize Binance Client
client = Client(api_key=BINANCE_API_KEY, api_secret=BINANCE_API_SECRET)

@app.route('/data')
def get_data():
    # Fetch last 500 hourly candles for BTC/USDT
    klines = client.get_klines(symbol='BTCUSDT', interval=Client.KLINE_INTERVAL_1HOUR, limit=500)

    # Convert to DataFrame with readable column names
    df = pd.DataFrame(klines, columns=[
        'open_time', 'open', 'high', 'low', 'close', 'volume',
        'close_time', 'quote_asset_volume', 'num_trades',
        'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'
    ])

    # Only keep essential fields
    df_result = df[['open_time', 'open', 'high', 'low', 'close', 'volume']]

    return jsonify(df_result.to_dict(orient="records"))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

