from flask import Flask, jsonify

app = Flask(__name__)

ufc_fighters = [
    {
        
    }
]

@app.get('/fighters')
def fighters():
    return jsonify (ufc_fighters)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001,debug=True)