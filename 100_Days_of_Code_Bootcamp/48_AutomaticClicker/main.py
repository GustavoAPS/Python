from selenium import webdriver
import time

# use your chrome diver .exe path
chrome_driver_path = r""


driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")

run_game = True

while run_game:
    cookie.click()
    time.sleep(0.001)
