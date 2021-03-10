from flask import Flask, render_template
import os


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    images = os.listdir('./static/pictures')
    return render_template('index.html', images=images)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/image/<string:image>')
def picture(image):
    return render_template('picture.html', title=image[:-4], image=image)

if __name__ == '__main__':
    app.run('0.0.0.0')
