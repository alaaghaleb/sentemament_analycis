from flask import Flask, render_template, request
import pickle
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

# Load the entire pipeline
# Load the entire pipeline
with open(r'C:\Users\MOBI LAP\Downloads\Imdb-Sentiment-Analysis-Flask-Deployment--Heroku-master\Imdb-Sentiment-Analysis-Flask-Deployment--Heroku-master\grid.pkl', 'rb') as model_file:
    grid = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            Reviews = request.form['Reviews']
            data = [Reviews]
            my_prediction = grid.predict(data)

            # Debugging statements
            print(f'Review: {Reviews}')
            print(f'Prediction: {my_prediction}')

            return render_template('result.html', prediction=my_prediction)
        except Exception as e:
            print(f'Error: {e}')
            return render_template('result.html', prediction='Error in prediction')

if __name__ == '__main__':
    app.run(debug=True)
