from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pprint import pprint

options = Options()
driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), options = options)
ads = []
driver.get("https://www.joberty.rs/IT-poslovi?page=1&pageSize=100&seniority=Internship,Junior&sort=created")


def find_element_xpath(driver, query: str):
    return driver.find_element("xpath", query)


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

#h4[@class = "font-semibold opacity-75"]
driver.get("https://www.helloworld.rs/prakse")
helloWorldJobProviders = driver.find_elements("xpath", "//h4[@class = 'font-semibold opacity-75']/a")
helloWorldJobTitles = driver.find_elements("xpath", "//a[@class = 'hover:opacity-50 font-bold text-lg']")
zippedArrays = zip(helloWorldJobTitles,helloWorldJobProviders)
ads.extend([[ad[0].get_attribute("innerHTML").split("\n")[0],ad[1].get_attribute("innerHTML")]
            for ad in zippedArrays])
driver.close()
print(len(ads))
print("[JOB TITLE, JOB PROVIDER, JOB LOCATION]")
pprint(ads)