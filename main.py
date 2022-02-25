from selenium.webdriver.support import expected_conditions as c
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from creds import name
from creds import passwd, link1
import time
#name, password, and link1(meeting id) have been put in 'creds' for confidentiality
signin = (By.XPATH, '//*[@id="office-HeroPhotographic-6j70rzy"]/div/div[3]/section/div/div[2]/div[1]/a')
email = (By.ID, "i0116")
password = (By.ID, "i0118")
nextbutton = (By.ID, "idSIButton9")
joinbutton = (By.XPATH, '//*[@id="m1644641672692"]/calling-join-button/button/span')

browser = webdriver.Chrome(r"C:\Users\ashri\PycharmProjects\SeleniumTest\Browsers\chromedriver.exe")
browser.get('https://www.microsoft.com/en-in/microsoft-teams/log-in')
WebDriverWait(browser, 10).until(c.element_to_be_clickable(signin)).click()

browser.switch_to.window(browser.window_handles[1])
browser.maximize_window()
time.sleep(5)
WebDriverWait(browser, 10).until(c.element_to_be_clickable(email)).send_keys(name)
WebDriverWait(browser, 10).until(c.element_to_be_clickable(nextbutton)).click()
WebDriverWait(browser, 10).until(c.element_to_be_clickable(password)).send_keys(passwd)
WebDriverWait(browser, 10).until(c.element_to_be_clickable(nextbutton)).click()

time.sleep(4)
browser.find_element(by=By.XPATH, value='//*[@id="idBtn_Back"]').click()
time.sleep(10)
browser.get('https://teams.microsoft.com/_?culture=en-in&country=IN&lm=deeplink&lmsrc=homePageWeb&cmpid=WebSignIn#/calendarv2')
browser.get(link1)
WebDriverWait(browser, 10).until(c.element_to_be_clickable(joinbutton)).click()
browser.find_element(by=By.XPATH, value='//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button')
