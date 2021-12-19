from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager
import time

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get('https://blackboard.syracuse.edu/auth-saml/saml/login?apId=_187_1&redirectUrl=https%3A%2F%2Fblackboard.syracuse.edu/')
time.sleep(3)
button = browser.find_element_by_link_test('SU NetID Login')
button.click()

time.sleep(3)

