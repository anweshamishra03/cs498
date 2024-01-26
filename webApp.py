from flask import Flask, request, jsonify

app = Flask(__name__)

seedValue = 0 # declare global var

@app.route('/', methods=['GET'])
def getSeed():
    return str(seedValue)

@app.route('/', methods=['POST'])
def updateSeed():
    global seedValue
    data = request.json
    seedValue = data['num']
    return f"Seed value is {seedValue}", 200


if __name__ == '__main__': #standard debug
    app.run(debug=True, host='0.0.0.0', port=80)


