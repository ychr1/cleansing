import re
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from konlpy.tag import Okt


review_data = pd.read_csv('test1.csv',encoding="utf-8-SIG")

# review_data["review"] = review_data["review"].str.replace("[^ \u3131-\u3163\uac00-\ud7a3]+","") # 한글만 추출
# review_data["review"] = review_data["review"].str.replace("[ㄱ-ㅣ]*","") # ㅋㅋ,ㅎㅎ 삭제

okt = Okt()
review_data = okt.morphs(str(review_data), stem=True)



# 불용어 처리
# f = open("stopword.txt", "r", encoding="utf-8")
# lines = f.readlines()
# review_data["review"] = review_data["review"].str.replace(str(lines),"")
# review_data.to_csv('test1.csv', encoding='utf-8-SIG', index=False)
# f.close()


review_data.to_csv('test1.csv', encoding='utf-8-SIG', index=False)




