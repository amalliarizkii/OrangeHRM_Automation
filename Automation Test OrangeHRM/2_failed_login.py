import unittest
import time
from selenium import webdriver 
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestLogin(unittest.TestCase): 

    def setUp(self): 
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
   
    def test_a_failed_login_with_invalid_password(self): 

        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin1234") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        #response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"spanMessage").text

        self.assertEqual(response_message, 'Invalid credentials')

    def test_b_failed_login_with_invalid_username(self): 

        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("Admin1") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("admin123") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        #response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"spanMessage").text

        self.assertEqual(response_message, 'Invalid credentials')

    def test_c_failed_login_with_empity_username_dan_password(self): 

        browser = self.browser #buka web browser
        browser.get("https://opensource-demo.orangehrmlive.com/") # buka situs
        time.sleep(3)
        browser.find_element(By.ID,"txtUsername").send_keys("") # isi username
        time.sleep(1)
        browser.find_element(By.ID,"txtPassword").send_keys("") # isi password
        time.sleep(1)
        browser.find_element(By.ID,"btnLogin").click() # klik tombol sign in
        time.sleep(1)

        # validasi
        #response_data = browser.find_element(By.ID,"swal2-title").text
        response_message = browser.find_element(By.ID,"spanMessage").text

        self.assertEqual(response_message, 'Username cannot be empity')

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()