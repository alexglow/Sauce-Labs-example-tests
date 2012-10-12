import unittest
from selenium import webdriver
from time import sleep

class Selenium2OnSauce(unittest.TestCase):

    def setUp(self):
        desired_capabilities = webdriver.DesiredCapabilities.INTERNETEXPLORER
        desired_capabilities['version'] = '7'
        desired_capabilities['platform'] = 'Windows 2003'
        desired_capabilities['name'] = 'Use a pre-run .bat'
        desired_capabilities['prerun'] = "http://www.YOURDOMAIN.com/example.bat"

        self.driver = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor="http://USERNAME:ACCESS-KEY@ondemand.saucelabs.com:80/wd/hub"
        )
        self.driver.implicitly_wait(30)

    def test_sauce(self):
        sesh = self.driver.session_id
        print "Link to your job: https://saucelabs.com/jobs/%s" % sesh
        self.driver.get('http://google.com')
        self.assertTrue("Google" in self.driver.title);
        self.driver.find_element_by_name('q').send_keys('hello world')
        self.driver.find_element_by_name('btnG').click()
        body = self.driver.find_element_by_xpath('//body')
        self.assertTrue('world' in body.text)

    def tearDown(self):
            self.driver.quit()

if __name__ == '__main__':
    unittest.main()