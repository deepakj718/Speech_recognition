from flask import Flask, redirect, render_template, url_for, request
import speech_recognition as sr


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/", methods= ['POST'])
def change():
    return redirect(url_for('transcribe'))

@app.route('/transcriber', methods=['GET',"POST"])
def transcribe():
    text = ""
    if request.method == 'POST':
        print("DATA RECIEVED")

        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]

        if file.filename == "":
            return redirect(request.url)
        
        if file:
            recognize_file = sr.Recognizer()
            audio_file = sr.AudioFile(file)
            with audio_file as source:
                file_data = recognize_file.record(source)
            text = recognize_file.recognize_google(file_data,key=None)

    return render_template('transcriber.html', text = text)


if __name__ == "__main__":
    app.run(debug=True, threaded = True)

