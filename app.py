from flask import Flask,jsonify,request
from classifier import get_prediction

app = Flask(__name__)
print("Hello")
@app.route("/predict_digit",methods=["POST"])

def predict_data():
    image = request.files.get("digit")
    prediction = get_prediction("digit")
    return jsonify({
        "prediction" : prediction
    }),200
    
if __name__ == "__main__":
    app.run(debug=True)  