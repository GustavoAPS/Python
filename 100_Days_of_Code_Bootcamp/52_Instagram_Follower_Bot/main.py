from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# constants
chrome_driver_path = r"C:\Users\Gustavo Afonso\Desktop\ChromeDriver\chromedriver.exe"
INSTAGRAM_LOGIN_URL = ""
SIMILAR_ACCOUNT = ""
USERNAME = ""
PASSWORD = ""
PEOPLE_FOLLOWED_DAY_LIMIT = 500
FOLLOW_PERSON_COOLDOWN = 10


def wait_for_seconds(seconds: int):
    time.sleep(seconds)
    return


# variable assignment
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get(INSTAGRAM_LOGIN_URL)

# wait page to load
wait_for_seconds(5)

username_input = driver.find_element_by_name("username")
password_input = driver.find_element_by_name("password")
button = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
wait_for_seconds(5)

username_input.send_keys(USERNAME)
wait_for_seconds(2)
password_input.send_keys(PASSWORD)
wait_for_seconds(2)
button.click()
wait_for_seconds(5)
search_user_input = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search_user_input.send_keys(SIMILAR_ACCOUNT)
wait_for_seconds(2)
search_user_input.send_keys(Keys.ENTER)
wait_for_seconds(2)

# close the application

driver.close()
# driver.quit()
#instagram allowed politic for automation:
# Follow
# unfollow