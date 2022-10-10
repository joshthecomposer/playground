from distutils.log import debug
from flask import Flask, render_template
app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('play.html', num = 3, color = 'blue')

@app.route('/')
def index():
    return render_template('play.html', num = 3, _color = 'blue')

@app.route('/play')
def default():
    return render_template('play.html', num = 3, _color = 'blue')

@app.route('/play/<int:num>')
def play(num):
    return render_template('play.html', num= num, _color= 'blue')

@app.route('/play/<int:num>/<string:_color>')
def play2(num, _color):
    return render_template('play.html', num= num, _color= _color)

if __name__ == '__main__':
    app.run(debug=True)
