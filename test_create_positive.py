import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class php4dvd_create_film_positive(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(20)

    def test_create_film_positive(self):
        driver = self.driver
        driver.get("http://localhost/php4dvd/")

        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys("admin")
        driver.find_element_by_name("submit").click()
        driver.find_element_by_link_text("Add movie").click()
        driver.find_element_by_name("imdbid").send_keys("0003")
        driver.find_element_by_name("name").send_keys("Test-film")
        driver.find_element_by_name("aka").send_keys("Test-information")
        driver.find_element_by_name("year").send_keys("2015")
        driver.find_element_by_name("duration").send_keys("0000")
        driver.find_element_by_id("own_no").click()
        driver.find_element_by_name("plots").send_keys("test-test")
        driver.find_element_by_id("submit").click()
        #checking film's name
        getText = driver.find_element_by_tag_name("h2").text
        print getText

    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()

