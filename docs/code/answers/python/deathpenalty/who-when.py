from bs4 import BeautifulSoup
import requests
url = 'http://wgetsnaps.github.io/tdcj-executed-offenders/death_row/dr_executed_offenders.html'
html = requests.get(url).text
soup = BeautifulSoup(html, 'lxml')
rows = soup.select('tr')[1:]

print('race,date')
for r in rows:
   print(r.select('td')[8].text + ',' + r.select('td')[7].text)
