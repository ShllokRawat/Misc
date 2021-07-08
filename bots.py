from selenium import webdriver
driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://www.google.com")
searchbox = driver.find_element_by_name("q")
search = drover.find_element_by_name("btnK")
searchbox.send_keys("bing")
search.submit()
