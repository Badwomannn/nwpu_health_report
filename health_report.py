import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os

USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
browser = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)

# open nwpu
browser.get('https://uis.nwpu.edu.cn/cas/login?service=https://ecampus.nwpu.edu.cn/')
browser.maximize_window()

# login
username = browser.find_element(By.ID, "username")
username.send_keys(USERNAME)
password = browser.find_element(By.ID, "password")
password.send_keys(PASSWORD)
browser.find_element(By.NAME, "submit").click()
time.sleep(1)

browser.get('https://yqtb.nwpu.edu.cn/wx/xg/yz-mobile/index.jsp')
browser.refresh()
browser.get('https://yqtb.nwpu.edu.cn/wx/ry/jrsb_xs.jsp')
browser.refresh()
time.sleep(1)

browser.find_element(By.LINK_TEXT, "提交填报信息").click() # 提交填报信息
qrxx = browser.find_element(By.CSS_SELECTOR, "#qrxx_div > div.weui-cells.weui-cells_form > div.weui-cells.weui-cells_checkbox > label > div.weui-cell__hd > i") # 核实按钮
hidden_qrxx = browser.find_element(By.CSS_SELECTOR, "#qrxx_div > div.weui-cells.weui-cells_form > div.weui-cells.weui-cells_checkbox > label") # 核实按钮上级
ActionChains(browser).move_to_element(qrxx).click(hidden_qrxx).perform() # 事件链点击
browser.find_element(By.ID, "save_div").click() # 确认提交
time.sleep(1)
    
browser.quit()
