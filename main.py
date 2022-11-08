# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import numpy as np

array17 = np.arange(1, 13).reshape(4, 3) # 1~12가 원소인 4x3 행렬
print(array17)

print(np.sum(array17)) # 모든원소의 합
print(np.sum(array17, axis=0)) # 열의 합을 1x3 형태로
print(np.sum(array17, axis=1)) #행의 합을 1x4 형태로

print(np.mean(array17)) #평균
print(np.mean(array17, axis=0)) #열 평균
print(np.mean(array17, axis=1)) #행 평균

print(np.var(array17, ddof=1))
print(np.var(array17, axis=0, ddof=1))
print(np.var(array17, axis=1, ddof=1))

