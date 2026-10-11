from flask import Flask, jsonify
import json

app = Flask(__name__)

with open("fighters.json", "r", encoding="utf-8") as f:
    fighter = json.load(f)

@app.get('/fighters')
def fighters():
    return jsonify(fighter)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001,debug=True)