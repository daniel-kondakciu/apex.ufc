from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

users = {}
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
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({"error": "name,email,password required"}), 400
    if username in users:
        return ({"error": "the username is already taken"}), 409
    if email in users:
        return jsonify({"error": "email is already registerd"}), 409
    if "@" not in email:
        return ({"error": "email is missing @"}), 409
    if ".com" not in email:
        return ({"error": "email is missing .com"}), 409
    if len(password) < 8:
        return ({"error": "password must be 8 or more characters"}), 409

    users[email] = password
    return jsonify({"message": "user created"}), 201

@app.route('/mainmenu')
def main_menu():
    return '<h1>profile, events, fighters, top 5, settings</h1>'

@app.route('/profile/<name>')
def profile(name):
    return f'<h1>name: {name}</h1>'

@app.route('/events/<ufc_event>', methods=['GET'])
def events(ufc_event):
    try:
        url = 'http://127.0.0.1:3000/fights'
        response = requests.get(url)
        fights = response.json()
        for e in fights:
            if e['ufc_event'].lower() == ufc_event.lower():
                return jsonify({'ufc': e['ufc_event'], 'card': e['card'], 'division': e['division'], 'title fight': e['title_bout'], 'fight': e['fight']})
        return jsonify({"error": "event not found"})
    except requests.exceptions.RequestException:
        return jsonify({'error': 'sorry we are having problems try later :('})

@app.route('/fighter/<name>', methods=['GET'])
def fighters(name):
    try:
        response = requests.get('http://127.0.0.1:5001/fighters')
        data = response.json()
        for fighter in data:
            if fighter['name'].lower() == name.lower():
                return jsonify({'name': fighter['name'], 'division': fighter['division'], 'rank': fighter['rank'], 'record': fighter['record']})
        return jsonify({"error": "fighter not found"})
    except requests.exceptions.RequestException:
        return jsonify({'error': 'sorry we are having problems try later :('})

@app.route('/top-5', methods=['POST', 'DELETE', 'GET'])
def top_fighters():
    if request.method == 'GET':
        return jsonify(fighters_list)
    
    data = request.get_json()
    fighter = data.get('fighter')
    if request.method == 'POST':
        if len(fighters_list) > 5:
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