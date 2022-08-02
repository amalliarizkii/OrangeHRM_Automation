import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
   
    def test_a_success_add_username_with_valid_employee_name(self): 

        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a/b").click() # klik tab Admin
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/ul/li[1]/a").click() # klik tab user management
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/ul/li[1]/ul/li/a").click() # klik tab users
        time.sleep(1)
        browser.find_element(By.ID,"btnAdd").click() # klik tombol Add
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[2]/input[1]").send_keys("Bella Dahlia") # isi employee name
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[3]/input").send_keys("bella.dahlia") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"systemUser_password").send_keys("New.york20") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"systemUser_confirmPassword").send_keys("New.york20") # confirm password
        time.sleep(1)
        browser.find_element(By.ID,"btnSave").click() # klik tombol Save
        time.sleep(1)

    def test_b_failed_add_username_with_invalid_employee_name(self): 

        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a/b").click() # klik tab Admin
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/ul/li[1]/a").click() # klik tab user management
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/ul/li[1]/ul/li/a").click() # klik tab users
        time.sleep(1)
        browser.find_element(By.ID,"btnAdd").click() # klik tombol Add
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[2]/input[1]").send_keys("Ayu Azzahra") # isi employee name
        time.sleep(1)       

    def test_c_success_search_username_with_valid_username(self): 

        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a/b").click() # klik tab Admin
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/ul/li[1]/a").click() # klik tab user management
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/ul/li[1]/ul/li/a").click() # klik tab users
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[1]/input").send_keys("bella.dahlia") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"searchBtn").click() # klik tombol search
        time.sleep(1)

    def test_d_failed_search_username_with_invalid_username(self): 

        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # klik tombol sign in
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/a/b").click() # klik tab Admin
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/ul/li[1]/a").click() # klik tab user management
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[1]/ul/li[1]/ul/li/a").click() # klik tab users
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol/li[1]/input").send_keys("bella.dahlia1") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"searchBtn").click() # klik tombol search
        time.sleep(1)    

        # validasi
        #response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/form/fieldset/ol/li[2]/span").text

        self.assertEqual(response_message, 'Employee does not exist')

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()