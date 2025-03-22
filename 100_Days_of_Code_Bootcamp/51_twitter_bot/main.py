from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


chrome_driver_path = r"Your chrome driver path"
TWITTER_LOGIN_URL = "https://twitter.com/i/flow/login"
user_name = "Your twitter login"
password = "Your twitter password"


driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get(TWITTER_LOGIN_URL)

time.sleep(10)
username_text_box = driver.find_element_by_name("username")
username_text_box.send_keys(user_name)
time.sleep(3)
username_text_box.send_keys(Keys.ENTER)

time.sleep(5)
password_text_box = driver.find_element_by_name("password")
password_text_box.send_keys(password)
time.sleep(3)
password_text_box.send_keys(Keys.ENTER)

time.sleep(5)
tweet_text_box = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
tweet_text_box.send_keys("I live.")
time.sleep(3)
tweet_text_box.send_keys(Keys.ENTER)
time.sleep(2)
tweet_button = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
tweet_button.click()
