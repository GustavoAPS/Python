from selenium import webdriver

driver = webdriver.Chrome(r"C:\Users\Gustavo Afonso\Desktop\ChromeDriver\chromedriver.exe")
driver.get("https://en.wikipedia.org/wiki/Main_Page")

number_of_articles = driver.find_element_by_css_selector("#articlecount a")
print(number_of_articles.text)
