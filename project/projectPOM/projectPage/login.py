from selenium import webdriver
import unittest
import time

class GoogleSearchLogin(unittest.TestCase):
    @classmethod
    def SetUpClass(self):
        self.driver = webdriver.Chrome("C:\drivers\chromedriver_win32\chromedriver.exe")
        self.driver.get("http://automationpractice.com/index.php")
        self.driver.implicitly_wait(7)
# login
    def LogInTest(self):
        self.driver.find_element_by_class_name("login").click()
        self.driver.find_element_by_name("email").send_keys("rmosharifa999@gmail.com")  #
        self.driver.find_element_by_name("passwd").send_keys("abc123")
        self.driver.find_element_by_name("SubmitLogin").click()
        time.sleep(2)
    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quite()
        print("Test Completed")
if __name__ == '__main__':
    unittest.main()
# driver.find_element_by_class_name("sf-with-ul").click()
#driver.find_element_by_xpath("/html/body/div/div[1]/header/div[3]/div/div/div[6]/ul/li[2]/a").click()  # dress
