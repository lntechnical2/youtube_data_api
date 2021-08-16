from flask import Flask
from flask import request, jsonify
from pyyoutube import Data 
app = Flask(__name__)


@app.route('/')
def home():
    return "<h1>Get YouTube Video Data </h1>"


@app.route('/api')
def api_id():
    if "link" in request.args:
        id = request.args['link']
    else:
        return "Error: No link field provided"
    yt = Data(id).data
    return jsonify(yt)
        
if __name__ == "__main__":
    app.run( debug=True)
