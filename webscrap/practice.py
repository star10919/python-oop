from bs4 import BeautifulSoup
from urllib.request import urlopen
class Bugsmusic(object):
    url = ''

    def __str__(self):
        return self.url


    # https://music.bugs.co.kr/chart/track/realtime/total?wl_ref=M_contents_03_01   (차트 창 url)
    @staticmethod
    def main():
        bugs = Bugsmusic()
        while 1:
            menu = int(input('0.Exit\n1.Input URL\n2.Get Ranking\n3.'))
            if menu == 0:
                break
            elif menu == 1:
                bugs.url = input('Input Url')
            elif menu == 2:
                print(f'Input URL is {bugs}')
                soup = BeautifulSoup(urlopen(bugs.url), 'lxml')

                print('-----------------ARTIST RANKING----------------')
                Bugsmusic.ranking(soup, 'artist')
                print('-----------------TITLE RANKING----------------')
                Bugsmusic.ranking(soup, 'title')
            else:
                print('wrong number')
                continue

    @staticmethod
    def ranking(soup, value):
        count = 0
        for i in soup.find_all(name='p', attrs=({"class": value})):
            count += 1
            print(f'{count}위')
            print(f':{value}:{i.find("a").text}')

Bugsmusic.main()