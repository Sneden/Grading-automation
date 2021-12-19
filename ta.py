
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import random

feedback = ["Overall Good Job!", "Overall Well done!", "Overall Nice Work!", "Overall Great Work!"]

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.maximize_window()
browser.get('https://blackboard.syracuse.edu/auth-saml/saml/login?apId=_187_1&redirectUrl=https%3A%2F%2Fblackboard.syracuse.edu/')
time.sleep(1)

input1 = browser.find_element_by_id("username")
input1.send_keys('<username>')

input2 = browser.find_element_by_id("password")
input2.send_keys('<password>')
enter_button = browser.find_element_by_name("_eventId_proceed")
enter_button.click()

browser.get('https://blackboard.syracuse.edu/ultra/course/')
time.sleep(3)

course_button = browser.find_element_by_id("course-link-_454400_1")
course_button.click()
time.sleep(2)

browser.get("https://blackboard.syracuse.edu/webapps/gradebook/do/instructor/viewNeedsGrading?course_id=_454400_1")  

course_buttonexp = browser.find_element_by_id("categoryFilter")
course_buttonexp.click()

filter = browser.find_element_by_xpath("//*[@id='categoryFilter']/option[2]")
filter.click()

go = browser.find_element_by_xpath("//*[@id='filterForm']/fieldset/ul/li[5]/input")
go.click()
time.sleep(2)

start = browser.find_element_by_xpath("//*[@id='listContainer_itemcount']/span/strong[1]").text
last = browser.find_element_by_xpath("//*[@id='listContainer_itemcount']/span/strong[2]").text
time.sleep(2)

c_start = int(start)
c_last = int(last)

section = browser.find_element_by_xpath("//*[@id='listContainer_row:0']/th/a") 
section.click()
time.sleep(2)

for x in range(c_start,c_last+1):
    arrow = browser.find_element_by_id("currentAttempt_gradeDataPanelLink")
    arrow.click()
    time.sleep(2)
    rubric = browser.find_element_by_xpath("//*[@id='collabRubricList']/div/h4/a")
    rubric.click()
    time.sleep(2)
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    one = browser.find_element_by_xpath("//*[@id='cell__514982_1']")
    one.click()
    two = browser.find_element_by_xpath("//*[@id='cell__514984_1']")
    two.click()
    three = browser.find_element_by_xpath("//*[@id='cell__514986_1']")
    three.click()
    four = browser.find_element_by_xpath("//*[@id='cell__514988_1']")
    four.click()
    time.sleep(2) 
    save_rubric = browser.find_element_by_xpath("//*[@id='currentAttempt_inlineRubric']/div[6]/a[2]")
    save_rubric.click()
    time.sleep(2)
    browser.switch_to.frame(browser.find_element_by_id("feedbacktext_ifr"))
    choose = random.choice(feedback)
    input_f = browser.find_element_by_xpath("//*[@id='tinymce']")
    input_f.send_keys('Incomplete Group Process Table' + '\n' + '\n' + choose)
    browser.switch_to.default_content()
    time.sleep(2)
    save_draft = browser.find_element_by_xpath("//*[@id='currentAttempt_saveButton']")
    save_draft.click()
    time.sleep(3)

time.sleep(2)
print("Done")
browser.quit()
