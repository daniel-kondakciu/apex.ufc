from flask import Flask, jsonify

app = Flask(__name__)

ufc_fights = [
    {
        'fight': '#12 ROSAS JR. VS BARCELOS #13',
        'division': 'BANTAMWEIGHT',
        'event': 'ufc vegas121',
        'card': 'main event'
    },
    {
        'fight': '#4 NORMA DUMONT VS AILIN PEREZ #5',
        'division': 'WOMAN BANTAMWEIGHT',
        'event': 'ufc vegas121',
        'card': 'co-main event'
    },
    {
        'fight': '#NR LUIS HERNANDEZ VS SEDRIQUES DUMAS #NR',
        'division': 'LIGHT HEAVYWEIGHT',
        'event': 'ufc vegas121'
    },
    {
        'fight': '#NR MAHAMMADALI OSMANLI VS ILIMBEK AKYLBEK #NR',
        'division': 'BANTAMWEIGHT',
        'event': 'ufc vegas121'
    },
    {
        'fight': '#NR MELISSA AMAYA VS TINA BLACK #NR',
        'division': 'WOMAN STRAWWEIGHT',
        'event': 'ufc vegas121'
    },
    {
        'fight': '#NR BRADY HIESTAND VS RINYA NAKAMURA #NR',
        'division': 'BANTAMWEIGHT',
        'event': 'ufc vegas121'
    },
    {
        'fight': '#NR RODOLFO VIEIRA VS ROBERT BRYCZEK #NR',
        'division': 'MIDDLEWEIGHT',
        'event': 'ufc vegas121'
    },
    {
        'fight': '#NR RODOLFO BELLATO VS CHRISTIAN EDWARDS #NR',
        'division': 'LIGHT HEAVYWEIGHT',
        'event': 'ufc vegas121'
    },
    {
        'fight': '#NR ELVES BRENER VS JOSIAH HARREL #NR',
        'division': 'LIGHTWEIGHT',
        'event': 'ufc vegas121'
    },
    {
        'fight': '#NR MONTEL JACKSON VS RICKY SIMON #NR',
        'division': 'BANTAMWEIGHT',
        'event': 'ufc vegas121'
    },
    {
        'fight': '#NR JOHN CASTANEDA VS ALATENGHELI #NR',
        'division': 'BANTAMWEIGHT',
        'event': 'ufc vegas121'
    },
    {
        'fight': '#NR VANESSA DEMOPOULOS VS YAZMIN JAUREGUI #NR',
        'division': 'WOMAN STRAWWEIGHT',
        'event': 'ufc vegas121'
    }
]


@app.get('/fights')
def fight():
    return jsonify(ufc_fights)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=3000,debug=True)