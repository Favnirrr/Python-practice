from sklearn import datasets, svm, metrics
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt

# 手書き数字データを読み込む
digits = datasets.load_digits()
print(digits.data)
# 訓練用データとテスト用データに分ける
data_train, deta_test, label_train, label_test = \
    train_test_split(digits.data, digits.target)

# SVMアルゴリズムを利用してモデルを構築する
clf = svm.SVC(gamma=0.001)
clf.fit(data_train, label_train)

# テストデータでの分類結果を予測する
predict = clf.predict(deta_test)

# 結果を表示する
result = list(predict == label_test).count(True) / len(label_test)

print(f'正解率: {result * 100}%')
# plt.imshow(data)