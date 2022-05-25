import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# Constants
INSTAGRAM_URL = "https://www.instagram.com/"
CHROME_DRIVER_PATH = "YOUR CHROME DRIVER PATH"
INSTAGRAM_PAGE = "YOUR PREFERRED INSTAGRAM PAGE"
INSTAGRAM_LOGIN_EMAIL = "YOUR LOGIN EMAIL"
INSTAGRAM_LOGIN_PASSWORD = "YOUR PASSWORD"

service = Service(CHROME_DRIVER_PATH)


class InstaFollower:

    def __init__(self, driver_path):
        # Setting up our driver
        self.driver = webdriver.Chrome(service=driver_path)
        self.driver.get(url=INSTAGRAM_URL)

    def login(self):
        # login input fields
        time.sleep(7)
        email_address_input = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div['
                                                                 '1]/div[2]/form/div/div[1]/div/label/input')
        password_input = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/main/article/div[2]/div['
                                                            '1]/div[2]/form/div/div[2]/div/label/input')
        login_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        # Login
        email_address_input.send_keys(INSTAGRAM_LOGIN_EMAIL)
        password_input.send_keys(INSTAGRAM_LOGIN_PASSWORD)
        time.sleep(5)
        login_button.click()

    def find_followers(self):
        # Search for Instagram page.
        time.sleep(6)
        search_bar = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')
        search_bar.send_keys(INSTAGRAM_PAGE)
        time.sleep(5)
        first_result = self.driver.find_element(By.XPATH, '/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div['
                                                          '3]/div/div[ '
                                                          '2]/div/div[1]/a/div/div[2]/div[1]/div/div/div[1]')
        first_result.click()
        time.sleep(5)
        followers_element = self.driver.find_element(By.XPATH,
                                                     '/html/body/div[1]/section/main/div/header/section/ul/li[2]/a/div')
        followers_element.click()

        # Followers pop up window
        time.sleep(5)
        follower_pop_up = self.driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[2]')
        for i in range(10):
            # Scrolling our pop-up window
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follower_pop_up)
            time.sleep(2)

    def follow(self):
        # Finding all Follow buttons in the pop-up window, and following them.
        time.sleep(5)
        follow_buttons = self.driver.find_elements(By.CLASS_NAME, 'sqdOP.L3NKy.y3zKF')

        for each_button in follow_buttons:
            each_button.click()
            time.sleep(2)

    def quit(self):
        time.sleep(5)
        self.driver.quit()


bot = InstaFollower(service)

bot.login()
bot.find_followers()
bot.follow()
bot.quit()
