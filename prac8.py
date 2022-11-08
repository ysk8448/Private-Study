import csv

inpol = open('C:/Users/kehah/Desktop/pollution.csv', 'r')
poldata = csv.reader(inpol)
list_pol = [i for i in poldata]
inpol.close()

import numpy as np
array1 = np.array(list_pol)

#데이터 전처리
array1 = np.delete(array1, 0, axis=0)
array1 = array1.astype(float)
array1 = array1[:, 4:8]

#평균 분산구하기
array1_mean = np.mean(array1, axis=0)
array1_std = np.std(array1, axis=0, ddof=1)

print(array1_mean,2)
print(array1_std,)

#중심화 변환 broadcasting 이용
array1_centering = array1 - array1_mean

#print(np.round(array1_centering,1))
print(array1_centering.shape)
print(array1_mean.shape)

#표준화 변환 broadcasting 이용
array1_stn = array1_centering / array1_std
print(array1_stn)

#표준화된 Z가 평균0, 분산1임을 확인
print(np.mean(array1_stn ,axis=0))
print(np.std(array1_stn, axis=0, ddof=1))


