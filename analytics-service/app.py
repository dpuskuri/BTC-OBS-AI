from flask import Flask, jsonify
import requests
import pandas as pd

app = Flask(__name__)

BINANCE_URL = "https://api.binance.com/api/v3/klines"

@app.route('/data')
def get_data():
    params = {
        "symbol": "BTCUSDT",
        "interval": "1h",
        "limit": 500
    }
    raw = requests.get(BINANCE_URL, params=params).json()

    df = pd.DataFrame(raw, columns=[
        'open_time', 'open', 'high', 'low', 'close', 'volume',
        'close_time', 'quote_asset_volume', 'num_trades',
        'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'
    ])
    # Return only essential columns
    df_result = df[['open_time', 'open', 'high', 'low', 'close', 'volume']]

    return jsonify(df_result.to_dict(orient="records"))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

