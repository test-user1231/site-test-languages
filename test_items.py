import time


def test_open_browser_with_different_language(browser, user_language):
    link = "http://selenium1py.pythonanywhere.com/{0}/catalogue/coders-at-work_207/".format(user_language)
    browser.get(link)
    browser.implicitly_wait(7)
    btn = browser.find_element_by_css_selector("form >button.btn-add-to-basket")
    if btn:
        print(btn.text)
    time.sleep(20)

