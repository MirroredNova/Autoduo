from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import duoconfig


def main():
    driver = webdriver.Firefox()
    driver.get(duoconfig.base_url)
    login(driver)


def login(driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(.,'I ALREADY HAVE AN ACCOUNT')]"))).click()

    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//label[@class='_1l5ZK']/div[@class='_2uEdv']/input[@data-test='email-input']")))
    password = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//label[@class='_1l5ZK']/div[@class='_2uEdv']/input[@data-test='password-input']")))
    log_in = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div/button[@data-test='register-button']")))

    username.send_keys(duoconfig.duo_username)
    password.send_keys(duoconfig.duo_password)
    log_in.send_keys(Keys.RETURN)

    start_lesson(driver)


def start_lesson(driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='_3ykek']/div[@class='_3bahF _3J-7b']/a[@data-test='global-practice']"))).click()


main()
