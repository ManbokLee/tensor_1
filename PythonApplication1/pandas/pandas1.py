import pandas as pd
import numpy as np

data = np.array(['a','b','c','d'])
s = pd.Series(data) # 판다스에서 시리즈 타입 만들기
print(s)

data2 = {
    'name' : ['홍길동', '김유신', '유관순', '강감찬'],
    'Age' : [28,30,25,15]
         }
df = pd.DataFrame(data2, index=['1등','2등','3등','4등'])
print(df)


