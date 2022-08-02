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
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[5]/a/b").click() # klik main menu Recruitment
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[2]/ul/li[5]/ul/li[1]/a").click() # klik submenu Candidates
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[2]/div/form/div[1]/input[1]").click() # klik tombol Add
        time.sleep(1)
        browser.find_element(By.ID,"addCandidate_firstName").send_keys("Bella") # isi Fullname
        time.sleep(1)
        browser.find_element(By.ID,"addCandidate_lastName").send_keys("Dahlia") # isi Lastname
        time.sleep(1)
        browser.find_element(By.ID,"addCandidate_email").send_keys("bella.dahlia4@gmail.com") # isi email
        time.sleep(1)
        browser.find_element(By.ID,"addCandidate_contactNo").send_keys("+61 876 7772429") # isi No hp
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol[2]/li[1]/select[@name='addCandidate[vacancy]']/option[text()='Associate IT Manager']").click() # select 
        time.sleep(1)
        browser.find_element(By.ID,"addCandidate_appliedDate").clear()
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol[2]/li[5]/input").send_keys("2022-08-05")
        time.sleep(1)
        browser.find_element(By.XPATH,"/html/body/div[1]/div[3]/div[1]/div[2]/form/fieldset/ol[2]/li[5]/img").click()
        time.sleep(3)
        browser.find_element(By.ID,"btnSave").click()
        time.sleep(1)



        # validasi
        #response_data = browser.find_element(By.ID,"swal2-title").text
        #response_message = browser.find_element(By.ID,"swal2-content").text

        #self.assertEqual(response_message, 'Anda Berhasil Login')

    def tearDown(self): 
        self.browser.close() 

if __name__ == "__main__": 
    unittest.main()