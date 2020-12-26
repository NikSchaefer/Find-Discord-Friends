from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException

def main():

    username = ''
    password = ''
    driverPath = '../Driver/chromedriver.exe' # set your chromedriver path
    nameToAdd = 'Account name you are searching for'

    def click(xpath):
        driver.find_element_by_xpath(xpath).click()

    def send(xpath, message):
        driver.find_element_by_xpath(xpath).send_keys(message)

    def search(name):
        sleep(0.3)
        driver.find_element_by_xpath(
            '/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div[1]/div/div[2]/form/input').clear()
        send(
            '/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div[1]/div/div[2]/form/input', name)
        click(
            '/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/div[1]/div[1]/div/div[2]/form/button')

    def login(name, pw):
        send(
            "/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/div[2]/input", name)
        send(
            "/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input", pw)
        click(
            "/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]")

    driver = webdriver.Chrome(driverPath)

    driver.get('https://discord.com/login')
    num = 2000

    # set details
    login(username, password)
    sleep(10)
    click(
        '/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[2]/section/div[1]/div[3]/div[5]/span')
    while True:
        try:
            search(nameToAdd + '#' + str(num))
            num += 1
        except NoSuchElementException:
            click(
                '/html/body/div/div[6]/div[2]/div/div/form/div[2]/button')


if __name__ == "__main__":
    main()
