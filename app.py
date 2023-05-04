from flask import Flask, request, jsonify, session
from flask_cors import CORS
import re
from datetime import timedelta
from flask_session import Session
from config import ApplicationConfig

app = Flask(__name__)
app.config.from_object(ApplicationConfig)
cors = CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)

server_session = Session(app)


# authentication API
@app.route('/login', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    print(request)
    if username == 'admin' and password == '1234':
        session['username'] = username
        session['loggedin'] = True
        print(session)
        return jsonify({'message': 'Login successful!', 'success': True})
    return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/@me')
def get_info():
    username = session.get('username')
    if not username:
        return jsonify({'error': 'Unauthorized'}), 400
    
    return jsonify({'user': username})

#Check if user logged in
@app.route('/api/checklogin')
def check_login():
    username = session.get('username')
    if username:
        print('hi')
        return jsonify({'username': username, 'isLoggedIn': True})
    else:
        return jsonify({'isLoggedIn': False})
    
# log out
@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('username', None)
    return jsonify({'message': 'logged out', 'loggedin': False})


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