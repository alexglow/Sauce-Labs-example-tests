# This test sets pass/fail status, sets visibility status to "Public", and retrieves the session ID, for each test.

import unittest
from selenium import webdriver
import httplib
import base64
import json
import sys

config = {"username": "YOUR-USERNAME",
          "access-key": "YOUR-API-KEY"}

class Selenium2OnSauce(unittest.TestCase):

    def setUp(self):
        desired_capabilities = webdriver.DesiredCapabilities.INTERNETEXPLORER
        desired_capabilities['platform'] = 'XP'
        desired_capabilities['version'] = '8'
        desired_capabilities['avoid-proxy'] = True
        desired_capabilities['name'] = 'Set job to public via REST API'

        self.driver = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor="http://%(username)s:%(access-key)s@ondemand.saucelabs.com:80/wd/hub" % config
        )
        self.driver.implicitly_wait(30)

    def report_pass_fail(self):
        base64string = base64.encodestring('%s:%s' % (config['username'],
                                                      config['access-key']))[:-1]
        result = json.dumps({'public':'true','passed': sys.exc_info() == (None, None, None)})
        connection = httplib.HTTPConnection("saucelabs.com")
        connection.request('PUT', '/rest/v1/%s/jobs/%s' % (config['username'],
                                                           self.driver.session_id),
                           result,
                           headers={"Authorization": "Basic %s" % base64string})
        result = connection.getresponse()
        return result.status == 200

    def test_passes(self):
        self.driver.get('http://www.google.com')
        sesh = self.driver.session_id
        print "Link to test_passes: https://saucelabs.com/jobs/%s" % sesh
        self.driver.find_element_by_name('q').send_keys('pass')
        self.assertTrue("Google" in self.driver.title)

    def test_fails(self):
        self.driver.get('http://www.google.com')
        sesh = self.driver.session_id
        print "Link to test_fails: https://saucelabs.com/jobs/%s" % sesh
        self.driver.find_element_by_name('q').send_keys('fail')
        self.assertFalse("Google" in self.driver.title)

    def tearDown(self):
        self.report_pass_fail()
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()