from flask import Flask, render_template, url_for
app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug = True)