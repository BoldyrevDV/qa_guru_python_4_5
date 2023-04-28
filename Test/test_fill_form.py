from selene import be, have, browser

def test_find_selene(browser_configuration):
    browser.open("https://demoqa.com/automation-practice-form")
