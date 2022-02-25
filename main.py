#The following program has been edited for the sake of increasing complexity at (6:26pm)

from selenium.webdriver.support import expected_conditions as c
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from creds import name
from creds import passwd, link1
import time
import datetime

signin = (By.XPATH, '//*[@id="office-HeroPhotographic-6j70rzy"]/div/div[3]/section/div/div[2]/div[1]/a')
email = (By.ID, "i0116")
password = (By.ID, "i0118")
nextbutton = (By.ID, "idSIButton9")
joinbutton = (By.XPATH, '//*[@id="m1644641672692"]/calling-join-button/button/span')
e=datetime.datetime.now()

L=eval(input("Enter time as [hr, min, sec]: "))
hr_rep=L[0]; min_rep=L[1]; sec_rep=L[2];
st = {'hr': hr_rep, 'min': min_rep, 'sec': sec_rep}  #Meeting time as given by user
h=e.hour; m=e.minute; s=e.second
t_h=st['hr']-h; t_m=st['min']-m; t_s=st['sec']-s
wait=(t_h*3600)+(t_m*60)+t_s
if(wait<0):
    print("Too late bud...")
    quit()
duration=int(input("Enter Duration (min): "))
duration=duration*60

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
time.sleep(wait)
browser.get(link1)
time.sleep(8)

video_btn = browser.find_element(by=By.CSS_SELECTOR, value="toggle-button[data-tid='toggle-video']>div>button")
video_is_on = video_btn.get_attribute("aria-pressed")
if video_is_on == "true":
    WebDriverWait(browser, 10).until(c.element_to_be_clickable(video_btn)).click()
    print("Video disabled")
audio_btn = browser.find_element(by=By.CSS_SELECTOR, value="toggle-button[data-tid='toggle-mute']>div>button")
audio_is_on = audio_btn.get_attribute("aria-pressed")
if audio_is_on == "true":
    WebDriverWait(browser, 10).until(c.element_to_be_clickable(audio_btn)).click()
    print("Microphone off")
    
WebDriverWait(browser, 10).until(c.element_to_be_clickable(joinbutton)).click()
browser.find_element(by=By.XPATH, value='//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div/button')
time.sleep(duration)
browser.find_element(by=By.CSS_SELECTOR, value="button[data-tid='call-hangup']").click()
