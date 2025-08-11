from flask import Flask, request, jsonify
import pandas as pd
import numpy as np

app = Flask(__name__)

def detect_spikes(data):
    df = pd.DataFrame(data)
    df['volume'] = pd.to_numeric(df['volume'], errors='coerce')
    zscores = np.abs((df['volume'] - df['volume'].mean()) / df['volume'].std())
    spikes = df[zscores > 2]
    return spikes.to_dict(orient="records")

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()
        spikes = detect_spikes(data)
        return jsonify({"spikes": spikes})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

