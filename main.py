from flask import Flask, jsonify, render_template, request
import os

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def prediction():
    if request.method == 'POST':
        return jsonify(request.form)
    else:
        return jsonify({'msg': 'use o form'})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
