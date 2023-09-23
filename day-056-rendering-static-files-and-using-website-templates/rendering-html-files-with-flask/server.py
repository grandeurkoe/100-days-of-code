from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    # Use the render_template function to render HTML files in your flask apps.
    # All website templates must be store inside the templates' folder.
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
