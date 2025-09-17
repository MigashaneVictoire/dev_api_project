from flask import Flask, request, jsonify, session, redirect, url_for
import uuid

users = {}  # username -> user_data

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-in-production'

@app.route('/')
def home():
    """Home page"""
    if 'user_id' in session:
        username = session.get('username')
        return {"User signed in": username}
    else:
        return {"User not found": None}  # fixed bug: username undefined


@app.route('/register', methods=['POST'])
def register():
    """Register a new user"""
    data = request.get_json()

    if not data:
        return jsonify({'success': False,'message': 'Invalid JSON data'}), 400

    username = data.get('username')
    password = data.get('password')

    if not username:
        return jsonify({'success': False,'message': 'Username is required'}), 400
    if not password:
        return jsonify({'success': False,'message': 'Password is required'}), 400
    if len(password) < 6:
        return jsonify({'success': False,'message': 'Password must be at least 6 characters long'}), 400
    if username in users:
        return jsonify({'success': False,'message': f'User {username} already exists'}), 400

    user_id = str(uuid.uuid4())
    users[username] = {'id': user_id, 'username': username,'password': password}
    return jsonify({'success': True, 'message': 'User registered successfully', 'user_id': user_id}), 201


@app.route('/login', methods=['POST'])
def login():
    """Authenticate user and create session"""
    data = request.get_json()
    if not data:
        return jsonify({'success': False,'message': 'Invalid JSON data'}), 400

    username = data.get('username')
    password = data.get('password')

    if not username:
        return jsonify({'success': False,'message': 'Username is required'}), 400
    if not password:
        return jsonify({'success': False,'message': 'Password is required'}), 400

    user = users.get(username)
    if not user or user['password'] != password:
        return jsonify({'success': False, 'message': 'Invalid credentials'}), 401

    session['user_id'] = user['id']
    session['username'] = username
    return jsonify({'success': True,'message': 'Login successful','user_id': user['id']}), 200


@app.route('/logout', methods=['POST'])
def logout():
    """Logout user and clear session"""
    session.clear()
    return jsonify({'success': True, 'message': 'Successfully logged out'}), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
