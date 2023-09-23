from flask import Flask, render_template

site_app = Flask(__name__)


@site_app.route("/")
def personal_site():
    return render_template("index.html")


if __name__ == "__main__":
    site_app.run(debug=True)