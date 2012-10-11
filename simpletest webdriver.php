// This is an example of using Simpletest (http://simpletest.org/en/start-testing.html) with Selenium 2 (WebDriver) on Sauce Labs' cross-browser testing VMs.

<?php
require_once('simpletest/autorun.php');

class TestSeleniumOnSauce extends UnitTestCase {
    
    function setUp() {
        $wd_host = 'http://USERNAME:API-KEY@ondemand.saucelabs.com:80/wd/hub';
        $web_driver = new PHPWebDriver_WebDriver($wd_host);
        $this->session = $web_driver->session('firefox');
    }
    
    function tearDown() {
        $this->session->close();
    }
    
    function testLoggingInIsLogged() {
        $this->session->open('http://saucelabs.com/test/guinea-pig');
        $this->assertEqual($this->session->title(),
                           "I am a page title - Sauce Labs");
        $element = $web_driver->findElementBy(LocatorStrategy::name, "comments");
        $element->sendKeys(array('hello world'));
        $element->submit();
    }
}
?>