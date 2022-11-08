import csv

inpol = open('C:/Users/kehah/Desktop/pollution.csv', 'r')
poldata = csv.reader(inpol)
list_pol = [i for i in poldata]
inpol.close()


import numpy as np

polarray1 = np.array(list_pol)


polarray1 = np.delete(polarray1, 0, axis=0)
polarray1 = np.delete(polarray1, 0, axis=1)


polarray1 = polarray1.astype(float)
print(polarray1)

array_month6 = polarray1[polarray1[:,0] == 6, :]

array_month6_PM = array_month6[:,4:8]

pm_result = np.vstack((np.mean(array_month6_PM, axis=0),
                   np.std(array_month6_PM,axis=0),
                   np.amin(array_month6_PM,axis=0),
                   np.percentile(array_month6_PM,q=25,axis=0),
                   np.median(array_month6_PM, axis=0),
                   np.percentile(array_month6_PM, q=75, axis=0),
                   np.amax(array_month6_PM, axis=0)))

import csv

with open('C:/Users/kehah/Desktop/pmpm.csv', 'w', newline='') as outfile:
    poldata1 = csv.writer(outfile)
    poldata1.writerows(pm_result)






