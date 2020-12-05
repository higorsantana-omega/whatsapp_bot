from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(10)

contacts = ['Bot']
mensagem = 'Oi'

def search_contact(contacts):
    search_box = driver.find_element_by_xpath('//div[contains(@class, "copyable-text selectable-text")]')
    time.sleep(5)
    search_box.click()
    search_box.send_keys(contacts)

for contact in contacts:
    search_contact(contacts)