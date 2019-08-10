from webcrawl.assembly import AssemblyCrawler
from webcrawl.bugsmusic import BugsCrawler
from webcrawl.krx import KrxCrawler
from webcrawl.naver_stock import StockModel
from webcrawl.naver_movie import NaverMovie
from webcrawl.naver_login import NaverLogin

class Controller:
    def __init__(self):
        pass

    def exec(self, flag):
            if flag == 'a':
                a = AssemblyCrawler('http://likms.assembly.go.kr/bill/billDetail.do?billId=PRC_R1N9J0N1X0Y9A1O8S3R5Z3J3K9O8N7')
                a.scrap()

            elif flag == 'b':
                b = BugsCrawler('https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20190810&charthour=11')
                b.scrap()

            elif flag == 'k':
                k = KrxCrawler('http://kind.krx.co.kr/disclosureSimpleSearch.do?method=disclosureSimpleSearchMain')
                k.scrap()

            elif flag == 'ns':
                ns = StockModel('005930')
                ns.scrap()

            elif flag == 'nm':
                nm = NaverMovie('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
                nm.scrap()

            #https://nid.naver.com/nidlogin.login 자동로그인
            elif flag == 'nl':
                nl = NaverLogin('https://nid.naver.com/nidlogin.login')
                nl.auto_login()


 #def print_menu():
  #          print('a. 국회 크롤링: ')
   #         print('b. 벅스 크롤링: ')
    #        print('0. 종료')
     #       flag = input('메뉴선택 \n')
      #      return flag


#         elif flag == '/':
#            result = self.calc.div()

#            return result
