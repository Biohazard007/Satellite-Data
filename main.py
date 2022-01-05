from flask import Flask, render_template, send_from_directory

app = Flask(__name__,static_folder='./static')

@app.route('/static/<path:path>')
def send_js(path):
    return send_from_directory(path)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/about")
def hello():
    return render_template('example.html')

 

app.run(debug=True)