import bs4 as bs
import requests

url = "https://www.repeaterbook.com/repeaters/TravelSearch.php?route=I-90&state_id=46"
r = requests.get(url)

soup = bs.BeautifulSoup(r.content, "html.parser")
table = soup.find_all('table')[2]
rows = table.find_all('tr')
row_list = []
print(rows)

for tr in rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    row_list.append(row)

print(row_list)

""" 
Updated, First print row finds top and first line, unable to locate any other rows afterwords 
"""
