from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure
from helpers.urls import Urls


class AuthPage(BasePage):
    
    NAME_INPUT = (By.XPATH, "//input[@name='name']")
    EMAIL_INPUT = (By.XPATH, "//input[@type='text']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    
    @allure.step("Зарегистрировать нового пользователя")
    def register_user(self, user):
        self.driver.get(Urls.REGISTER_URL)
        
        
        name_input = self.find_element(self.NAME_INPUT)
        name_input.send_keys(user["name"])
        
        
        email_inputs = self.find_elements(self.EMAIL_INPUT)
        email_inputs[1].send_keys(user["email"])
        
        
        password_input = self.find_element(self.PASSWORD_INPUT)
        password_input.send_keys(user["password"])
        
        
        register_button = self.find_element(self.REGISTER_BUTTON)
        register_button.click()
        
       
        self.wait.until(lambda driver: "login" in driver.current_url)
    
    @allure.step("Авторизоваться")
    def login_user(self, email, password):
       
        email_input = self.find_element(self.EMAIL_INPUT)
        email_input.send_keys(email)
        
        
        password_input = self.find_element(self.PASSWORD_INPUT)
        password_input.send_keys(password)
        
       
        login_button = self.find_element(self.LOGIN_BUTTON)
        login_button.click()
        
        
        self.wait.until(lambda driver: Urls.BASE_URL in driver.current_url)
    
    @allure.step("Авторизоваться после регистрации")
    def login_after_registration(self, user):
        
        self.login_user(user["email"], user["password"])