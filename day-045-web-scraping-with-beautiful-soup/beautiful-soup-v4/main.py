from bs4 import BeautifulSoup

# Some websites might not work with an HTML parser. So instead we use lxml
# import lxml

# Set the encoding argument to 'utf8' to prevent the UnicodeDecodeError.
with open("website.html", encoding='utf8') as website:
    contents = website.read()

# Create an object of BeautifulSoup class.
# If the website doesn't support "html.parser" then use "lxml.parser" instead.
soup = BeautifulSoup(contents, "html.parser")

# To get the data from a certain HTML element, for example title element.
# print(soup.title)

# To get the name of the title element.
# print(soup.title.name)

# To get the content of the title element.
# print(soup.title.string)

# To prettify your html code.
# print(soup.prettify())

# To get all data of a particular element.
all_anchor = soup.find_all(name="a")
# print(all_anchor)

# for anchor in all_anchor:
    # print(anchor.string)
    # OR
    # print(anchor.get_text())
    # To get the data from a particular attribute use the get() method.
    # print(anchor.get("href"))

# To get an element using a particular attribute.
# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

# In a scenario where there are thousands of elements of the same type.
# It becomes exceeding important to narrow down what element we want.
# This can be done using CSS Selectors.
# company_url = soup.select_one(selector="p a")
# print(company_url.get("href"))

# Similarly you can use the ID selectors to fetch elements.
name = soup.select_one(selector="#name")
print(name)

# Similarly you can select elements using the Class selectors.
all_heading = soup.select(selector=".heading")
print(all_heading)
