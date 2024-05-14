import requests
from bs4 import BeautifulSoup

url = 'https://www.nba.com/players'
response = requests.get(url)

if response.status_code == 200:
    html_content = response.content
else:
    print('Failed to retrieve the webpage')
    
soup = BeautifulSoup(html_content, 'html.parser')

data = []

table = soup.find('table', class_='players-list')
table_body = table.find('tbody')
rows = table_body.find_all('tr')
for row in rows:
    cols = row.find_all('td')

    data.append([ele for ele in cols if ele])
    
print(data)