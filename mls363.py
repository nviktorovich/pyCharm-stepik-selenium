import pytest
from selenium import webdriver
import time
import math

def set_answer():
	return math.log(int(time.time()))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)
    browser.implicitly_wait(15)
    ans_field = browser.find_element_by_css_selector("textarea.textarea")
    ans_field.send_keys(str(set_answer()))
    browser.find_element_by_css_selector("button.submit-submission").click()
    rev = browser.find_element_by_css_selector("pre.smart-hints__hint").text
    assert rev == "Correct!", f'expected "Correct!" - message, but we get: "{rev}"'