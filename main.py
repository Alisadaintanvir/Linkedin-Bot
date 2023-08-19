from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv

load_dotenv()

driver = webdriver.Chrome()
driver.get(url="https://www.linkedin.com/jobs/search/?currentJobId=3689679460&f_LF=f_AL&geoId=102257491&keywords="
               "python%20developer&location=London%2C%20England%2C%20United%20Kingdom")

sign_in = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
sign_in.click()
time.sleep(2)

username = driver.find_element(By.ID, "username")
username.send_keys(os.environ.get("linkedin_email"))
password = driver.find_element(By.ID, "password")
password.send_keys(os.environ.get("linkedin_password"), Keys.ENTER)
time.sleep(5)

time.sleep(5)
apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
apply_button.click()

time.sleep(5)
phone = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
if phone.text == "":
    phone.send_keys("PHONE")

submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
submit_button.click()
driver.quit()
