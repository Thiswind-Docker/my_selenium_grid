'''Test for launching baidu.com in AWS machine through grid'''
 
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
 
def test_firefox():
    #Set desired capabilities
    desired_capabilities = DesiredCapabilities.FIREFOX
    desired_capabilities['platform'] = 'LINUX'
 
    #Using Remote connection to connect to aws grid - Used manager ip
    url = "http://localhost:4444/wd/hub"
    driver  = webdriver.Remote(url, desired_capabilities)
 
    #Checking the driver session
    print (driver)
 
    #Launch baidu and print title
    driver.get("http://www.baidu.com")
 
    print (driver.title)
    driver.quit()
