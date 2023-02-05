import requests # Загрузка новостей с сайта.
import re # Регулярные выражения.
from bs4 import BeautifulSoup
from urllib.request import urlopen
from bs4 import BeautifulSoup
import html


x = open('table.txt','w', encoding='utf8')
d = ['https://www.maam.ru/', 'https://iqsha.ru/', 'https://www.uchportal.ru/load/173',
     'https://www.igraemsa.ru/', 'https://chudo-udo.info/', 'http://www.razvitierebenka.com/',
     'https://poskladam.ru/18/dist/', 'http://razvitiedetei.info/', 'https://iqsha.ru/ilove/post/razvivaiushchie-igry-dlia-detei',
     'https://www.nalog.gov.ru/rn77/fl/'
     ]
for i in d:
    x.write(i + ' ## ')
    print(i)
    resp = requests.get(i)
    # Загружаем текст в объект типа BeautifulSoup.
    bs=BeautifulSoup(resp.text, "html5lib")
    # Получаем заголовок статьи.
    if bs.h1:
        aTitle=bs.h1.text.replace("\xa0", " ")
    # Получаем текст статьи.
        findheaders = re.compile("<output+?>", re.S)
        anArticle=BeautifulSoup(" ".join([p.text for p in bs.find_all("p")]), "html5lib").get_text().replace("\xa0", " ")
        anArticle= anArticle.replace('↑', '')

    #quote = re.compile(".mw-parser-output", re.S)
    #anArticle = "".join(quote.split(anArticle[0]))
    # Возвращаем кортеж из заголовка и текста статьи.
        x.write(str(anArticle))
        x.write('\n')
        print(anArticle) 

     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
     
  #1111
