from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route('/dashboard-data')
def dashboard_data():
    raw = requests.get('http://data-service:5001/data').json()
    spikes = requests.post('http://analytics-service:5002/analyze', json=raw).json()
    return jsonify({'raw': raw, 'spikes': spikes})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
