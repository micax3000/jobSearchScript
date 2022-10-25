from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = options)

driver.get("https://www.joberty.rs/IT-poslovi?page=1&pageSize=100&seniority=Internship,Junior&sort=created")
contents = driver.find_elements("css selector", 'div.compact-job')
contents.extend(driver.find_elements("css selector","div.mb-20"))
print(len(contents),[content.get_attribute('innerHTML') for content in contents])