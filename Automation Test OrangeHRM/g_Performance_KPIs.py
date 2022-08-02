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
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[7]/a/b").click() # klik performance
        time.sleep(1)
        browser.find_element(By.ID,"menu_performance_Configure").click() # klik configure
        time.sleep(1)
        browser.find_element(By.ID,"menu_performance_searchKpi").click() # klik KPI`s
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[2]/form/div[1]/input[1]").click() # klik add
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[2]/form/fieldset/ol/li[1]/select").click()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[2]/form/fieldset/ol/li[1]/select[@name='defineKpi360[jobTitleCode]'/option[text()='Content Specialist']")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[2]/form/fieldset/ol/li[2]/input").send_keys("Communication")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[2]/form/fieldset/ol/li[3]/input").clear
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div[2]/form/fieldset/ol/li[3]/input").send_keys("50")
        time.sleep(1)
        browser.find_element(By.ID,"saveBtn").click()
        time.sleep(1)



        # validasi
        #response_data = browser.find_element(By.ID,"swal2-title").text
        #response_message = browser.find_element(By.ID,"swal2-content").text

        #self.assertEqual(response_message, 'Anda Berhasil Login')

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()