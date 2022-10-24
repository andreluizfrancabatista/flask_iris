from flask import Flask, jsonify, render_template, request
import os

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    # return jsonify({"Choo Choo": "Welcome to your Flask app"})
    return render_template("index.html")

@app.route('/predict')
def prediction():
    if request.method == 'POST':
        return request.form.get('val1')
    else:
        return jsonify({'msg': 'use o form'})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
