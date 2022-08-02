import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
   
    def test_a_success_edit_MyInfo(self): 

        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[6]/a/b").click() # klik Main menu My Info
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div[2]/form/fieldset/p/input").click() # klik tombol Edit
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div[2]/form/fieldset/ol[1]/li/ol/li[1]/input").clear()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div[2]/form/fieldset/ol[1]/li/ol/li[1]/input").send_keys("Bella")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div[2]/form/fieldset/ol[1]/li/ol/li[2]/input").clear()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div[2]/form/fieldset/ol[1]/li/ol/li[3]/input").clear()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div[2]/form/fieldset/ol[1]/li/ol/li[3]/input").send_keys("Dahlia")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div[2]/form/fieldset/p/input").click()
        time.sleep(1)

        # validasi
        #response_data = browser.find_element(By.ID,"swal2-title").text
        #response_message = browser.find_element(By.ID,"swal2-content").text

        #self.assertEqual(response_message, 'Anda Berhasil Login')

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()