import re
import pandas as pd
# from pandas import DataFrame
# import numpy as np

review_data = pd.read_csv('test.csv')
# df = pd.DataFrame(review_data)
# print(review_data)
review_data["review"] = review_data["review"].str.replace("[^ \u3131-\u3163\uac00-\ud7a3]+","") # 한글만 추출
review_data["review"].str.lstrip()

# review = re.compile("[^ \u3131-\u3163\uac00-\ud7a3]+")

review_data.to_csv('test1.csv', mode="w", encoding='utf-8-SIG', index=False)


