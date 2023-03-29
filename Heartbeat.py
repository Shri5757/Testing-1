# Importing the required libraries
import json
import time
import selenium.webdriver as webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.support.ui import Select

serv = Service('C:\\Users\\shrik\\Desktop\\driver\\chromedriver.exe')
options = Options()
options.add_experimental_option('detach',True)
driver = webdriver.Chrome(options=options,service=serv)
url_to_monitor = r'https://saucelabs.com/'
    
def get_status_code(url):
    driver.get(url)
    driver.maximize_window()
    r = requests.get(url)
    title = driver.title
    return (r.status_code,title)

print('Status Code: ',get_status_code(url_to_monitor))

def login():
    time.sleep(5)
    driver.find_element('xpath',"//button [@class ='MuiButtonBase-root MuiButton-root MuiButton-text MuiButton-textDark MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-disableElevation MuiButton-root MuiButton-text MuiButton-textDark MuiButton-sizeMedium MuiButton-textSizeMedium MuiButton-disableElevation css-zaj0tr' ]").click()
    time.sleep(10)
    driver.switch_to.window(driver.window_handles[1])
    user_id = 'oauth-shri.dhumal5757-77343'
    pwd = 'Shri@5757'
    driver.find_element('xpath',"//input [@id = 'idToken1']").send_keys(user_id)
    driver.find_element('xpath',"//input [@id = 'idToken2']").send_keys(pwd)
    driver.find_element('xpath',"//input [@value='Log in']").click()
    time.sleep(30)
    elements =(driver.find_elements('xpath', "//span [@class='overflow-ellipsis Typography__body__im0nl font-sans']"))
    success = False
    for ele in elements:
        if user_id in ele.text:
            success = True
            break
    if success == True:
        return ' log in success'
    else:
        return 'not success'

print(login())

def test_case():
    driver.find_element('xpath',"//div [@class  = 'font-semibold whitespace-nowrap Typography__body__im0nl font-sans' and text()='Insights'] ").click()
    time.sleep(1)
    driver.find_element('xpath', "//div[@class='Typography__body__im0nl font-sans' and text()='Test History']").click()
    # driver.save_screenshot()
    time.sleep(3)
    lst1 = driver.find_elements(By.XPATH,"//p[@class='Statistics__text__l6mn0']")
    lst2 = driver.find_elements(By.XPATH,"//h4 [@class = 'Statistics__label__CFuZQ flex content-center items-center']")
    op = {}
    for i in range(1,3):
        op[lst2[i].text]=(lst1[i].text)
        time.sleep(2)
    driver.save_screenshot('ss.png')
    return (op)

result = test_case()
time.sleep(2)

def log_out():
    elements = driver.find_elements(By.XPATH,"//button [@class='min-w-7 group px-2 relative justify-center flex flex-row items-center no-underline hover:no-underline outline-none focus:outline-none ring-0 bg-transparent border-none w-full appearance-none text-medium-emphasis cursor-pointer hover:bg-gray-50 active:bg-sds-primary-10']")
    for i in range(6):
        if i == 4:
            elements[i].click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//button [@class='flex items-center px-2 py-0.75 outline-none focus:outline-none ring-0 w-full text-left hover:no-underline cursor-pointer active:font-semibold border-none bg-white hover:bg-gray-50 text-high-emphasis active:bg-sds-primary-10']").click()


log_out()

def output(result):
    opt = json.dumps(result)
    return opt

final_op = output(result)
print(final_op)
