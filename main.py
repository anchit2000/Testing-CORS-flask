import flask
import json
from flask_cors import CORS , cross_origin

app = flask.Flask(__name__)

CORS(app)

@app.route("/api")
# @cross_origin()  # this is optional if only want to make one function accessible
def resp():
    return json.dumps({
        'test': 'testing the script'
    })

if __name__ == '__main__':
    app.run()

