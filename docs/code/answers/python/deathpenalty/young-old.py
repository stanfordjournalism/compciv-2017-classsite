from bs4 import BeautifulSoup
import requests
url = 'http://wgetsnaps.github.io/tdcj-executed-offenders/death_row/dr_executed_offenders.html'
html = requests.get(url).text
soup = BeautifulSoup(html, 'lxml')
rows = soup.find_all('tr')[1:]

rows = sorted(rows, key=lambda r: int(r.find_all('td')[6].text))

oldstr = "Oldest offender to be executed was {age}-year-old {firstname} {lastname} from {countyname} county, on {date}"

youngstr = "Youngest offender to be executed was {age}-year-old {firstname} {lastname} from {countyname} County, on {date}"

r = rows[-1].find_all('td')
o = oldstr.format(age=r[6].text, firstname=r[4].text, lastname=r[3].text,
              date=r[7].text, countyname=r[9].text)

r = rows[0].find_all('td')
y = youngstr.format(age=r[6].text, firstname=r[4].text, lastname=r[3].text,
              date=r[7].text, countyname=r[9].text)
