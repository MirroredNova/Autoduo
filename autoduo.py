from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import duoconfig

#there are different types of challenges
#div data-test="challenge-select" is pick one of the three pictures
#div data-test="challenge-judge" is a pick one of the three options for the translation
#div data-test="challenge-listenTap" is a multiple choice listening question
#div data-test="challenge-listen" is a written listening question
#div data-test="challenge-tapComplete" is a fill in the blank question
#div data-test="challenge-translate" is a translate the sentence problem
#div data-test="challenge-form" is a fill in the blank but more conjugation based
#div data-test="challenge-name" is a single word translate


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

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='_1cw2r']/button[@data-test='player-next']"))).click()


#def answer_question():


main()
