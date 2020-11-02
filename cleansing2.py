import re
import pandas as pd
from pandas import DataFrame

df = pd.read_csv('test.csv', sep = ',', encoding= 'utf-8-SIG')

def cleanning(df):
    clean = re.compile("[^ \3131-\u3163\uac00-\ud7a3]+")
    result = clean.sub("",df)
    return result
# df = review_column.str.replace("[^ㄱ-ㅎ ㅏ-ㅣ 가-힣]","")
df.to_csv('test1.csv', mode="w", encoding='utf-8-SIG', index=False)


