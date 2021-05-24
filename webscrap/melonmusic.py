import urllib.request

from bs4 import BeautifulSoup
from urllib.request import urlopen
class Melonmusic(object):
    url = ''
    hdr = {'User-Agent': 'Mozilla/5.0'}

    def __str__(self):
        return self.url

#  https://www.melon.com/chart/index.htm
    @staticmethod
    def main():
        melon = Melonmusic()
        while 1:
            menu = int(input('0.EXIT \n 1.Input url \n 2.Get Ranking \n '))
            if menu == 0:
                break
            elif menu == 1:
                melon.url = input('Input Url')
            elif menu == 2:

                req = urllib.request.Request(melon.url, headers=melon.hdr)
                html = urllib.request.urlopen(req).read()

                print(f'Input URL is {melon}')
                soup = BeautifulSoup(html, 'lxml')
                print('-----Artist Ranking-----')
                count = 0
                for i in soup.find_all(name='div', attrs=({"class": "ellipsis rank01"})):
                    count += 1
                    print(f'{str(count)}위')
                    print(f'ARTIST: {i.find("a").text}')

                print('-----Title Ranking-----')
                count = 0
                for i in soup.find_all(name='div', attrs=({"class": "ellipsis rank02"})):
                    count += 1
                    print(f'{str(count)}위')
                    print(f'Title: {i.find("a").text}')
            else:
                print('wrong number')
                continue

Melonmusic.main()