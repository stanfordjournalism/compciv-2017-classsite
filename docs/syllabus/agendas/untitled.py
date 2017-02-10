import requests
from bs4 import BeautifulSoup

resp = requests.get('http://wgetsnaps.github.io/tdcj-executed-offenders/death_row/dr_executed_offenders.html')
txt = resp.text

GODLY_WORDS = ['God', 'Allah', 'Heaven', 'Hell', 'Jesus', 'Holy Spirit']

soup = BeautifulSoup(txt, 'lxml')
inmaterows = soup.select('table tr')[1:]

for row in inmaterows:
    a = row.select('td a')[1]
    print(a.attrs['href'])





def get_last_words(url):
    resp = requests.get(url)




def is_this_godly(txtstr):
    for word in GODLY_WORDS:
        if word in txtstr:
            return True

    return False






