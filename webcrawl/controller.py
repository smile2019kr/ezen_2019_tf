from webcrawl.assembly import AssemblyCrawler
from webcrawl.bugsmusic import BugsCrawler

class Controller:
    def __init__(self):
        pass

        def exec(self, flag, url):
            if flag == 'a':
                a = AssemblyCrawler('http://likms.assembly.go.kr/bill/billDetail.do?billId=PRC_R1N9J0N1X0Y9A1O8S3R5Z3J3K9O8N7')
                a.scrap()

            elif flag == 'b':
                b = BugsCrawler('https://music.bugs.co.kr/chart/track/realtime/total?chartdate=20190810&charthour=11')
                b.scrap()

#          elif flag == '*':
#             result = self.calc.mul()

#         elif flag == '/':
#            result = self.calc.div()

            return result
