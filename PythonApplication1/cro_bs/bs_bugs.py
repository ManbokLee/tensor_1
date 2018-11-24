'''
    https://music.bugs.co.kr/chart/track/realtime/total
    https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20181124&charthour=09


    BeautifulSoup : 크롤링 라이브러리 (심플함)
    urllib : 웹 크롤링 용 라이브러리
'''


from bs4 import BeautifulSoup
from urllib.request import urlopen


def main():
    url = urlopen('https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20181124&charthour=09')

    # lxml 패키지 필요
    soup = BeautifulSoup(url, 'lxml')

    cnt_artist = 0
    cnt_title = 0

    # print(soup)

    for link1 in soup.find_all(name="p", attrs=({"class" : "artist"})):
        cnt_artist += 1
        print(str(cnt_artist) + "위")
        print("아티스트: " + link1.find("a").text.strip())

    print('-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

    for link2 in soup.find_all(name="p", attrs=({"class" : "title"})):
        cnt_title += 1
        print(str(cnt_title) + "위")
        print("노래제목: " + link2.text.strip())

main()