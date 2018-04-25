from bs4 import BeautifulSoup
import time
from datetime import datetime, timedelta
meterDayBfYstr = 0
meterYstr = 0

DBfYesterday = datetime.now() - timedelta(days=2)
DBfYesterday = DBfYesterday.strftime('%m_%d_%Y')
YesterdayDate = datetime.now() - timedelta(days=1)
YesterdayDate = YesterdayDate.strftime('%m_%d_%Y')
Yesterday = 'Вчера'

path = "C:/WorkData/Avito/Avito_Daily/GPU_04_24_2018.html"

with open(path, 'r', encoding='utf-8') as f:
    data = f.read()

soup = BeautifulSoup(data, 'html.parser')
print(soup.prettify())
print(type(soup))
print('__________________________')

namelist = []
reflist = []
pricelist = []
timelist = []

for name in soup.find_all('a', class_="description-title-link", href=True):
    namelist.append(name.text)
    reflist.append(name['href'])

print(len(namelist))# amount of ads
print(len(reflist))

for price in soup.find_all('div', class_="price"):
    pricelist.append(price.text)
print(len(pricelist))

DayAmountDayBeforeYesterday = DBfYesterday[3:5]

for date in soup.find_all('span', class_="date"):
    timelist.append(date.text)
    if DayAmountDayBeforeYesterday in date.text:
        meterDayBfYstr+=1
    if Yesterday in date.text[3:9]:
        meterYstr+=1
    print(date.text)

print('Date = ', DBfYesterday, 'DayBefore Yesterday amount: ', meterDayBfYstr)
print('Date = ', YesterdayDate, 'Yesterday amount: ', meterYstr)
print(len(timelist))
