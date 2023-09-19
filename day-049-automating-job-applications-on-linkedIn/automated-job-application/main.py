import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# LINKEDIN email and password stored as environment variables.
MY_EMAIL = os.environ["MY_EMAIL"]
MY_PASSWORD = os.environ["MY_PASSWORD"]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option(name="detach", value=True)

chrome_driver = webdriver.Chrome(chrome_options)
chrome_driver.maximize_window()

chrome_driver.get(url="https://www.linkedin.com/jobs/search/?currentJobId=3656983339&f_LF=f_AL&geoId=102257491"
                      "&keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom")

# SIGNIN TO LINKEDIN ACCOUNT
chrome_driver.find_element(By.LINK_TEXT, value="Sign in").click()

chrome_driver.find_element(By.ID, value="username").send_keys(MY_EMAIL)
chrome_driver.find_element(By.ID, value="password").send_keys(MY_PASSWORD)
chrome_driver.find_element(By.CSS_SELECTOR,
                           value="#organic-div > form > div.login__form_action_container > button").click()
time.sleep(15)

# APPLY TO JOBS USING LINKEDIN EASY APPLY FEATURE.
chrome_driver.find_element(By.CSS_SELECTOR, value=".jobs-apply-button--top-card button").click()
chrome_driver.find_element(By.XPATH, value='//*[@id="single-line-text-form-component-formElement-urn-li-jobs'
                                           '-applyformcommon-easyApplyFormElement-3656983339-720017503049330542'
                                           '-phoneNumber-nationalNumber"]').send_keys("1234567890")
chrome_driver.find_elements(By.TAG_NAME, value="button")[1].click()
chrome_driver.find_elements(By.TAG_NAME, value="button")[2].click()
chrome_driver.find_elements(By.TAG_NAME, value="button")[3].click()
chrome_driver.find_elements(By.TAG_NAME, value="button")[2].click()
chrome_driver.find_elements(By.TAG_NAME, value="button")[5].click()
chrome_driver.find_elements(By.TAG_NAME, value="button")[3].click()
chrome_driver.find_elements(By.TAG_NAME, value="button")[9].click()
