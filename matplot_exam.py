from matplotlib import pyplot as plt

plt.plot(['유재석', '박명수', '하하'], [85, 100, 95])
plt.title('수학점수')
plt.show()

x = ['유재석', '박명수', '하하', '정형돈']
y_1 = [85, 100, 95, 88]
y_2 = [79, 97, 87, 92]
plt.plot(x, y_1, label='수학',
         color='red', linestyle='-.',
         marker='o')
plt.plot(x, y_2, label='영어')
plt.legend(loc='lower right')
plt.title('수학/영어 성적')
plt.xlabel('이름')
plt.ylabel('점수')
plt.ylim(70, 105)
plt.grid(True)
plt.show()