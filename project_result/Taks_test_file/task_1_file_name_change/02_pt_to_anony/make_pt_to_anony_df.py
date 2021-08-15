### Make dataframe which have anony_num and Pt_id

import numpy as np
import pandas as pd

pt_list = np.random.randint(1000000, 10000000, size = 351) 
## 환자번호를 임의로 생성!!!! 351개생성
#print(pt_list)

#src = 'C:\Users\pks98\test'

#### 환자 몇명인지 체크하고 R001, R002 이런식으로 문자열 만들기


num_pt = len(pt_list) ## 환자가 몇명인지 체크
num_pt_list = np.arange(1, num_pt + 1) ## 1부터 마지막 환자까지 생성!!

num_pt_list = list(map(str, num_pt_list)) ## 환자 id를 숫자에서 문자열로 변경!!
how_long = len( str(num_pt)) ## 총 환자수를 문자열로 바꿔서 총 몇자리수인지 체크!! 그거만큼 0 넣어줄거임

num_pt_list = ['C'+ i.zfill(how_long) for i in num_pt_list]  ## 자릿수에 맞추어 0 채워주기
'''
    근데 만약 그냥 26개 있어도 026 이런식으로 맞추면 z.fill(3) 하기

'''


#### 환자 번호랑 익명 값 매칭 시켜서 데이터 프레임으로 만들고 저장하기!!

anony_list = []
anony_list.append(num_pt_list)
anony_list.append(pt_list)

df_anony = pd.DataFrame(anony_list, columns = ['anony_num', 'Pt_ID'])

df_anony.to_csv('C:\\Users\\pks98\\Desktop\\test\\anony_file.csv', index = False)

'''
 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape

   --> 주소에 \ 가 아니라 \\ 이런식으로 하기


'''

####