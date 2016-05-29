import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_log_in(self):
        driver = self.driver
        driver.get("https://mail.ex.ua/")
        elem = driver.find_element_by_name('login')
        elem.send_keys("email")
        elem.send_keys(Keys.RETURN)
        elem2 = driver.find_element_by_name('password')
        elem2.send_keys("password")
        elem2.send_keys(Keys.RETURN)
        assert driver.find_element_by_xpath('/html/body/script[4]')

        def tearDown(self):
            self.driver.close()

if __name__ == "__main__":
    unittest.main()