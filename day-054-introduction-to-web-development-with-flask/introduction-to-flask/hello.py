from flask import Flask

# Type 'set FLASK_APP=hello.py' for your flask project to work.
# Type 'flask run' to deploy your flask web server.
# To close your web server press "CTRL + C"
# __name__ can be used to find out the current class, function, method, descriptor, or generator instance.
app = Flask(__name__)


# Display the homepage when the user arrives at "/".
# hello_world() function will only be called if user is trying to access the url "/" i.e., homepage
# Here @app.route("/") is a decorator function.
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
def say_bye():
    return "Bye"


# To run hello.py from the current file.
# This portion of the code inside the if block will only run if hello.py is run directly.
# If hello.py is run directly then __name__ will be equal to __main__.
# If you import a module say random. Then print(random.__name__) will print 'random' on the console.
if __name__ == "__main__":
    # app.run() does the same operation as typing 'flask run'.
    app.run()
