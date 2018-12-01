import numpy as np

# rank 가 1인 배열 생성
a = np.array([1,2,3])

print(type(a))
print(a.shape)
print(a[0], a[1], a[2])

a[0] = 5
print(a)


b = np.array([[1,2,3],[4,5,6]])
print(type(b))
print(b.shape)
print(a[0,0], a[0,1], a[0,2])


c = np.zeros((2,2)) # 모든 값이 0인 배열 생성
print(c)


d = np.ones((1,2)) # 모든 값이 1인 배열 생성
print(d)

e = np.pull((2,2),7) # 모든 값이 7인 배열 생성
print(e)

f = np.random.random((2,2)) # 모든 값이 랜덤으로 채워진 배열 생성
print(f)
