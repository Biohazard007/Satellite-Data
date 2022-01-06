from flask import Flask, render_template, send_from_directory

app = Flask(__name__,static_folder='./static')

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory(path)

@app.route("/")
def signin():
    return render_template('signin.html')

@app.route("/signup")
def signup():
    return render_template('signup.html')


@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/map")
def map():
    return render_template('map.html')

app.run(debug=True)