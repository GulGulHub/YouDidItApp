from datetime import datetime
from flask import Flask,render_template, url_for, flash, redirect, request
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8bc5df3b90c6dfb32dcbdfcfb485cb35'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

app.app_context().push()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    
    def __repr__(self):
        return f"User('{self.username}','{self.email}','{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    def __repr__(self):
        return f"Post('{self.title}','{self.date_posted}')"


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

@app.route('/', methods=['GET', 'POST'])

@app.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == 'Post':
        name = request.form["name"]
        return redirect(url_for('getSomeTLC', name=name))
    return render_template('home.html')

@app.route("/getSomeTLC", methods=['GET', 'POST'])
def getSomeTLC():
    name = request.form.get('name')
    return render_template('getSomeTLC.html',posts=posts, name=name, title='getSomeTLC')

@app.route("/dinoWorld")
def dinoWorld():
    return render_template('dinoWorld.html')    

@app.route("/register", methods=['Get','Post'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'account created for {form.username.data}!', 'success')
        return redirect(url_for('dinoWorld'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['Get','Post'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been loggen in!', 'sucess')
            return redirect(url_for('dinoWorld'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')

    return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
    app.run(debug=True)      