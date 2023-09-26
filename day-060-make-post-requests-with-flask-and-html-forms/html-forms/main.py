from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


# Create decorator that will trigger a method when it receives a POST request.
@app.route("/login", methods=["POST", "GET"])
def receive_data():
    # The Request object allows you to interact with the data that you send during your POST request.
    # The method attribute provides what kind of HTTP request has been made by the form on clicking the submit button.
    # The request.form['<name-attribute-of-input-element>'] can be used to access data from each input element.
    if request.method == 'POST':
        return render_template("login.html", username=request.form['username'], password=request.form['password'])


if __name__ == "__main__":
    app.run(debug=True)
