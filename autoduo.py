from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from googletrans import Translator

import re
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


def switch(challenge, driver):
    switcher = {
        'challenge-select': select,
        'challenge-judge': judge,
        'challenge-listenTap': listen_tap,
        'challenge-listen': listen,
        'challenge-tapComplete': tap_complete,
        'challenge-translate': translate,
        'challenge-form': form,
        'challenge-name': name
    }
    return switcher.get(challenge, 'invalid')(driver)


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
            (By.XPATH, "//div[@class='_3bahF _3J-7b']/a[@data-test='global-practice']")))

    driver.get(duoconfig.base_url + 'practice')
    next_button(driver)
    check_question_type(driver)


def check_question_type(driver):
    challenge = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='_1Y5M_ _2szQy _27r1x']")))
    challenge = challenge.get_attribute('data-test').split()

    print(challenge[1])
    switch(challenge[1], driver)


def get_question(driver):
    question = driver.find_element_by_xpath("//h1[@data-test='challenge-header']/span")
    return question


def next_button(driver):
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "//div[@class='_1cw2r']/button[@data-test='player-next']"))).click()


def select(driver):
    translator = Translator()
    #“”
    question = get_question(driver).get_attribute('innerHTML')
    question = question.split("”")
    question = question[0].split("“")

    choices = driver.find_elements_by_xpath("//span[@class='_1xgIc']/span")
    for choice in choices:
        translation = translator.translate(choice.get_attribute('innerHTML'), dest="en")
        result = re.search('text=(.*), pronunciation', str(translation))
        if result.group(1) == question[1]:
            print(result.group(1))
            choice.click()
            next_button(driver)
            next_button(driver)
            check_question_type(driver)



def judge(driver):
    print(get_question(driver).get_attribute('innerHTML'))


def listen_tap(driver):
    print(get_question(driver).get_attribute('innerHTML'))


def listen(driver):
    print(get_question(driver).get_attribute('innerHTML'))


def tap_complete(driver):
    print(get_question(driver).get_attribute('innerHTML'))


def translate(driver):
    print(get_question(driver).get_attribute('innerHTML'))


def form(driver):
    print(get_question(driver).get_attribute('innerHTML'))


def name(driver):
    print(get_question(driver).get_attribute('innerHTML'))


main()
