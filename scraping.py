from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import mysql.connector


cnx = mysql.connector.connect(user='root',port=3308, password='',
                          host='127.0.0.1',
                          db='data')
cursor=cnx.cursor()
path='chromedriver'
driver=webdriver.Chrome(path)
url='C:/Users/HP/Desktop/IMDb.html'
driver.get(url)




first_part="//*[@id='main']/div/span/div/div/div[3]/table/tbody/tr["
Title_part="]/td[2]/a"
Image_part="]/td[1]/a"
Rating_part="]/td[3]/strong"
Release_part="]/td[2]/span"
for n in range(1,10):
    Title=first_part+str(n)+Title_part
    Image=first_part+str(n)+Image_part
    Rating=first_part+str(n)+Rating_part
    ReleaseYear=first_part+str(n)+Release_part
    table1=driver.find_element_by_xpath(Title).text
    table2=driver.find_element_by_xpath(Rating).text
    table3=driver.find_element_by_xpath(Image).text
    table4=driver.find_element_by_xpath(ReleaseYear).text
    cursor.execute("INSERT INTO movies(Title,ReleaseYear,Rank,Rating,Url,Image) VALUES (%s,%s,%s,%s,%s,%s)", (table1,table4," ",table2," ",table3))
mysql.connection.commit()



