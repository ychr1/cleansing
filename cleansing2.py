import re
import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from konlpy.tag import Okt
from soyspacing.countbase import CountSpace
from soyspacing.countbase import RuleDict
from hanspell import spell_checker
from chatspace import ChatSpace

review_data = pd.read_csv('test1.csv', sep = ",", encoding="utf-8")

# review_data["review"] = review_data["review"].str.replace("[^ \u3131-\u3163\uac00-\ud7a3]+","") # 한글만 추출
# review_data["review"] = review_data["review"].str.replace("[ㄱ-ㅣ]*","") # ㅋㅋ,ㅎㅎ 삭제
# review_data["review"] = review_data["review"].str.replace("<br>","")


# tokenizer = Mecab()
# okt = Okt()
# stopword = []
# review_data = okt.morphs(str(review_data), stem=True)

# with open("stopword.txt", "r", encoding="utf-8") as file:
#     for text in file:
#         w = text.strip("\n")
#         stopword.append(w)


# review = []

# for row in review_data["review"]:
#     sentence = row["review"]
#     review_data["review"] = okt.morphs(sentence)

    # r_temp = []
    # for token in temp_r:
    #     if token not in stopword:
    #         r_temp.append(token)
    # tokennized_sent = " ".join(r_temp)
    # review.append(tokennized_sent)

# Null행 삭제
# review_data = review_data.dropna()
# print(review_data.isnull().sum())
with open("test1.csv", encoding="UTF-8") as f:
    line = f.read()
    spacer = line.ChatSpace()
    review_data["review"] = spacer.space(str(line))


review_data.to_csv('test1.csv', sep=",", encoding="utf-8-SIG", index=False)




