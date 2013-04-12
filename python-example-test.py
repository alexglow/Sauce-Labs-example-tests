# A test that includes most common commands and some useful Desired Capabilities settings. 

import unittest
from selenium import webdriver
from time import sleep

class GLaDOS(unittest.TestCase):

    def setUp(self):
        desired_capabilities = webdriver.DesiredCapabilities.INTERNETEXPLORER
        desired_capabilities['version'] = '9'
        desired_capabilities['platform'] = 'Windows 2008'
        desired_capabilities['name'] = 'Useful Python commands'
        
        # http://saucelabs.com/docs/additional-config
        desired_capabilities['tags'] = ['cloud', 'testing']
        desired_capabilities['custom-data'] = { "release": "1.0", "commit": "0k392a9dkjr", "staging": "true" }
        desired_capabilities['idle-timeout'] = 60 #seconds
        
        self.driver = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor="http://USERNAME:API-KEY@ondemand.saucelabs.com:80/wd/hub")
        self.driver.implicitly_wait(30)

    def test_sauce(self):
        
        self.driver.get('http://saucelabs.com/test/guinea-pig')
        self.assertTrue("I am a page title" in self.driver.title)
        self.driver.find_element_by_link_text('i am a link').click()
        self.driver.back()

        commentbox = self.driver.find_element_by_id('comments')
        commentbox.send_keys('hello, world!')
        commenttext = "\n" + commentbox.get_attribute('value') + "\n"
        print commenttext
        
        commentbox.clear()
        commentbox.send_keys('hello again!')
        commentbox.submit()
        body = self.driver.find_element_by_xpath('//body')
        self.assertTrue('hello again!' in body.text)
        
        sleep(20) # Use sparingly! Implicit waits are usually better.
        
        html_source = self.driver.page_source
        self.assertTrue('i_am_an_id' in html_source)
        
        # Write page source to a file in PWD
        ascii_source = html_source.encode('ascii', 'ignore')
        source_file = open("pagesource.txt", "w")
        source_file.write(ascii_source)
        source_file.close()
        
        self.driver.get_screenshot_as_file('guineapig.png') # Also saves to PWD
        
        sesh = self.driver.session_id
        print "Link to your job: https://saucelabs.com/jobs/%s" % sesh
        
    def tearDown(self):
            self.driver.quit()

if __name__ == '__main__':
    unittest.main()