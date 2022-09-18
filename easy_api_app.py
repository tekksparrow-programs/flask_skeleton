from flask import Flask, render_template, url_for

app = Flask(__name__)

data = [
    { 
        'username': 'sleepyTurtle',
        'hero': 'Tracer',
        'date_added': 'Fri Sep 16 2022',
        'info': 'won last game with positive k/d ratio'
    },
    {
        'username': 'TekkSparrow',
        'hero': 'Winston',
        'date_added': 'Fri Sep 16 2022',
        'info': 'lost their last 5 games',
    },
    {
        'username': 'zing-ding',
        'hero': 'Widow',
        'date_added': 'Fri Sep 16 2022',
        'info': 'no games played last 90 days'
    }
]

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html', data=data, title='Home')

@app.route("/about")
def about_page():
    return render_template('about.html', data=data, title='About')

@app.route("/login")
def login_page():
    return render_template('login.html', data=data, title='Login')

@app.route("/register")
def register_page():
    return render_template('register.html', data=data, title='Register')

if __name__ == '__main__':
    app.run(host="localhost", port=12031, debug=True)