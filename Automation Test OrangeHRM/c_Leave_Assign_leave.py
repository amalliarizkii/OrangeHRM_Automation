import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
   
    def test_a_success_login(self): 

        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[3]/a/b").click() # klik tab Leave
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[3]/ul/li[7]/a").click() # klik tab Assign leave
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[1]/input[1]").send_keys("Bella Dahlia") # Isi employee name
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[2]/select[@name='assignleave[txtLeaveType]']/option[text()='CAN - Personal']").click() # select 
        time.sleep(1)
        browser.find_element(By.ID,"assignleave_txtFromDate").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[4]/input").send_keys("2022-08-05") # isi From date
        time.sleep(3)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[4]/img").click()
        time.sleep(3)
        browser.find_element(By.ID,"assignBtn").click() # klik tombol Assign
        time.sleep(2)
        
        # validasi
        #response_data = browser.find_element(By.ID,"swal2-title").text
        #response_message = browser.find_element(By.ID,"swal2-content").text

        #self.assertEqual(response_message, 'Anda Berhasil Login')

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()