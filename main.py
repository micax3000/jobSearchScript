from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pprint import pprint

options = Options()
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = options)
ads = []
driver.get("https://www.joberty.rs/IT-poslovi?page=1&pageSize=100&seniority=Internship,Junior&sort=created")
premiumAds = driver.find_elements("css selector", 'div.compact-job')
commonAds = driver.find_elements("css selector", "div.mb-20")
for premiumAd in premiumAds:
    adInfo = premiumAd.find_element("xpath", "div/div[2]/div")
    jobTitle = adInfo.find_element("xpath", "*/a")
    jobProvider = adInfo.find_element("xpath", "a")
    jobLocation = adInfo.find_element("xpath", "span/*/span[@class = 'black-link']")
    ads.append([jobTitle.get_attribute("innerHTML"),
                jobProvider.get_attribute("innerHTML"),
                jobLocation.get_attribute("innerHTML")])

for commonAd in commonAds:
    adInfo = commonAd.find_element("xpath", "div")
    jobTitle = adInfo.find_element("xpath", "div/div/*/a")
    jobProvider = adInfo.find_element("xpath", "div[2]/*/a")
    jobLocation = adInfo.find_element("xpath", "div[2]/div/span/*/span[@class = 'black-link']")
    ads.append([jobTitle.get_attribute("innerHTML"),
                jobProvider.get_attribute("innerHTML"),
                jobLocation.get_attribute("innerHTML")])

print(len(ads))
print("[JOB TITLE, JOB PROVIDER, JOB LOCATION]")
pprint(ads)