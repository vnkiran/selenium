from threading import Thread
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# This array 'caps' defines the capabilities browser, device and OS combinations where the test will run
caps=[{
      'os_version': '10',
      'os': 'Windows',
      'browser': 'chrome',
      'browser_version': '93.0',
      'name': 'Parallel Test1', # test name
      'build': 'browserstack-build-1' # Your tests will be organized within this build
      },
      {
      'realMobile': 'true',
      'browserName': 'android',
      'device': 'Samsung Galaxy S21 Ultra',
      'os_version': '11.0',
      'name': 'Parallel Test2',
      'build': 'browserstack-build-1'
      },
      {
      'os_version': 'Big Sur',
      'os': 'OS X',
      'browser': 'safari',
      'browser_version': 'latest',
      'name': 'Parallel Test3',
      'build': 'browserstack-build-1'
}]
#run_session function searches for 'BrowserStack' on google.com
def run_session(desired_cap):
  driver = webdriver.Remote(
      command_executor='https://groupin_3Z5k8I:pWQsKswyeTs5jSyWruxa@hub-cloud.browserstack.com/wd/hub',
      desired_capabilities=desired_cap)
  driver.get("https://www.google.com")
  if not "Google" in driver.title:
      raise Exception("Unable to load google page!")
  elem = driver.find_element_by_name("q")
  elem.send_keys("BrowserStack")
  elem.submit()
