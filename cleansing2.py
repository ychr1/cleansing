import re
import pandas as pd
import numpy as np



df = pd.read_csv('test1.csv', encoding="utf-8")

# df["review"] = df["review"].str.replace("[^ㄱ-ㅎ ㅏ-ㅣ 가-힣]","") # 한글만 추출
# df["review"] = df["review"].str.replace("[ㄱ-ㅣ]*","") # ㅋㅋ,ㅎㅎ 삭제


# 앞 공백 처리
# df["review"] = df["review"].str.strip()
# df["point"] = df["point"]


# Null행 삭제
# df = df.dropna()
# print(df.isnull().sum())


df.to_csv('test1.csv', sep=",", encoding="utf-8-SIG", index=False)

