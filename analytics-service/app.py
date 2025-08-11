from flask import Flask, request, jsonify
import numpy as np
import pandas as pd

app = Flask(__name__)

def detect_spikes(data):
    df = pd.DataFrame(data)
    zscores = np.abs((df['volume'] - df['volume'].mean()) / df['volume'].std())
    spikes = df[zscores > 2]
    return spikes.to_dict()

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.json
    spikes = detect_spikes(data)
    return jsonify(spikes)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
