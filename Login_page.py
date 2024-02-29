
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Login_page():
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()
        self.username = "Nandhini"
        self.lastname ="Sundar"
        self.email ="nandhini2024@gmail.com"
        self.phone ="9874562100"
        self.password = "nandhi@12"
        self.confrm = "nandhi@12"
        self.password_invalid = "sdd45"




    def Register(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        self.driver.find_element(By.XPATH,"//a[@title='My Account']").click()
        self.driver.find_element(By.XPATH,"//a[text()='Register']").click()
        self.driver.find_element(By.XPATH,"//input[@name='firstname']").send_keys(self.username)
        self.driver.find_element(By.XPATH,"//input[@name='lastname']").send_keys(self.lastname)
        self.driver.find_element(By.XPATH,"//input[@name='email']").send_keys(self.email)
        self.driver.find_element(By.XPATH,"//input[@name='telephone']").send_keys(self.phone)
        self.driver.find_element(By.XPATH,"//input[@name='password']").send_keys(self.password)
        self.driver.find_element(By.XPATH,"//input[@name='confirm']").send_keys(self.confrm)
        self.driver.find_element(By.XPATH,"//input[@name='agree']").click()
        self.driver.find_element(By.XPATH,"//input[@value='Continue']").click()
        self.driver.find_element(By.XPATH,"//a[text()='Continue']").click()
        self.driver.forward()

    def valid_login(self):
        self.driver.get(self.url)
        self.driver.find_element(By.XPATH,"//a[@title='My Account']").click()
        self.driver.find_element(By.XPATH,"(//a[text()='Login'])[1]").click()
        self.driver.find_element(By.XPATH,"//input[@id='input-email']").send_keys(self.email)
        self.driver.find_element(By.XPATH,"//input[@id='input-password']").send_keys(self.password)
        self.driver.find_element(By.XPATH,"//input[@value='Login']").click()
        current_url = self.driver.current_url
        if current_url != self.url:
            print("Login Successful!")
    def invalid_credentials(self):
        self.driver.get(self.url)
        self.driver.find_element(By.XPATH, "//a[@title='My Account']").click()
        self.driver.find_element(By.XPATH, "(//a[text()='Login'])[1]").click()
        self.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys(self.email)
        self.driver.find_element(By.XPATH,"//input[@id='input-password']").send_keys(self.password_invalid)
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        invalid = self.driver.find_element(By.XPATH,"//div[@class='alert alert-danger alert-dismissible']")
        if invalid.is_displayed():
            print("Login not Successful!!")
    def without_credentials(self):
        self.driver.get(self.url)
        self.driver.find_element(By.XPATH, "//a[@title='My Account']").click()
        self.driver.find_element(By.XPATH, "(//a[text()='Login'])[1]").click()
        self.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys(" ")
        self.driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys(" ")
        self.driver.find_element(By.XPATH, "//input[@value='Login']").click()
        warning = self.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")
        if warning.is_displayed():
            print("Please provide a valid email and password!!")



url = "https://tutorialsninja.com/demo/index.php?route=product/category&path=52"

Login_page(url).Register()
Login_page(url).valid_login()
Login_page(url).invalid_credentials()
Login_page(url).without_credentials()

