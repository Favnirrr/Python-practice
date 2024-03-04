from sklearn import datasets

from matplotlib import pyplot as plt, cm

digits = datasets.load_digits()
idx = 1500
data = digits.images[idx]
print("answer : " ,digits.target[idx])

plt.imshow(data.reshape(8,8),cmap=cm.gray_r, interpolation='nearest')
plt.show()