from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

options = webdriver.ChromeOptions()
options.binary_location = r"Browser_location"
chromedriver = "chromedriver_location"
driver = webdriver.Chrome(chromedriver,chrome_options=options)
driver.get('https://web.whatsapp.com/')

name = input('Enter Receiver name:')
msg = input('Enter Message:')
wait = WebDriverWait(driver,timeout=900)

#For searching the user 
user = driver.find_elements_by_xpath('//span[@title = "%s"]'%name)
user.click()

#For Enterng Message and Clicking send button
msg_box = driver.find_element_by_class_name('_2S1VP')
msg_box.send_keys(msg)
button = driver.find_element_by_class_name('_35EW6')
button.click()