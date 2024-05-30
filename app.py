from flask import Flask, request, jsonify
import pickle
from flasgger import Swagger
import numpy as np

app = Flask(__name__)
Swagger(app)

# Load the entire pipeline
with open('grid.pkl', 'rb') as model_file:
    grid = pickle.load(model_file)


@app.route('/')
def home():
    return "Welcome to the ML Model API"


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        reviews = data.get('Reviews')
        if not reviews:
            return jsonify({'error': 'No review provided'}), 400

        # Make prediction
        my_prediction = grid.predict([reviews])

        # Convert numpy int32 to Python int
        prediction_int = int(my_prediction[0])

        # Debugging statements
        print(f'Review: {reviews}')
        print(f'Prediction: {prediction_int}')
        prediction_dect = {1: 'Positive', 0: 'Negative'}

        return jsonify({'prediction': prediction_dect[prediction_int]})
    except Exception as e:
        print(f'Error: {e}')
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
