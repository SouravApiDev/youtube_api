from flask import Flask, request, jsonify
from pytube import YouTube
app = Flask(__name__)
@app.route('/')
def home():
    return 'home'
@app.route('/yt', methods = ['POST'])
def youtube():
    if request.method == 'POST':
        yt = YouTube(request.form.get('yo'))
        result = {'Title':yt.streaming_data}
        return jsonify(result)
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')