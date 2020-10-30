import re
import pandas as pd
from pandas import DataFrame

df = pd.read_csv('test.csv', sep = ',', encoding= 'utf-8-SIG')

review_column = ['review','point']

# only_BMP_pattern = re.compile("["
#         u"\U00010000-\U0010FFFF" 
#                            "]+", flags=re.UNICODE)
result = []
result= pd.DataFrame(result, columns=review_column)
# for index, row in df.iterrows():    # iterrows 하나에 각 column 이 해당하는 부분들을 출력
#     review = only_BMP_pattern.sub(r' ', str(row['review']))
#     # point = only_BMP_pattern.sub(r' ', str(row['point']))
#     imsi = [row["review"], row["point"]]
#     result.append(imsi)

# result = pd.DataFrame(result, columns=review_column)

print('======= start ========')

"""
   * 입력 문자열에서 한글, 숫자, 영문을 제외한 모든 문자를 제거
   *
   * \uAC00-\uD7A3 : 가-힣 (음계)
   * \u3131-\u314E : ㄱ-ㅎ (자음)
   * \u314F-\u3163 : ㅏ-l (모음)
   * \u318D\u119E\u11A2\u2022\u2025a\u00B7\uFE55 : 천지인 키보드 문자
   * 참조 : http://bit.ly/39Ji0qA
   * '가-힣'으로 할경우 euc-kr 에서는 작동하지 않음.
"""

# emoji_pattern = re.compile("["
#         u"\U0001F600-\U0001F64F"  # emoticons
#         u"\U0001F300-\U0001F5FF"  # symbols & pictographs
#         u"\U0001F680-\U0001F6FF"  # transport & map symbols
#         u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
#                            "]+", flags=re.UNICODE)
# result1=[]
for index, row in result.iterrows():    # iterrows 하나에 각 column 이 해당하는 부분들을 출력
    # review = emoji_pattern.sub(r' ', row['review'])
    review = re.compile('[^ \u3131-\u3163\uac00-\ud7a3]+') # 한글과 띄어쓰기를 제외한 모든 글자
    # review = re.sub("", review)
    # answer = emoji_pattern.sub(r' ', row['owner_comment'])
    # answer = re.sub('[❤️★♥️✨⭐♡♥☆⚽️⚾️❄❣️❤]', ' ', answer)
    # answer = re.sub(pattern=pattern, repl='', string=answer)
    # answer = re.sub('[-=+,#/\:^$@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', ' ', answer)
    # answer = re.sub('▬▬▬▬ ◙ ▬▬▬▬═▂▄▄▓▄▄▂◢◤ █▀▀████▄▄▄▄◢◤█▄ █ █▄ ███▀▀▀▀▀▀▀╬◥█████◤', ' ', answer)
    # point = re.compile('[^ \u3131-\u3163\uac00-\ud7a3]+') 
    # point = re.sub('  ', ' ', answer)

    imsi = [row["review"], row["point"]]
    result.append(imsi)

result = pd.DataFrame(result, columns=review_column)
result.to_csv('test1.csv', mode='w', encoding='utf-8-SIG', index=False)

print('======= end ========')
