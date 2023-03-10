import datetime
import predict
import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = './static/images_predict/images_predict'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

pred = predict

@app.route('/', methods=['GET', 'POST'])
def broken():
    if request.method == 'POST':
        os.remove('./static/images_predict/images_predict/image.jpg')
        image = request.files['file']
        filename = secure_filename('image.jpg')
        image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        predict = pred.get_predict()
        now = datetime.datetime.now()
        return render_template('index_2.html', predict=predict, now=now)
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('signin.html')




if __name__ == '__main__':
    app.run(debug=True)