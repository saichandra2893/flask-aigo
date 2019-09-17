"""
A simple Wipro flask app intialization
"""

import  json

from flask import Flask, request

app = Flask(__name__)
app.debug = True


@app.route('/status', methods=['GET'])
def status_change():
    response = json.dumps({"status":True})
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
