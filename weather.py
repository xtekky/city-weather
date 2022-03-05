from selenium.webdriver.common.keys import Keys as k
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

Options = Options()
Options.headless = True
driver = webdriver.Chrome(options=Options, executable_path="C:\Program Files (x86)\chromedriver.exe")

driver.get("https://google.com/")
wait = WebDriverWait(driver, 20)

def process():
    global temperature
    global precipitation
    global wind
    global humidity
    global time
    global forecast

    #accepting google cookies and selecting language
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME,'V5OCtd'))).click()
    if language == 'en':
        wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="tbTubd"]/div/li[13]'))).click()
    if language == 'fr':
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="tbTubd"]/div/li[18]'))).click()
    if language == 'de':
        wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="tbTubd"]/div/li[9]'))).click()

    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="L2AGLb"]/div'))).click()

    #searching for weather
    wait.until(EC.visibility_of_element_located((By.NAME, 'q'))).send_keys(city, ' weather'+k.RETURN)

    #scraping weather data and assigning to variables
    temperature = wait.until(EC.visibility_of_element_located((By.ID, 'wob_tm'))).text
    wind = wait.until(EC.visibility_of_element_located((By.ID, 'wob_ws'))).text
    precipitation = wait.until(EC.visibility_of_element_located((By.ID, 'wob_pp'))).text
    humidity = wait.until(EC.visibility_of_element_located((By.ID, 'wob_hm'))).text
    time = wait.until(EC.visibility_of_element_located((By.ID, 'wob_dts'))).text
    forecast = wait.until(EC.visibility_of_element_located((By.ID, 'wob_dc'))).text


def info():

    #printing weather info
    print('Date: ', time)
    print('Forecast: ', forecast)
    print('Temperature: ',temperature,'°C')
    print('Wind: ',wind)
    print('Precipitation: ', precipitation)
    print('Humidity: ', humidity)

#city and language input
city = input('City: ')
language = input('Language [en,fr,de]: ')
if language != 'fr':
    if language != 'de':
         if language !='en':
            print('Language not supported')
            exit()
process()
info()

#leave driver
driver.quit()
