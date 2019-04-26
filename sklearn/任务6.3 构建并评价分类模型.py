import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

# 使用sklearn估计器构建SVM模型
cancer = load_breast_cancer()
cancer_data = cancer['data']
cancer_target = cancer['target']
cancer_names = cancer['feature_names']
# 划分训练集和测试集
cancer_data_train, cancer_data_test, cancer_target_train, cancer_target_test = train_test_split(cancer_data,
                                                                                                cancer_target,
                                                                                                test_size=0.2,
                                                                                                random_state=22)
# 数据标准化
stdScaler = StandardScaler().fit(cancer_data_train)
cancer_trainStd = stdScaler.transform(cancer_data_train)
cancer_testStd = stdScaler.transform(cancer_data_test)
# 建立SVM模型
svm = SVC().fit(cancer_trainStd, cancer_target_train)
print('建立的SVM模型为:\n', svm)

# 预测训练集结果
cancer_target_pred = svm.predict(cancer_testStd)
print('预测前20个结果为:\n', cancer_target_pred[:20])

# 分类结果的混淆矩阵与准确率
# 求出预测和真实一样的数目
true = np.sum(cancer_target_pred == cancer_target_test)
print('预测对的数目为:\n', true)
print('预测错的数目为:\n', cancer_target_test.shape[0] - true)
print('预测结果的准确率为:\n', true / cancer_target_test.shape[0])

# 评价分类模型
# ①
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, cohen_kappa_score

print('准确率:', accuracy_score(cancer_target_test, cancer_target_pred))
print('精确率:', precision_score(cancer_target_test, cancer_target_pred))  # 要注意区分精确率和准确率
print('召回率:', recall_score(cancer_target_test, cancer_target_pred))
print('F1值：', f1_score(cancer_target_test, cancer_target_pred))
print('CK系数:', cohen_kappa_score(cancer_target_test, cancer_target_pred))
# ②
from sklearn.metrics import classification_report

print('分类报告:', classification_report(cancer_target_test, cancer_target_pred))

# ③绘制ROC曲线
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt

fpr, tpr, thresholds = roc_curve(cancer_target_test, cancer_target_pred)
plt.figure(figsize=(10, 6))
plt.xlim(0, 1)
plt.ylim(0.0, 1.1)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.plot(fpr, tpr, linewidth=2, linestyle='-', color='red')
plt.show()
