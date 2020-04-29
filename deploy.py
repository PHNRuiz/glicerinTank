from flask import Flask, request

app = Flask(__name__)

volume = 0

@app.route('/glicerina', methods=['POST'])
def postVolume():
    data = request.get_json(force=True)

    global volume
    volume += (data['glicerina']) #confirmar como thomas vai mandar a glicerina

    return 200


@app.route('/glicerina', methods=['GET'])
def getVolume():
    global volume
    response = {
        'glicerina': volume
    }
    return response






def create_app():
    global app

    return app

def create_App():
    global app

    app.run()