from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

users = {}
LIMIT = 5
fighters = []

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
    url = 'http://127.0.0.1:3000/fights'
    response = requests.get(url)
    fights = response.json()
    return (fights)

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

@app.route('/top-fighters', methods=['POST', 'DELETE', 'GET'])
def top_5():
    data = request.get_json()
    fighter = data("fighter")

    if request.method == 'POST':
        if len(fighters) >= LIMIT:
            return jsonify({'message': 'you cannot enter more than 5 fighters'}), 400
    fighters.append(fighter)
    return jsonify({'message': 'fighter added'})
    
    if request.method == 'DELETE':
        if fighter not in fighters:
            return jsonify({'error': 'fighter not in your list'}), 404
        fighters.remove(fighter)
        return jsonify({'message': 'fighter removed'})
    
    if request.method == 'GET':
        return jsonify(fighters)


if __name__ == '__main__':
    app.run(debug=True)