from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest






class Test_Suace:
    def setup_method(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.saucedemo.com/")
        self.userNameInput=self.driver.find_element(By.ID,"user-name")
        self.passwordInput=self.driver.find_element(By.ID,"password")
        self.loginBtn=self.driver.find_element(By.ID,"login-button")

    def teardown_method(self):
        self.driver.quit()

    def test_userNameAndPasswordEmpty(self):
        self.loginBtn.click()
        errorMessage=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        assert errorMessage.text=="Epic sadface: Username is required"


    @pytest.mark.skip() 
    def test_passwordEmpty(self):
        self.userNameInput.send_keys("mekan")
        self.loginBtn.click()
        errorMessage=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        assert errorMessage.text=="Epic sadface: Password is required"
        
    
    def test_lockedUser(self):
        self.userNameInput.send_keys("locked_out_user")
        self.passwordInput.send_keys("secret_sauce")
        self.loginBtn.click()
        errorMessage=self.driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        assert errorMessage.text=="Epic sadface: Sorry, this user has been locked out."
        



    def test_iconCheck(self):
        self.loginBtn.click()
        sleep(1)
        userx=self.driver.find_element(By.CSS_SELECTOR,"svg:not(:root).svg-inline--fa")
        #passwordx=driver.find_element(By.CLASS_NAME,"svg-inline--fa fa-times-circle fa-w-16 error_icon")
        sleep(1)
        xBtn=self.driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div.error-message-container.error > h3 > button > svg")
        
        if userx.is_displayed():
            xBtn.click()
            sleep(3)
            
            if xBtn==object:
                assert True
            
               

    def test_urlCheck(self):
        self.userNameInput.send_keys("standard_user")
        self.passwordInput.send_keys("secret_sauce")
        self.loginBtn.click()
        sleep(1)
        assert self.driver.current_url=="https://www.saucedemo.com/inventory.html" 

        
        

    def test_product_count(self):
        self.userNameInput.send_keys("standard_user")
        self.passwordInput.send_keys("secret_sauce")
        self.loginBtn.click()
        sleep(1)
        products=self.driver.find_elements(By.CLASS_NAME,"inventory_item")
        assert products.__len__()==6

            
            

       
        

        
        
        

        

        

        


