#!/usr/bin/python

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import csv
import datetime
import codecs


now = datetime.datetime.now()


if __name__ == "__main__":
 
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://plus.washtec.com/#login')
    time.sleep(10)
    client = driver.find_element_by_xpath("//*[@tabindex='1']")
    username = driver.find_element_by_xpath("//*[@tabindex='2']")
    password = driver.find_element_by_xpath("//*[@tabindex='3']")
    
    # Fill credentials in next 3 rows
    client.send_keys("")
    username.send_keys("")
    password.send_keys("")
    
    login_button= driver.find_element_by_xpath("//*[@tabindex='4']")
    login_button.send_keys(Keys.RETURN)
    time.sleep(10)

    driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[4]/div/div[4]/div/div[2]/div/div[3]/div/div[2]/div/div[2]/div/div/table/tbody/tr/td[2]/table/tbody/tr[2]/td/div/div[3]/div/div[2]/div/div/table/tbody/tr[2]/td[1]").click()
    time.sleep(5)
    
    # In next line adjust absolute path to 'result.csv' where will be placed results of scrape 
    with codecs.open('/var/sentora/hostdata/zadmin/public_html/4_og_cx/result.csv', 'w' , encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile, delimiter=',' )
        writer.writerow([driver.find_element_by_xpath("//*[@class='gwt-HTML']").text,driver.find_element_by_xpath("//*[@class='gwt-Image FB3O21-h-j']").get_attribute("src"),now.strftime("%H:%M")])
      
    driver.quit()
   
