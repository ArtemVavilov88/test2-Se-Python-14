import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class php4dvd_delete_film(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)

    def test_delete(self):
        driver = self.driver
        driver.get("http://localhost/php4dvd/")

        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()
        #just find the first element with class="nocover"
        driver.find_element_by_class_name("nocover").click()
        driver.find_element_by_link_text("Remove").click()
        #accept the "Are you sure you want to remove this?" dialog
        driver.switch_to_alert().accept()

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()