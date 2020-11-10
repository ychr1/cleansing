import re
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from konlpy.tag import Okt


df = pd.read_csv('test1.csv', sep = ",", encoding="utf-8-SIG")

# df["review"] = df["review"].str.replace("[^ㄱ-ㅎ ㅏ-ㅣ 가-힣]","") # 한글만 추출
# df["review"] = df["review"].str.replace("[ㄱ-ㅣ]*","") # ㅋㅋ,ㅎㅎ 삭제


# 앞 공백 처리
# df["review"] = df["review"].str.strip()
# df["point"] = df["point"]


# Null행 삭제
# df = df.dropna()
# print(df.isnull().sum())

okt = Okt()
review = []
for idx, row in df.iterrows():
    temp_r = []
    sentence = row["review"]
    temp_r = okt.morphs(sentence)
    temp_r = " ".join(temp_r)
    review.append(temp_r)

df["review"] = review
df.to_csv('test1.csv', sep=",", encoding="utf-8-SIG", index=False)

