from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

users = {}
LIMIT = 5
top_fighters = []

@app.route('/')
@app.route('/apex.com')
def apex():
    return "<h1> LOG IN </h1> <h4> SIGN IN </h4>"

@app.route('/login', methods=["POST"])
def log_in():
    data = requests.get_json()
    email = data.get("email")

@app.route('/signup', methods=['POST'])
def sign_up():
    data = requests.get_json()
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not name or not email or not password:
        return jsonify({"error": "name,email,password are required"}), 400

    if email in users:
        return jsonify({"message": "email is already registerd"}), 409

    users[email] = password
    return jsonify({"message": "user created welcome"}), 201

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
        return (fights)
    except requests.ecceptions.RequestException:
        return jsonify({'error': 'sorry we are having problems try later'})

@app.route('/fighter/<fighter>')
def fighters(fighter):
    try:
        response = requests.get('http://127.0.0.1:5001/fighters')
        data = response.json()
        for fighter in data:
            if fighter in data:
                return jsonify({'division': data['division'], 'name': data['name']})
            else:
                return jsonify({'message': 'couldnt find the fighter'})
    except requests.exceptions.RequestException:
        return jsonify({'error': 'sorry we are having problems try later'})

@app.route('/settings')
def settings():
    return ''

@app.route('/top_fighters', methods=['POST', 'DELETE', 'GET'])
def top_5():
    data = request.get_json()
    fighters_5 = data.get("fighters_5")

    if request.method == 'POST':
        if len(fighters_5) >= LIMIT:
            return jsonify({'message': 'you cannot enter more than 5 fighters'}), 400
        top_fighters.append(fighters_5)
        return jsonify({'message': 'fighter added'})
    
    if request.method == 'DELETE':
        if top_fighters not in fighters_5:
            return jsonify({'error': 'fighter not in your list'}), 404
        top_fighters.remove(fighters_5)
        return jsonify({'message': 'fighter removed'})
    
    if request.method == 'GET':
        return jsonify(top_fighters)


if __name__ == '__main__':
    app.run(debug=True)