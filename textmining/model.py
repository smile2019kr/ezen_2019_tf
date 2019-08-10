from konlpy.tag import Okt
from nltk.tokenize import word_tokenize
import re
import nltk


class SamsungReport:
    def __init__(self):
 #       self.okt = Okt
        self.okt = Okt()


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
        print(tokens[:7])
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
        print('------ 추출된 명사 300 ------')
        print(texts[:300])

    @staticmethod
    def download():
        nltk.download()
