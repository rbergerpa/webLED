import pdb
from flask import Flask, request, json, jsonify
from werkzeug.contrib.fixers import ProxyFix

import gpio

app = Flask(__name__, static_url_path='')

LED_PIN = "gpio13"


@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/led/<int:id>', methods=['PUT'])
def led(id):
    json = request.get_json()
    state = json['state']
    gpio.digitalWrite(LED_PIN, state)
    return jsonify(state=state)

def initLED():
    gpio.pinMode(LED_PIN, gpio.OUTPUT)


# For gunicorn
app.wsgi_app = ProxyFix(app.wsgi_app)

initLED()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
