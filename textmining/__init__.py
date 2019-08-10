from textmining.model import SamsungReport


if __name__ == '__main__':
    # static 이므로 바로 사용해도 됨. sr = SamsungReport 이런식으로 지정해주지않아도 됨
 #   f = SamsungReport.read_file()
 #   print(SamsungReport.extract_hangeul(f))
    sam = SamsungReport()
 # 10행 - nltk(자연어토큰) 다운로드를 위한 명령문
#    sam.download()
 # 12행 - nltk 다운로드 완료된 이후 활성화해서 실행 (nltk 다운로드 완료 전까지는 비활성화로 진행)
    print(sam.extract_noun())
