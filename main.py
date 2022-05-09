from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import string

usname = "username here"
passwd = "password here"

driver = webdriver.Chrome("./chrome/chromedriver.exe")  # Create a browser
driver.maximize_window()  # Make it fullscreen


def document_initialised(driver):  #
    return driver.execute_script("return initialised")


def waitUntilLoads(
    driver, timeout=10
):  # document_initialised and waitUntilLoads from Stackoverflow
    WebDriverWait(driver=driver, timeout=timeout).until(document_initialised)


def createRandomSleepTime(  # Just sleeps random seconds. Default between 2 and 5
    min=2, max=5
):
    sleepTime = random.randrange(min, max)
    time.sleep(sleepTime)


def calculateMistake(str):
    maxWrong = int(len(str) / 5)  # Max wrong character count
    print("Max wrong: ")
    countWrong = random.randrange(1, maxWrong)  # Wrong character count
    position = []

    for i in range(countWrong):  # choose random position for wrong characters
        position.append(random.randrange(0, len(str)))
    position.sort()  # Sort it
    position = list(dict.fromkeys(position))  # Remove duplicated elements of list
    return position  # return it


def writeSome(
    element, str
):  # Function use send_key() function for type somethings like human
    action = ActionChains(driver=driver)
    action.move_to_element(element).click().perform()  # click to selected element
    position = calculateMistake(str=str)  # get position array before typing
    j = 0
    for i in range(len(str)):
        if position[j] == i:
            rnd = random.choice(string.ascii_letters.casefold())
            # if true position comes generate a random letter, type it then delete it
            time.sleep(random.random())
            element.send_keys(rnd)
            print(rnd)
            element.send_keys(Keys.BACKSPACE)
            element.send_keys(str[i])
            time.sleep(random.random())
        else:
            # if everything is okay type letter normally
            element.send_keys(str[i])
            time.sleep(random.random())


def loginTwitter(username, password):
    driver.get("https://twitter.com/i/flow/login")  # opens twitter login page
    createRandomSleepTime()
    username_box = driver.find_element(
        by=By.XPATH, value="//input[@name='text']"
    )  # Find username input
    writeSome(username_box, usname)
    username_box.send_keys(Keys.ENTER)
    createRandomSleepTime()
    password_box = driver.find_element(
        by=By.XPATH, value="//input[@name='password']"
    )  # Find password input
    writeSome(password_box, password)
    password_box.send_keys(Keys.ENTER)
    waitUntilLoads(driver)  # Waits until load is over
    driver.quit()


# Just run it for test
loginTwitter(usname, passwd)
createRandomSleepTime()
