from flask import Flask,redirect,url_for
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'
@app.route('/home')
def hello_home():
    return "<h2> Hello from homepage </h2>"

if __name__ == '__main__':
    app.run(debug=True)