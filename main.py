'''Test for launching qxf2.com in AWS machine through grid'''
 
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
 
def test_chrome():
    #Set desired capabilities
    desired_capabilities = DesiredCapabilities.CHROME
    desired_capabilities['platform'] = 'LINUX'
 
    #Using Remote connection to connect to aws grid - Used manager ip
    url = "http://113.55.14.53:4444/wd/hub"
    driver  = webdriver.Remote(url, desired_capabilities)
 
    #Checking the driver session
    print (driver)
 
    #Launch qxf2 and print title
    driver.get("http://ehall.ynu.edu.cn")
 
    print (driver.title)
    driver.quit()

if __name__ == '__main__':
    test_chrome()