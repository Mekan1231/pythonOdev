from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait





driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.saucedemo.com/")

class Test_Suace:
    def UserNameAndPasswordEmpty(self):
        
        userNameInput=driver.find_element(By.ID,"user-name")
        passwordInput=driver.find_element(By.ID,"password")
        loginBtn=driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()

        errorMessage=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        
        if userNameInput.text=="" and passwordInput.text=="":
            result=errorMessage.text=="Epic sadface: Username is required"
        else:
            print("test koşulu yalnış belirlenmiştir.")

        print(result)

        sleep(5)
    
    def passwordEmpty(self):
        
        userNameInput=driver.find_element(By.ID,"user-name")
        userNameInput.send_keys("mekan")
        passwordInput=driver.find_element(By.ID,"password")
        loginBtn=driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()

        errorMessage=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        
        print(errorMessage.text=="Epic sadface: Password is required")
        sleep(5)
    
    def lockedUser(self):
        
        userNameInput=driver.find_element(By.ID,"user-name")
        userNameInput.send_keys("locked_out_user")
        passwordInput=driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        loginBtn=driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()

        errorMessage=driver.find_element(By.XPATH,"/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3")
        
        print(errorMessage.text=="Epic sadface: Sorry, this user has been locked out.")
        sleep(5)



    def iconCheck(self):
        driver.find_element(By.ID,"login-button").click()
        sleep(3)
        userx=driver.find_element(By.CSS_SELECTOR,"svg:not(:root).svg-inline--fa")
        #passwordx=driver.find_element(By.CLASS_NAME,"svg-inline--fa fa-times-circle fa-w-16 error_icon")
        sleep(3)
        
        xBtn=driver.find_element(By.CSS_SELECTOR,"#login_button_container > div > form > div.error-message-container.error > h3 > button > svg")
        
        

        if userx.is_displayed():
            xBtn.click()
            sleep(3)
            
            if xBtn==object:
                print("İstenilen koşullar sağlanmamıştır.")
            else:
                print("Başarılı. İstenilen koşullar sağlanmıştır.")
               

    def urlCheck(self):
        userNameInput=driver.find_element(By.ID,"user-name")
        userNameInput.send_keys("standard_user")
        passwordInput=driver.find_element(By.ID,"password")
        passwordInput.send_keys("secret_sauce")
        loginBtn=driver.find_element(By.ID,"login-button")
        sleep(2)
        loginBtn.click()
        sleep(2)

        assert driver.current_url=="https://www.saucedemo.com/inventory.html" 

        print("Başarılı. Istenilen koşullar sağlanmıştır.")
        print("------------------")
        print("Son test")

        products=driver.find_elements(By.CLASS_NAME,"inventory_item")

        if products.__len__()==6:
            print("Son test başarılı bir şekilde tamamlanmıştır.")
            print(f"Ürün sayısı: {products.__len__()}")
            

       
        
test=Test_Suace()
#test.UserNameAndPasswordEmpty()
#test.passwordEmpty()
#test.lockedUser()
#test.iconCheck()        
test.urlCheck()
        
        
        

        

        

        


