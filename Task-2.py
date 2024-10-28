from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Sign_Up_Flow():
    URL = "https://altdrx.com/"

    def __init__(self) -> None:
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.wait = WebDriverWait(self.driver,20)

    def signup(self):
        try :
            self.driver.get(url=self.URL)
            self.driver.maximize_window()
            self.wait.until(EC.url_to_be(self.URL))
            sign_btn = self.wait.until(EC.element_to_be_clickable((By.ID,"signin")))
            sign_btn.click()
            
            self.wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@class='flex flex-col rounded-lg']")))
            signip_lnl = self.wait.until(EC.element_to_be_clickable((By.XPATH,'//a[text()="Sign up"]')))
            signip_lnl.click()
            
            print("SignUp link clicked")
            self.wait.until(EC.visibility_of_element_located((By.XPATH,'//input[@placeholder="Full Name"]')))
            
            f_name_ip = self.driver.find_element(By.XPATH,'//input[@placeholder="Full Name"]')
            f_name_ip.send_keys("Sivachandran")


            resi_sts_dd = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH,'//div[@class ="multiselect text-fs13 rounded-md py-2"]')))
            resi_sts_dd.click()
            resi_indian_op = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, f"//li[span[text()='Resident Indian']]" )))
            resi_indian_op.click()


            ph_no_ip = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH,'(//input[@name="phone"])[1]')))
            ph_no_ip.send_keys('9345813010')


            email_ip = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH,'//input[@placeholder="Email ID"]')
            ))
            email_ip.send_keys('sivachandransekarbe@gmail.com')

            ph_otp_ip = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH,'//input[@name="otp"]')))

            otp = input("Enter OTP received in mobile")
            ph_otp_ip.send_keys(otp)
            
            chck_box_1 = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH,'//div[contains(text(), "By signing up")]/input')
            ))
            chck_box_1.click()
            chck_box_2 = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH,"//div/p[contains(., 'I Agree to')]/parent::div/parent::div/input")
            ))
            chck_box_2.click()

            Register_btn = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH,'//div[@class="flex flex-col rounded-lg bg-white relative z-20"]//button')
            ))
            Register_btn.click()


        except:
            print("Selenium Error : ",Exception)

        finally:
            self.driver.quit()


signupva = Sign_Up_Flow()
signupva.signup()