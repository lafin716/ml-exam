import pandas as pd

obj = pd.Series([10, 20, 30, 40, 50])
obj_2 = pd.Series([10, 20, 30, 40, 50],
                  index=['a', 'b', 'c', 'd', 'e'])
print(obj)
print(obj.index)
print(obj.values)
print(obj[1])
print(obj_2)
print(obj_2[['a', 'e']])
print(obj_2[1:3])

print('2차원', '=' * 30)
data = {
    '이름': ['유재석', '박명수', '정형돈', '하하', '정준하', '노홍철'],
    '나이': [35, 60, 34, 33, 54, 40],
    '키': [170, 175, 160, 174, 182, 180]}
frame = pd.DataFrame(data)
frame_2 = pd.DataFrame(data,
                       columns=['이름', '나이', '키', '몸무게'])
frame_3 = pd.DataFrame(data, index=['첫째', '둘째', '셋째', '넷째', '다섯째', '여섯째'])
print(data)
print(frame)
print(frame_2)
print(frame_3)
print(frame.head(2))
print(frame.tail(2))

print('데이터 추출', '=' * 30)
print(frame_3.loc['둘째', '이름'])
print(frame_3.loc['넷째', ['나이', '이름']])
print('데이터 추출 iloc ', '=' * 30)
print(frame_3.iloc[2, 0])
print(frame_3.iloc[3, :2])
print(frame_3.iloc[:, [0, 1]])

