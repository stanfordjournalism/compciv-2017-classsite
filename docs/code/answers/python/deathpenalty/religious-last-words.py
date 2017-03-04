
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import requests


SRC_URL = 'http://wgetsnaps.github.io/tdcj-executed-offenders/death_row/dr_executed_offenders.html'

def extract_last_words_url(inmate_tr):
    tds = inmate_tr.select('td')
    lastword_td = tds[2]
    link = lastword_td.select('a')[0]
    href = link.attrs['href']

    return urljoin(SRC_URL, href)

def has_religious_words(txtstr):
    RELIGIOUSWORDS = ['God', 'Lord', 'Savior', 'Soul', 'Allah', 'Prophet', 'Heaven', 'Hell']
    for word in RELIGIOUSWORDS:
        if word in txtstr:
            return True
        else:
            pass # keep on going
    # if for loop ends, that means all
    # religiouswords were tested
    return False

def fetch_inmate_rows():
    html = requests.get(SRC_URL).text
    soup = BeautifulSoup(html, 'lxml')
    inmate_rows = soup.find_all('tr')[1:]
    return inmate_rows


for row in fetch_inmate_rows():
    lastwords_url = extract_last_words_url(row)
    if 'no_last_statement' not in lastwords_url:
        # fetch page
        lastwordsresp = requests.get(lastwords_url)
        txt = lastwordsresp.text
        if has_religious_words(txt):
            cols = row.find_all('td')
            print(cols[4].text, cols[3].text, 'is religious:', lastwords_url)
