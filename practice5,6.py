
"""
import csv

coffee1 = open('C:/Users/kehah/Desktop/coffee1.csv','r')
csv_data = csv.reader(coffee1)
list_data = [i for i in csv_data]
coffee1.close()
print(list_data)

import numpy as np

array_data = np.array(list_data)
print(list_data)
array_data = np.delete(array_data, 0, axis=0)#
print(array_data)
array_data = np.delete(array_data, 0, axis=1) #첫행, 첫열 삭제
print(array_data)

array_data = array_data.astype(int) #문자형->정수형 변환
print(array_data)

sum_day = np.sum(array_data,axis = 1) #일별 총판매량
print(sum_day)
sum_menu = np.sum(array_data, axis = 0)#메뉴별 총판매량
print(sum_menu)

mean_day =np.mean(array_data,axis = 1) #일별 평균판매량
print(mean_day)
mean_menu = np.mean(array_data, axis = 0) #메뉴별 평균판매량
print(mean_menu)

###############practice6#############
import csv

J45 = open('C:/Users/kehah/Desktop/J45.csv','r')
pop = open('C:/Users/kehah/Desktop/population.csv','r')

list_J45 = [i for i in csv.reader(J45)]
list_pop = [i for i in csv.reader(pop)]

J45.close()
pop.close()

#2차원 배열
import numpy as np

array_J45 = np.array(list_J45)
array_pop = np.array(list_pop)

#첫 행,열 삭제
array_J45 = np.delete(array_J45, 0, axis=0)#
array_J45 = np.delete(array_J45, 0, axis=1)#
array_pop = np.delete(array_pop, 0, axis=0)#
array_pop = np.delete(array_pop, 0, axis=1) #첫행, 첫열 삭제

#정수형으로 변환
array_J45 = array_J45.astype(int)
array_pop = array_pop.astype(int)

print(array_J45)
print(array_pop)

disease_rate = np.around(array_J45 / array_pop, 3)
print(disease_rate)

total_disease_rate = np.around(np.sum(array_J45, axis=1) / np.sum(array_pop, axis=1),3)
print(total_disease_rate)

"""
#############################prac7############################
import csv

pol = open('C:/Users/kehah/Desktop/pollution.csv','r')
csv_data = csv.reader(pol)
list_data = [i for i in csv_data]
pol.close()


import numpy as np
array1 = np.array(list_data)

array1 = np.delete(array1, 0, axis=0)

array1 = array1.astype(float)
Month = array1[:,1]
#6월 자료만 인덱싱
array_Month6 = (array1[Month == 6,:])

# array_Month_6_2 =array1[np.where(array1[:,1] == 6)[0],:]

#slicing
array_Month6_PM = array_Month6[:,4:8]
array_mean = np.mean(array_Month6_PM, axis=0)
array_std = np.std(array_Month6_PM, axis=0, ddof=1)
result = np.vstack((np.mean(array_Month6_PM, axis=0), np.std(array_Month6_PM, axis=0, ddof=1),
           np.amin(array_Month6_PM, axis=0), np.percentile(array_Month6_PM, q=25, axis=0),
           np.median(array_Month6_PM, axis=0), np.percentile(array_Month6_PM, q=75, axis=0),
           np.amax(array_Month6_PM, axis=0)))



array_min = np.amin(array_Month6_PM, axis=0)

print(np.mean(array_Month6_PM, axis=0))
print(np.std(array_Month6_PM, axis=0, ddof=1))

#csv 파일 저장

import csv
with open('C:/Users/kehah/Desktop/PM_result.csv', 'w', newline='') as outfile:
    data = csv.writer(outfile)
    data.writerows(result)
