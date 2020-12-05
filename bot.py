from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(30)

contacts = ['Bot']
mensagem = 'Oi'

def search_contact(contacts):
    search_box = driver.find_element_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    time.sleep(5)
    search_box.click()
    search_box.send_keys(contacts)
    time.sleep(3)
    search_box.send_keys(Keys.ENTER)

def send_msg(mensagem):
    search_box_msg = driver.find_elements_by_class_name('_1awRl')
    time.sleep(5)
    search_box_msg.click()
    search_box_msg.send_keys(mensagem)
    search_box_msg.send_keys(Keys.ENTER)

for contact in contacts:
    search_contact(contacts)
    send_msg(mensagem)