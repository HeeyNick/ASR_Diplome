from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/upload', methods=['POST'])
@cross_origin()
def upload():
    audio_file = request.files['file']
    audio_file.save('./saved/file.wav')
    return 'successfulli'

if __name__ == "__main__":
  app.run(port=5500, debug=True)
