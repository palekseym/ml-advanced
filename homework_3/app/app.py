import pickle
import numpy as np

from flask import Flask, request
from collections import OrderedDict


app = Flask(__name__)

model = None
scaler = None

@app.route('/predict', methods=['POST'])
def predict():
    global model, scaler

    data = request.get_json()
    order_data = OrderedDict()
    for i in ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']:
        order_data[i] = 0

    for key in order_data.keys():
        order_data[key] = data[key]

    x = np.array([order_data[key] for key in order_data.keys()])[np.newaxis, :]
    x = scaler.transform(x)

    return str(model.predict(x)[0])


def load_model():
    global model, scaler
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    with open('scaler.pkl', 'rb') as f:
        scaler = pickle.load(f)


if __name__ == '__main__':
    load_model()
    app.run(host='0.0.0.0', port=80)