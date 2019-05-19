from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'b4c40a3458d86a6d6065cca186ef5fe3'

posts = [
  {
    'author': 'Corey Schafer',
    'title': 'Blog posts 1',
    'content': 'First post content',
    'date_posted': 'April 20, 2018'
  },
  {
    'author': 'Bob Sagat',
    'title': 'Blog posts 3',
    'content': 'Second post content',
    'date_posted': 'April 30, 2018'
  }
]

@app.route("/")
def hello():
    return render_template('home.html', posts = posts)

@app.route("/home")
def home():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
      flash(f'Account creaed form {form.username.data}!', 'success')
      return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
  app.run(debug=True)