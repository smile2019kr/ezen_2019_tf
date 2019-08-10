from konlpy.tag import Okt
from nltk.tokenize import word_tokenize
import re
import nltk
import pandas as pd
from nltk import FreqDist
#빈도수 출력하는 클래스를 nltk에서 불러오기
from wordcloud import WordCloud
import matplotlib.pyplot as plt

class SamsungReport:
    def __init__(self):
 #       self.okt = Okt
        self.okt = Okt()

 #   @staticmethod  -> 15행에서 self.okt.pos~~~를 사용하게 되므로 12행에 기재한 이 표기를 삭제하고 13행 def read_file(): 의 괄호안에 self 기재
    def read_file(self):
#        okt = Okt()
#        okt.pos("삼성전자 글로벌센터 전자사업부", stem=True)
        self.okt.pos("삼성전자 글로벌센터 전자사업부", stem=True)
        filename = './data/kr-Report_2018.txt'
        # r : read.  encoding은 global한 한글인식을 위해 utf-8 (영어 인코딩의 경우 불필요)
        with open(filename, 'r', encoding='utf-8') as f:
            texts = f.read()
        return texts

    @staticmethod
    #한글만 뽑아내기
    def extract_hangeul(texts):
        #줄바꿈을 공백으로 만들어라
        temp = texts.replace('\n', ' ')
        # 한글의 시작(ㄱ)과 끝(힣). 반드시 처음시작부터 끝까지 한글이 있는 것만 token으로 분류해라
        tokenizer = re.compile(r'[^ ㄱ-힣]+')
        temp = tokenizer.sub('', temp)
        return temp

    @staticmethod
    def change_token(texts):
        tokens = word_tokenize(texts)
     #   print(tokens[:7])
        return tokens

# 명사만 추출. 조사를 삭제하겠다는 것.
    def extract_noun(self):
        # 삼성전자의 스마트폰은  -> 삼성전자 스마트폰
        noun_tokens = []
        tokens = self.change_token(self.extract_hangeul(self.read_file()))
        for token in tokens:
            token_pos = self.okt.pos(token)
            #명사가 1개 이상이면 붙여버리라는 명령문
            temp = [txt_tag[0] for txt_tag in token_pos if txt_tag[1] == 'Noun']
            if len(''.join(temp)) > 1:
                noun_tokens.append("".join(temp))
        texts = " ".join(noun_tokens)
        # 디버깅용
    #    print('------ 추출된 명사 300 ------')
    #    print(texts[:300])
        return texts

#nltk 다운로드하기
    @staticmethod
    def download():
        nltk.download()

#stopword 53행까지의 결과를 보고 분석에 필요없는 단어들을 삭제하는 것.
    # 데이터폴더에 stopword.txt 로 주어져있음
    @staticmethod
    def read_stopword():
        stopfile = './data/stopwords.txt'
        with open(stopfile, 'r', encoding='utf-8') as f:
            stopwords = f.read()
        stopwords = stopwords.split(' ')
#디버깅용으로 10개만 출력
     #   print('------- 제거할 단어 --------')
     #   print(stopwords[:10])
        return stopwords

# stopwords 삭제하기

#    @staticmethod 기본적으로 사용했다가 78, 79행을 추가하면서 self 를 사용하게 되어 삭제한 것
    def remove_stopword(self):
        texts = self.extract_noun()
        tokens = self.change_token(texts)
  #      print('-------- 1 명사 -----')
   #     print(texts[:30])
        stopwords = self.read_stopword()
    #    print('------ 2 스톱 ---------')
    #    print(stopwords[:30])
   #     print('------ 3 필터 --------')
        texts = [text for text in tokens if text not in stopwords]
   #     print(texts[:30])
        return texts
        # 메소드는 단일기능을 수행하도록 하는게 나으므로 return texts 로 마무리
# 디버깅 체크 후, 1,2,3의 출력문을 비활성화

    # 단어빈도 산출에 pandas 필요하므로 올라가서 pandas as pd
    def find_freq(self):
        # stopwords가 제거된 상태의 texts를 사용해야 하므로 아래와 같이 입력
        texts = self.remove_stopword()
        freqtxt = pd.Series(dict(FreqDist(texts))).sort_values(ascending=False)
        #ascending=False 로 지정하였으므로 빈도수가 큰수부터 내려옴
        print(freqtxt[:30])

#wordcloud를 불러와야하므로 터미널에서 pip install wordcloud 설치 후 맨 위에 가서 wordcloud 불러오기
    def draw_wordcloud(self):
        texts = self.remove_stopword()
        # D2Coding.ttf -> 폰트. sleck에서 다운로드
        wcloud = WordCloud('./data/D2Coding.ttf', relative_scaling=0.2, background_color='white').generate(" ".join(texts))
        plt.figure(figsize=(12,12))
        plt.imshow(wcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()
