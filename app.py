from flask import Flask,render_template, url_for, flash, redirect, request
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