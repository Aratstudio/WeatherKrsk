# coding=utf-8
import bs4
import requests


s = requests.get('https://sinoptik.com.ru/погода-красноярск')

b = bs4.BeautifulSoup(s.text, "html.parser")
p3 = b.select('.temperature .p3')
pogoda1 = p3[0].getText()


print (pogoda1)

p = b.select('.rSide .description')

pogoda = p[0].getText()
print (pogoda.strip())
