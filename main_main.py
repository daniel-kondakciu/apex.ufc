from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

users = {}

@app.route('/')
@app.route('/apex.com')
def apex():
    return "<h1> LOG IN </h1> <h4> SIGN IN </h4>"

@app.route('/login', methods=["POST"])
def log_in():
    data = request.get_json()

@app.route('/signup', methods=['POST'])
def sign_up():
    data = request.get_json()
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
    response = request.get(url)
    fights = response.json()
    return (fights)

@app.route('/fighter/<fighter>')
def fighters(fighter):
    url = 'http://127.0.0.1:5001/fighters'
    response = request.get(url)
    fighters = response.json()
    return render_template('fighters.html', fighters=fighters)

@app.route('/settings')
def settings():
    return ''

if __name__ == '__main__':
    app.run(debug=True)