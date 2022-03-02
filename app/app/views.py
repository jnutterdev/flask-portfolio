from app import app
from flask import render_template
from datetime import datetime
from flask import request, redirect
from sassutils.wsgi import SassMiddleware

app.wsgi_app = SassMiddleware(
    app.wsgi_app,
    {
        'app': {
            'sass_path': 'static/sass',
            'css_path': 'static/css',
            'wsgi_path': '/static/css',
            'strip_extension': False
        }
    }
)

@app.route("/")
def index():
    return render_template("public/index.html")

@app.route("/about")
def about():
    return render_template("public/about.html")

@app.template_filter("clean_date")
def clean_date(dt):
    return dt.strftime("%d %b %Y")

@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():

    if request.method == "POST":

        req = request.form

        missing = list()

        for k, v in req.items():
           if v == "":
               missing.append(k)

        if missing:
            feedback = f"Missing fields for {', '.join(missing)}"
            return render_template("public/sign_up.html", feedback=feedback)
        
        return redirect(request.url)

    return render_template("public/sign_up.html")

@app.route("/jinja")
def jinja():
    # Strings
    my_name = "John"

    # Integers
    my_age = 41

    # Lists
    langs = ["Python", "JavaScript", "Bash", "Ruby"]

    # Dictionaries
    friends = {
        "Erika": 42,
        "Cody": 28,
        "Amy": 26,
        "Clarissa": 23,
        "Wendell": 39
    }

    # Tuples
    colors = ("Red", "Blue")

    # Booleans
    cool = True

    # Classes
    class GitRemote:
        def __init__(self, name, description, domain):
            self.name = name
            self.description = description 
            self.domain = domain

        def pull(self):
            return f"Pulling repo '{self.name}'"

        def clone(self, repo):
            return f"Cloning into {repo}"

    my_remote = GitRemote(
        name="Learning Flask",
        description="Learn the Flask web framework for Python",
        domain="https://github.com/Julian-Nash/learning-flask.git"
    )

    # Functions
    def repeat(x, qty=1):
        return x * qty

    date = datetime.utcnow()

    return render_template(
        "public/jinja.html", my_name=my_name, my_age=my_age, langs=langs,
        friends=friends, colors=colors, cool=cool, GitRemote=GitRemote, 
        my_remote=my_remote, repeat=repeat, date=date
    )