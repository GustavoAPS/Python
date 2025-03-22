from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = r"C:\Users\Gustavo Afonso\Desktop\ChromeDriver\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://elgoog.im/t-rex/")
canvas = driver.find_elements_by_class_name("runner-canvas")

run_game = True
time.sleep(5)

while run_game:
    time.sleep(1)
    canvas.send_keys("webdriver" + Keys.ARROW_UP)
