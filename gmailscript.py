from selenium import webdriver


def test_search_gmail():
    driver = webdriver.Chrome()
    driver.get("https://mail.google.com/mail/u/0/#inbox")
    email = driver.find_element_by_name("identifier")
    email.send_keys("dominic.maki@gmail.com")
    next_button = driver.find_element_by_class_name("VfPpkd-RLmnJb")
    next_button.click()
    password = driver.find_element_by_name("password")
    password.send_keys("Korexican1234")
    next_button_2 = driver.find_element_by_class_name("VfPpkd-RLmnJb")
    next_button_2.click()
    confirm_button = driver.find_element_by_class_name("RveJvd snByac")
    confirm_button.click()


def main():
    test_search_gmail()


if __name__ == "__main__":
    main()