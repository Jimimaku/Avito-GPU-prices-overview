import os
import random
import time
from datetime import datetime, timedelta
from grab import Grab

print('started')

meter = 0
YesterdayStr = ''

for n in range(1,6): # 5
    g = Grab()
    print('starting page number ', n)
    time.sleep(random.uniform(30, 120))#random delay
    #avitourl = 'https://www.avito.ru/sankt-peterburg/tovary_dlya_kompyutera/komplektuyuschie/videokarty?p='+str(n)+'&view=list&s=104'
    avitourl = 'https://www.avito.ru/sankt-peterburg/tovary_dlya_kompyutera/komplektuyuschie/videokarty?p='+str(n)+'&s=104&view=list'
    resp = g.go(avitourl)
    mystr = resp.unicode_body()
    print(type(mystr))
    #print(mystr)
    #print('mystr', type(mystr), mystr)
    print('amount of вчера ', mystr.count('вчера'), 'meter ', meter)
    if mystr.count('вчера') < 4 and meter!=0:
        print('breaking', meter)
        break # yesterday is over
    if "вчера" in mystr:
        print('вчера is in mystr', mystr)
        meter += 1 #counting how many pages in yesterday
    YesterdayStr += mystr + ('\n NEW PAGE URL PAGE\n')

time = datetime.now() - timedelta(days=1)
time = time.strftime('%m_%d_%Y')

print('Finished parsing')

RawDataFileName = 'C:/WorkData/Avito/Avito_Daily/' + 'GPU_' + time + '.html'
with open(RawDataFileName, 'w', encoding='utf-8') as file:
    file.write(YesterdayStr)


print('Finished writing')
