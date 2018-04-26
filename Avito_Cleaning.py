from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time, sched
import numpy as np
import csv

s = sched.scheduler(time.time, time.sleep)

def Avito_Cleaning():

    DBfYesterday = datetime.now() - timedelta(days=2)
    DBfYesterday = DBfYesterday.strftime('%m_%d_%Y')
    YesterdayDate = datetime.now() - timedelta(days=1)
    YesterdayDate = YesterdayDate.strftime('%m_%d_%Y')
    TodayDate = datetime.now()
    TodayDate = TodayDate.strftime('%m_%d_%Y')

    path = "C:/WorkData/Avito/Avito_Daily/GPU_" + YesterdayDate #!!!

    with open(path+".html", 'r', encoding='utf-8') as f:
        data = f.read()

    soup = BeautifulSoup(data, 'html.parser')

    namelist = [] # columns in csv
    reflist = []
    pricelist = []
    timelist = []

    for name in soup.find_all('a', class_="description-title-link", href=True):
        namelist.append(name.text)
        reflist.append(name['href'])

    for price in soup.find_all('div', class_="price"):
        pricelist.append(price.text)

    for date in soup.find_all('span', class_="date"):
        if DBfYesterday[3:5] in date.text:
            timelist.append(date.text)
        elif 'Вчера' in date.text[3:9]:
            timelist.append(YesterdayDate)
        elif 'Сегодня' in date.text[3:11]:
            timelist.append(TodayDate)
        else:
            timelist.append(date.text)

    YesterdayIndices = [i for i, x in enumerate(timelist) if x == YesterdayDate]
    DataColumnsLen = len(namelist),len(pricelist),len(timelist),len(reflist)

    namelist = np.array(namelist) #in order to pick only yesterday date
    namelist = namelist[YesterdayIndices]
    pricelist = np.array(pricelist)
    pricelist = pricelist[YesterdayIndices]
    pricelist = [i.strip() for i in pricelist]
    timelist = np.array(timelist)
    timelist = timelist[YesterdayIndices]
    reflist = np.array(reflist)
    reflist = reflist[YesterdayIndices]

    output = zip(namelist,pricelist,timelist,reflist)

    with open(path + ".csv", "w", encoding='utf-8') as f:
        writer = csv.writer(f)
        for row in output:
            writer.writerow(row)

    print('Should be equal, total used ads', DataColumnsLen)
    print('Total GPU ads per day ' + YesterdayDate, len(namelist))
    print('Downloaded rows/Added rows (should be > 1)', DataColumnsLen[0]/len(namelist))
    print('Saved to', path + ".csv")
    #s.enter(60, 1, Avito_Cleaning)


    return('Finished')

Avito_Cleaning()

#s.enter(60, 1, Avito_Cleaning)
#s.run()
