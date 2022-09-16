from flask import Flask, render_template

app = Flask(__name__)

data = [
    { 
        'element': 1,
        'word': 'tuna fish'
    },
    {
        'element': 2,
        'word': 'windy',
    },
    {
        'element': 3,
        'word': 'wonderful'
    }
]

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html', data=data, title='Home Page')

@app.route("/about")
def about_page():
    return render_template('about.html', data=data, title='About Page')

if __name__ == '__main__':
    app.run(host="localhost", port=12031, debug=True)