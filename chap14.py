import numpy as np

# -10 부터 10까지의 배열을 x로 정의
x=np.arange(-10,11)
print(x)

y=4*x+7
print(y)

print(x[0]) # -10

# x1은 음수
x1=x[x<0]
print(x1)