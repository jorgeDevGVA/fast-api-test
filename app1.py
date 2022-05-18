from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from PIL import Image
import requests
from gtts import gTTS
from playsound import playsound


ALLOWED_EXTENSIONS = set(['txt','pdf','png','jpg','jpeg','gif'])
UPLOAD_FOLDER = 'images'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route("/")
def home():
    return render_template('home.html')


@app.route('/uploader', methods = ['post', ])
def upload_file():
    if request.method == 'POST' and request.files:
        f = {'file': request.files['image']}
        try:
            response = requests.post("http://localhost:5050/uploadfile",files = f)
            responseText = response.text
        except Exception as e:
            return render_template('results.html', text=e)
 
        myobj = gTTS(text=responseText,lang='en', slow=False)
        myobj.save(app.config['UPLOAD_FOLDER'] + '/speech.mp3')
        playsound(app.config['UPLOAD_FOLDER'] + '/speech.mp3')

        return render_template('results.html', text=responseText)   
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug = True)