from flask import Flask, jsonify
import json

app = Flask(__name__)

with open("event.json", "r", encoding="utf-8") as f:
    event = json.load(f)


@app.get('/fights')
def fight():
    return jsonify(event)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=3000)