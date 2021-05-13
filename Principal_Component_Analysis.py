import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn import preprocessing

with open('./bilibili.txt', 'r+',encoding='utf-8') as f:
    lst=[]
    for line in f.readlines():
        lst.append(line.split(','))
X = np.array([[int(i[4]),int(i[8]),int(i[9]),int(i[10]),int(i[11]),int(i[12])] for i in lst[0:50:]])
X_df = pd.DataFrame(X)
scaler = preprocessing.MinMaxScaler().fit(X_df)
X_scaler = pd.DataFrame(scaler.transform(X_df))
# 主成分分析建模
pca = PCA(n_components=None)  # n_components提取因子数量，None，返回所有主成分
pca.fit(X_scaler)
pca.explained_variance_  # 贡献方差，即特征根
pca.explained_variance_ratio_  # 方差贡献率
pca.components_  # 成分矩阵
k1_spss = pca.components_ / np.sqrt(pca.explained_variance_.reshape(-1, 1))  # 成分得分系数矩阵
# 确定权重
# 求指标在不同主成分线性组合中的系数
j = 0
Weights = []
for j in range(len(k1_spss)):
    for i in range(len(pca.explained_variance_)):
        Weights_coefficient = np.sum(100 * (pca.explained_variance_ratio_[i]) * (k1_spss[i][j])) / np.sum(
            pca.explained_variance_ratio_)
    j = j + 1
    Weights.append(np.float(Weights_coefficient))
print('Weights',Weights)
# 权重结果进行归一化
Weights=pd.DataFrame(Weights)
Weights1 = preprocessing.MinMaxScaler().fit(Weights)
Weights2 = Weights1.transform(Weights)
print(Weights2)
