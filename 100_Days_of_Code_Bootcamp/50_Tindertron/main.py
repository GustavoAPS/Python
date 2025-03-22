from selenium import webdriver
import time

chrome_driver_path = r"YOUR PATH"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://tinder.com/app/recs")

tindertron_likes = 0

time.sleep(30)
like_button = driver.find_element_by_xpath('//*[@id="q-600306533"]/div/div[1]/div/div/main/div/div[1]/div/div/div[4]/div/div[4]/button')

while tindertron_likes < 99:
    time.sleep(2)
    like_button.click()
    tindertron_likes += 1
