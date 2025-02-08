from flask import Flask, request, jsonify
import pickle

# Initialize the Flask app
app = Flask(__name__)

# Load the model
model = pickle.load(open('sales_pred.pkl', 'rb'))

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get form values from the request
    
            tv = request.args.get(tv)
            radio = request.args.get(radio)
            newspaper = request.args.get(newspaper)

            # Make prediction
            prediction = model.predict([[tv, radio, newspaper]])

            # Return the prediction result as a JSON response
            return jsonify({'predicted_value': round(prediction[0], 2)})
        except Exception as e:
            return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
