from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

users = {}
LIMIT = 5
fighters_list = []


@app.route('/')
@app.route('/apex.com')
def apex():
    return "<h1> LOG IN </h1> <h4> SIGN IN </h4>"

@app.route('/login', methods=["POST"])
def log_in():
    data = request.get_json()
    email = data.get("email")
    password = data.get('password')

@app.route('/signup', methods=['POST'])
def sign_up():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name or not email or not password:
        return jsonify({"error": "name,email,password required"}), 400

    if email in users:
        return jsonify({"message": "email is already registerd"}), 409

    users[email] = password
    return jsonify({"message": "user created"}), 201

@app.route('/mainmenu')
def main_menu():
    return '<h1>profile, events, fighters, settings</h1>'

@app.route('/profile/<name>')
def profile(name):
    return f'<h1>name: {name}</h1>'

@app.route('/events')
def events():
    try:
        url = 'http://127.0.0.1:3000/fights'
        response = requests.get(url)
        fights = response.json()
        return jsonify(fights)
    except requests.exceptions.RequestException:
        return jsonify({'error': 'sorry we are having problems try later :('})

@app.route('/fighter/<name>')
def fighters(name):
    try:
        response = requests.get('http://127.0.0.1:5001/fighters')
        data = response.json()
        for fighter in data:
            if fighter['name'].upper() == name.upper():
                return jsonify({'name': fighter['name'], 'division': fighter['division'], 'rank': fighter['rank'], 'record': fighter['record']})
            elif fighter not in data:
                return jsonify({'message': 'couldnt find the fighter'})
    except requests.exceptions.RequestException:
        return jsonify({'error': 'sorry we are having problems try later :('})

@app.route('/top-5', methods=['POST', 'DELETE', 'GET'])
def top_fighters():
    data = request.get_json()
    fighter = data.get('fighter')
    if request.method == 'GET':
        return jsonify(fighters_list)
    
    if request.method == 'POST':
        if len(fighters_list) >= LIMIT:
            return jsonify({'error': 'You have reached your limit list please remove a fighter to add another one'})
        fighters_list.append(fighter)
        return jsonify({'message': 'Fighter added in your list'}), 201
    
    if request.method == 'DELETE':
        if fighter not in fighters_list:
            return jsonify({'error': 'Fighter not in your list'}), 404
        fighters_list.remove(fighter)
        return jsonify({'message': 'Fighter removed from your list'}), 200

@app.route('/settings')
def settings():
    return ''

if __name__ == '__main__':
    app.run(debug=True)