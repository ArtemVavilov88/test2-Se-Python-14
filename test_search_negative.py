import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class php4dvd_search_film_negative(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)

    def test_search_negative(self):
        driver = self.driver
        driver.get("http://localhost/php4dvd/")

        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_id("q").clear()
        driver.find_element_by_id("q").send_keys("An amazing film")
        driver.find_element_by_id("q").send_keys(Keys.RETURN)
        #checking message about searching
        getText_message = driver.find_element_by_class_name("content").text
        print getText_message

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()