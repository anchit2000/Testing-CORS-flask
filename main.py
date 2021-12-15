import flask
import json
from flask_cors import CORS

app = flask.Flask(__name__)

CORS(app)

@app.route("/api")
def resp():
    return json.dumps({
        'test': 'testing the script'
    })

if __name__ == '__main__':
    app.run()

