from flask import Flask, request
from flask import render_template, send_file
import io

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return render_template('main.html')


@app.route('/image_upload/', methods=['GET', 'POST'])
def image_upload():
    if request.method == 'POST':
        f = request.files['image']
        return send_file(filename_or_fp=io.BytesIO(f.read()), attachment_filename=f.filename)

if __name__ == '__main__':
    app.debug = True
    app.run()
    # app.run(host='0.0.0.0')
