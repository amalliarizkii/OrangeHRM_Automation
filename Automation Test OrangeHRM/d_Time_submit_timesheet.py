import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
   
    def test_a_success_submit_timesheet(self): 

        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[4]/a/b").click() # klik time
        time.sleep(1)
        browser.find_element(By.ID,"menu_time_Timesheets").click() # klik timesheet
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[4]/ul/li[1]/ul/li[2]/a").click() # klik employee timesheet
        time.sleep(1)
        browser.find_element(By.ID,"employee").clear()
        time.sleep(1)
        browser.find_element(By.ID,"employee").send_keys("Cecil Bonaparte") # isi employee name
        time.sleep(1)
        browser.find_element(By.ID,"btnView").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div/div[1]/form/ol/li/select[@name='startDates']/option[text()='2020-09-21 to 2020-09-27']").click()
        time.sleep(1)
        browser.find_element(By.ID,"btnSubmit").click()
        time.sleep(1)

        # validasi
        #response_data = browser.find_element(By.ID,"swal2-title").text
        #response_message = browser.find_element(By.ID,"swal2-content").text

        #self.assertEqual(response_message, 'Anda Berhasil Login')

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()