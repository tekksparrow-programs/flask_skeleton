from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World! This is the EASY API APP</p>"

if __name__ == '__main__':
    app.run(host="localhost", port=12031, debug=True)