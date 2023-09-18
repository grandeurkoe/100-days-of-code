import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)

chrome_driver = webdriver.Chrome(chrome_options)
chrome_driver.maximize_window()
# chrome_driver.get(url="https://en.wikipedia.org/wiki/Main_Page")

# wikipedia_article_count = chrome_driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# print(wikipedia_article_count.text)

# To click on a link.
# wikipedia_article_count.click()

# To click on a link using link text.
# content_portals = chrome_driver.find_element(By.LINK_TEXT, value="Content portals")
# content_portals.click()

# To type in a search bar and Click ENTER.
# wikipedia_search = chrome_driver.find_element(By.NAME, value="search")
# wikipedia_search.send_keys("Python")
# wikipedia_search.send_keys(Keys.ENTER)

chrome_driver.get(url="https://secure-retreat-92358.herokuapp.com/")
first_name = chrome_driver.find_element(By.NAME, value="fName")
last_name = chrome_driver.find_element(By.NAME, value="lName")
my_email = chrome_driver.find_element(By.NAME, value="email")
first_name.send_keys("Me")
last_name.send_keys("Meowya")
my_email.send_keys("me.meowya@gmail.com")
my_email.send_keys(Keys.ENTER)


# chrome_driver.quit()

