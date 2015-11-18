import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class php4dvd_search_film_positive(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)

    def test_search_positive(self):
        driver = self.driver
        driver.get("http://localhost/php4dvd/")

        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_id("q").clear()
        driver.find_element_by_id("q").send_keys("Snatch")
        driver.find_element_by_id("q").send_keys(Keys.RETURN)
        # There is the film which was found
        driver.find_element_by_css_selector("div[title=Snatch]")

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()