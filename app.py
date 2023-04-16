from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)

# authentication API
@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']

    if username == 'admin' and password == '1234':
        return jsonify({'message': 'Login successful!'})
    return jsonify({'message': 'Invalid username or password'}), 401

# Sign up
@app.route('/Signup', methods=['POST'])
def signup():
    msg = ''
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    if re.match(r'[A-Za-z0-9]+', username):
        msg = 'Signed Up successfully'
        print(username, email)
    else:
        return jsonify({'message': 'Username must contain only characters and numbers.'}), 401

    return jsonify({'msg': msg})

if __name__ == '__main__':
    app.run(debug=True)