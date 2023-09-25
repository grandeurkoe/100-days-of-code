from flask import Flask, render_template
from random import randint
from datetime import datetime
import requests

GENDERIZE_ENDPOINT = ""


def get_api_data(url, param):
    response = requests.get(url=url, params=param)
    response.raise_for_status()
    data = response.json()
    return data


template_app = Flask(__name__)


@template_app.route("/")
def home():
    random_number = randint(1, 10)
    current_year = datetime.today().year
    # You can pass any number of keyword arguments in the render_template() function.
    # You need to provide a name for the arguments that you wish to pass.
    # This name would then be used to reference the argument in the HTML file.
    return render_template("index.html", num=random_number, year=current_year)


@template_app.route("/guess/<name>")
def guess(name):
    # Convert name to titlecase.
    titlecase_name = str(name).title()

    param = {
        "name": f"{str(name)}",
    }

    # Get the gender of 'name' using the Genderize API.
    genderize_data = get_api_data("https://api.genderize.io", param)

    # Get the age of 'name' using the Agify API.
    agify_data = get_api_data("https://api.agify.io", param)

    return render_template("guess.html", some_name=titlecase_name, gender=genderize_data['gender'],
                           age=agify_data['age'])


# <num> got passed as an argument in the blog.html using the url_for() function.
@template_app.route("/blog/<num>")
def get_blog(num):
    print(num)
    # Get blog data using the npoint API.
    blog_response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    blog_response.raise_for_status()
    blog_data = blog_response.json()
    return render_template("blog.html", posts=blog_data)


if __name__ == "__main__":
    template_app.run(debug=True)
