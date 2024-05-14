import time
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'https://www.nba.com/players'

driver = webdriver.Safari()
driver.get(url)

data = []

for i in range(12):
    html_content = driver.page_source
    soup = BeautifulSoup(html_content, 'html.parser')
    
    table = soup.find('table', class_='players-list')
    table_body = table.find('tbody')
    rows = table_body.find_all('tr')
    for row in rows:
        names = row.find_all('p')
        names = [ele.text.strip() for ele in names]
        image = row.find(class_='PlayerImage_image__wH_YX PlayerImage_round__bIjPr')
        data.append([names[0] + ' ' + names[1], image.get('src')])
        
    driver.find_element(By.XPATH, "//button[@title='Next Page Button']").click()
    time.sleep(2)

driver.quit()

filename = 'nba.csv'

headers = ['Name', 'Image']

with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow(headers)
    writer.writerows(data)

print(f"Data written to {filename}")