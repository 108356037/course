from flask import Flask, jsonify, request, render_template

app = Flask(__name__, template_folder='templates/')

stores = [{
    'name': 'My Store',
    'items': [{'name': 'my item', 'price': 15.99}]
}]


@app.route('/')
def home():
    return render_template('index.html')

# post /store data: {name :}


@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)
    # pass

# get /store/<name> data: {name :}


@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})
    # pass

#get /store


@app.route('/ping')
def get_pong():
    return jsonify({'message':'pong'})


app.run(debug=True, host='0.0.0.0', port=5000)
