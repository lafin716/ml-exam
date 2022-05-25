import numpy as np

print("배열 선언 ===================")

data = np.array([1,2,3,4,5,6])
data_2d = np.array([[1,2,3], [4,5,6]])
data_random = np.random.randn(2, 3)
data_zeros = np.zeros(5)
data_ones = np.ones((2, 3))
data_arange = np.arange(10, 121, 10)
data_reshape = data_arange.reshape((2, 6))

print(data)
print(data_2d)
print(data_random)
print(data_zeros)
print(data_ones)
print(data_arange)
print(data_reshape)

print("배열 값 접근 ===================")

data = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(data)
print(data[0][1])
print(data[0][1:])
data[0] = 100
print(data)
data[:] = 300
print(data)

print("배열 연산 ==============")

data = np.array([
    [5, 7, 9],
    [-7, -6, 19],
    [6, 8.9, 11]
])

data_2 = data * 2
data_3 = data + 3

print(data)
print(data_2)
print(data_3)
print(data > data_2)

print("배열 통계 ================= ")
data = np.array([
    [5, 7, 9],
    [-7, -6, 19],
    [6, 8, 11]
])

print(data)
print(data.sum())
print(data.mean())
print(data.max())
print(data.min())
print(data.max(axis=0))
index_1 = np.argmax(data, axis=0)
print(index_1)

print("배열 조건식 ==================")
data = np.random.randn(2, 3)
print(data)
print(data > 0)
total = (data < 0).sum()
print(total)
data_minus = np.where(data < 0, 0, data)
print(data_minus)
