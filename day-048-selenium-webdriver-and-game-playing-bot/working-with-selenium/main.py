# webdriver will drive the web browser and do our automated tasks.
from selenium import webdriver

# Import the By class to find elements in the webpage.
from selenium.webdriver.common.by import By

# To keep the Chrome browser open after program finishes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)

# webdriver.Chrome() allows selenium package to work with the Google Chrome browser.
chrome_driver = webdriver.Chrome(options=chrome_options)

# The get() function allows you to open a webpage by providing an url.
# chrome_driver.get(url="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1")

# Find elements using class name.
# Add .text to convert html to text format
# product_price_whole = chrome_driver.find_element(By.CLASS_NAME, 'a-price-whole').text
# product_price_decimal = chrome_driver.find_element(By.CLASS_NAME, 'a-price-fraction').text
# print(f"The price is ${product_price_whole}.{product_price_decimal}")

# chrome_driver.get(url="https://docs.python.org/3/index.html")

# python_search_bar = chrome_driver.find_element(By.NAME, value="q")

# To get what tag a particular selenium element.
# print(python_search_bar.tag_name)

# To get the value of a particular attribute.
# print(python_search_bar.get_attribute("placeholder"))

chrome_driver.get(url="https://www.python.org/")

# Find elements using ID.
# python_go_button = chrome_driver.find_element(By.ID, value="submit")
# print(python_go_button.size)

# Find element by CSS Selector.
# pydocs_link = chrome_driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(pydocs_link.text)

# XPath is the method of locating an HTML element by Path structure.
# submit_website_bug = chrome_driver.find_element(By.XPATH, value="/html/body/div/footer/div[2]/div/ul/li[3]/a")
# print(submit_website_bug.text)

# CHALLENGE - Extract Upcoming Events.
events = {}

all_event_dates = chrome_driver.find_elements(By.TAG_NAME,
                                              value="time")
upcoming_event_dates = all_event_dates[5:10:]

all_event_names = chrome_driver.find_elements(By.CSS_SELECTOR,
                                              value=".shrubbery .menu li a")
upcoming_event_names = all_event_names[5:10:]

for event_index in range(len(upcoming_event_dates)):
    each_event = {
        'time': f"2023-{upcoming_event_dates[event_index].text}",
        'name': upcoming_event_names[event_index].text
    }
    events[event_index] = each_event

print(events)
# To close a tab from the Chrome browser.
chrome_driver.close()

# To close the Chrome browser including all tabs.
chrome_driver.quit()
