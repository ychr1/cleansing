import re
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


review_data = pd.read_csv('test.csv',encoding="utf-8-SIG")

# review_data["review"] = review_data["review"].str.replace("[^ \u3131-\u3163\uac00-\ud7a3]+","") # 한글만 추출
# review_data["review"] = review_data["review"].str.replace("[ㄱ-ㅣ]*","") # ㅋㅋ,ㅎㅎ 삭제

f = open("stopword.txt", "r")
lines = f.read()
review_data["review"] = review_data["review"].str.replace(lines,"")
f.close()


    


review_data.to_csv('test1.csv', encoding='utf-8-SIG', index=False)




