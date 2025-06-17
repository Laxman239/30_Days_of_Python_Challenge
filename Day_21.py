from bs4 import BeautifulSoup
import requests

html_file = requests.get('https://www.indiatoday.in/').text
soup = BeautifulSoup(html_file, 'lxml')
headlines = soup.find_all('div', class_ = 'B1S3_content__wrap__9mSB6')

for h in headlines:
    print(h.a.text)