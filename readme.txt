A growing library of example tests for use with your Sauce Labs (saucelabs.com) cross-browser testing account.

This is a work in progress. I don't guarantee that scripts will be kept up to date, but they all successfully pass at the time of publishing.

Feel free to submit examples to alex@saucelabs.com; any submissions will be stripped of identifying information and tested out before publishing.

Repo includes:
• prerun : Example of using a pre-run executable (http://saucelabs.com/docs/additional-config#prerun), used to configure the VM before your test runs on Sauce. You can use this to modify the regedits (https://gist.github.com/alexglow/2962905), install plugins, and so forth.

• python-example-test.py : This covers most common Selenium 2 (WebDriver) commands in Python, plus some useful Desired Capabilities settings. Should be helpful even if you're writing in another language.

• rest example job.py : Covers setting your test's pass/fail status in Sauce, a common desire, in Python/WebDriver via our REST API.

• simpletest webdriver.php : An example of using Simpletest (http://simpletest.org/en/start-testing.html) with WebDriver.