from flask import Flask


def make_bold(function):
    def wrap_bold():
        return "<b>" + function() + "</b>"

    return wrap_bold


def make_emphasis(function):
    def emphasis_wrap():
        return f"<em>{function()}</em>"

    return emphasis_wrap


def make_underlined(function):
    def underline_wrap():
        return f"<u>{function()}</u>"

    return underline_wrap


# Type 'set FLASK_APP=hello.py' for your flask project to work.
# Type 'flask run' to deploy your flask web server.
# To close your web server press "CTRL + C"
# __name__ can be used to find out the current class, function, method, descriptor, or generator instance.
app = Flask(__name__)


# Display the homepage when the user arrives at "/".
# hello_world() function will only be called if user is trying to access the url "/" i.e., homepage
# Here @app.route("/") is a decorator
# Here route() is the decorator function of app object declared in the Flask class.
# hello_world() function can not only return strings but also HTML elements.
@app.route("/")
def hello_world():
    # Adding inline CSS using the style attribute in the h1 element. Here, style is a global attribute.
    # To add additional HTML elements simply append the HTML element at the end of the previous element.
    return ("<h1 style='text-align: center'>Hello, World!</h1>"
            "<p>This is a paragraph.</p>"
            "<img align='center' src='https://media4.giphy.com/media/MeJgB3yMMwIaHmKD4z/giphy.gif?cid"
            "=ecf05e47e1bsuaw3p34lw3yovjhd9wj9dqplbpijct1o1c5t&ep=v1_gifs_search&rid=giphy.gif&ct=g', width='500px'/>")


@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def say_bye():
    return "Bye!"


# You can add variable sections to a URL by marking sections with <variable_name>
# Go to http://127.0.0.1:5000/username/Meowya to pass 'Meowya' as a keyword argument to the greet() function.
# Creating variable paths and converting to a specified data type.
# Arguments like <converter:variable_name> can be used to specify the type of the arguments.
@app.route("/<name>/<int:number>")
def greet(name, number):
    return f"Hello, {name}! You're {number} years old."


# To run hello.py from the current file.
# This portion of the code inside the if block will only run if hello.py is run directly.
# If hello.py is run directly then __name__ will be equal to __main__.
# If you import a module say random. Then print(random.__name__) will print 'random' on the console.
if __name__ == "__main__":
    # app.run() does the same operation as typing 'flask run'.
    # To run the app in debug mode change the debug parameter to True in the run() function.
    # Debug mode allows us to no longer stop and restart the server everytime we make changes.
    app.run(debug=True)
