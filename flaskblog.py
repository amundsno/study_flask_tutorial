from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config["SECRET_KEY"] = "3c7fa6a162adde35bb329aa27783d0d8" # Acquired using the 'secrets' module >> secrets.token_hex(number_of_bits)

posts = [
    {
        "author": "Some Name",
        "title": "First post title",
        "content": "First post content",
        "date_posted": "5th of July, 2020"
    },
    {
        "author": "Some Name",
        "title": "Second post title",
        "content": "Second post content",
        "date_posted": "6th of July, 2020"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/register")
def register():
    form = RegistrationForm() # Form being sent to the render_template
    return render_template("register.html", title="Register", form=form)

@app.route("/login")
def login():
    form = LoginForm() # Form being sent to the render_template
    return render_template("login.html", title="Login", form=form)

if __name__ == "__main__":
    app.run(debug = True)