from flask import Flask,render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '8bc5df3b90c6dfb32dcbdfcfb485cb35'

posts = [
    {
         'date':'November 28th',
        'deedt':'I woke up and took a shower'
       
    },
    {
        'date': 'November 27th',
        'deed': 'I made my bed'
    },
    {
        'date': 'November 23th',
        'deed': 'I used my phone'
    }
]

@app.route('/')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/getSomeTLC")
def getSomeTLC():
    return render_template('getSomeTLC.html',posts=posts, title='getSomeTLC')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
    app.run(debug=True)      