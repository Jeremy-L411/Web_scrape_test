import bs4 as bs
import requests
import urllib.request

# urllib does not work, SSL error
# source = urllib.request.urlopen('https://www.repeaterbook.com/repeaters/TravelSearch.php?route=I-90&state_id=46')
source = requests.get('https://www.repeaterbook.com/repeaters/TravelSearch.php?route=I-90&state_id=46')
soup = bs.BeautifulSoup(source, 'xml.parser')


table = soup.find('table')

table_rows = table.find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)

"""
Attempting to get top of table "Frequency", "Offset", "Tone", "Call" on top
and then loop through the frequencies in the table. It is the second table that I see 
in the inspector, the first is the "On air, off air, Testing, unknown. 
"""