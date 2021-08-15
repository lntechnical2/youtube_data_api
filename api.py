import flask
from flask import request, jsonify
from pyyoutube import Data 
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Get YouTube Video Data </h1>"


@app.route('/api', methods=['GET'])
def api_id():
    if "link" in request.args:
        id = request.args['link']
    else:
        return "Error: No link field provided"
    yt = Data(id).data
    return jsonify(yt)
        
app.run()
