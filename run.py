from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Ajay Shukla',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Amit Shukla',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 10, 2019'
    }
]

@app.route("/")
@app.route("/home")
def hellow():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", posts=posts, title='About')


if __name__ == "__main__":
    app.run(host ='0.0.0.0', port = 5000, debug = True)
