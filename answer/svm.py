"""
    SVMアルゴリズムで手書き文字の判定を学習し、また結果を評価します.
"""
from sklearn import svm, metrics
import joblib

# 学習用のデータを読み込みます.
with open("./csv/train-images.csv") as f:
    images = f.read().split("\n")[:500]
with open("./csv/train-labels.csv") as f:
    labels = f.read().split("\n")[:500]

# 機械学習のモデルに読み込むために、データを変換します.
images = [[int(i)/256 for i in image.split(",")] for image in images]
labels = [int(l) for l in labels]

# モデルの学習を行います.
clf = svm.SVC()
clf.fit(images, labels)

# テストデータを読み込みます.
with open("./csv/test-images.csv") as f:
    test_images = f.read().split("\n")[:500]
with open("./csv/test-labels.csv") as f:
    test_labels = f.read().split("\n")[:500]

# 機械学習のモデルに読み込むために、データを変換します.
test_images = [[int(i)/256 for i in image.split(",")] for image in test_images]
test_labels = [int(l) for l in test_labels]

# 予測します.
predict = clf.predict(test_images)

# 予測精度を表示します.
ac_score = metrics.accuracy_score(test_labels, predict)
cl_report = metrics.classification_report(test_labels, predict)
print("Accuracy:", ac_score)
print(cl_report)

# 結果を保存する
joblib.dump(clf, "./result/svm.pkl")
