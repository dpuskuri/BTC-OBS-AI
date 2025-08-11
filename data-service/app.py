rom flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/data')
def get_data():
    url = "https://api.binance.com/api/v3/klines?symbol=BTCUSDT&interval=1h&limit=1000"
    raw = requests.get(url).json()
    # Format data for downstream usage
    return jsonify(raw)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
