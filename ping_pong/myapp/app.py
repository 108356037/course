from flask import Flask, jsonify, request, render_template

app = Flask(__name__, template_folder='templates/')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ping')
def get_pong():
    return jsonify({'message':'pong'})


app.run(debug=True, host='0.0.0.0', port=5000)
