# This example test demonstrates how to capture a screenshot to your local machine that is running the test script.

import unittest
from selenium import webdriver

class Selenium2OnSauce(unittest.TestCase):

    def setUp(self):
        desired_capabilities = {'browserName': 'firefox'}
        desired_capabilities['version'] = '11'
        desired_capabilities['platform'] = 'Mac 10.6'
        desired_capabilities['name'] = 'Capture screenshot with WebDriver'

        self.driver = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor="http://USERNAME:ACCESS-KEY@ondemand.saucelabs.com:80/wd/hub"
        self.driver.implicitly_wait(30)

    def test_sauce(self):
        self.driver.get('http://google.com')
        sesh = self.driver.session_id
        print "Link to your job: https://saucelabs.com/jobs/%s" % sesh
        self.assertTrue("Google" in self.driver.title);
        self.driver.find_element_by_name('q').send_keys('hello, world!')
        self.driver.find_element_by_name('btnG').click()
        body = self.driver.find_element_by_xpath('//body')
        self.assertTrue('hello' in body.text)
        self.driver.get_screenshot_as_file('google.png') # see http://seleniumhq.org/docs/04_webdriver_advanced.html#taking-a-screenshot

    def tearDown(self):
            self.driver.quit()

if __name__ == '__main__':
    unittest.main()