from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pprint import pprint


def find_element_xpath(driver, query: str):
    return driver.find_element("xpath", query)

options = Options()
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = options)
ads = []
driver.get("https://www.joberty.rs/IT-poslovi?page=1&pageSize=100&seniority=Internship,Junior&sort=created")
premiumAds = driver.find_elements("css selector", 'div.compact-job')
commonAds = driver.find_elements("css selector", "div.mb-20")
for premiumAd in premiumAds:
    adInfo = find_element_xpath(premiumAd, "div/div[2]/div")
    jobTitle = find_element_xpath(adInfo, "*/a")
    jobProvider = find_element_xpath(adInfo, "a")
    jobLocation = find_element_xpath(adInfo, "span/*/span[@class = 'black-link']")
    ads.append([jobTitle.get_attribute("innerHTML"),
                jobProvider.get_attribute("innerHTML"),
                jobLocation.get_attribute("innerHTML")])

for commonAd in commonAds:
    adInfo = find_element_xpath(commonAd,"div")
    jobTitle = find_element_xpath(adInfo, "div/div/*/a")
    jobProvider = find_element_xpath(adInfo, "div[2]/*/a")
    jobLocation = find_element_xpath(adInfo, "div[2]/div/span/*/span[@class = 'black-link']")
    ads.append([jobTitle.get_attribute("innerHTML"),
                jobProvider.get_attribute("innerHTML"),
                jobLocation.get_attribute("innerHTML")])

print(len(ads))
print("[JOB TITLE, JOB PROVIDER, JOB LOCATION]")
pprint(ads)