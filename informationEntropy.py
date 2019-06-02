# -*- coding:utf-8 -*-
import pandas as pd
import pydotplus
from math import log
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_graphviz

from sklearn.metrics import classification_report, confusion_matrix

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

f = open('NHIS_OPEN_GJ_2017.csv', 'r')
features = f.readline().replace("\n", "").split(',')
print(features)
line = True
data = []
line = list(map(float, f.readline().replace("\n", "").split(',')))
print(line)
cnt = 0
for x in range(1000000):

    data.append(line)
    tmp  =f.readline().replace("\n", "").split(',')
    try:
        line = list(map(float, tmp))
    except:
        continue
a = np.array(data)
alcohol = a[:, len(features) - 1:]
healthData = a[:, :len(features) - 1]
tv = []
for x in alcohol:
    tv.append(int(x[0]))
print(healthData)
cigar = np.array(tv)
print(cigar)
health_pd = pd.DataFrame(data=np.c_[healthData, cigar],columns=features)

train_set, test_set = train_test_split(health_pd, test_size=0.2, random_state=42)
tree_clf = DecisionTreeClassifier(criterion='entropy', max_depth=10) # 6이 최대, 3이 가장 잘나옴

featureStartNumber = 0
featureEndNumber = 22
trainFeatures = list(train_set.columns[featureStartNumber:featureEndNumber])  # 학습시킬 feature 22개, 0 : 22
print(trainFeatures)
cnt = 0.0
#for train_el in train_set['flavanoids']:
#    if train_el <= 1.4:
#        cnt += 1
#print(-((45.0/142.0)*log(45.0/142.0, 2) + (57.0/142.0)*log(57.0/142.0, 2) + (40.0/142.0) * log(40.0/142.0, 2)))
#print(-((8.0/48.0) * log(8.0 /48.0, 2) + (40.0/48.0) * log(40.0/48.0, 2)))
X = train_set[features[featureStartNumber:featureEndNumber]]
y = train_set[features[-1]]
tree_clf.fit(X, y)

# https://datascienceschool.net/view-notebook/16c28c8c192147bfb3d4059474209e0a/
# http://dataaspirant.com/2017/04/21/visualize-decision-tree-python-graphviz/
# https://scikit-learn.org/stable/modules/tree.html
dot_data = export_graphviz(tree_clf, out_file=None,
                           feature_names=features[featureStartNumber:featureEndNumber],
                           class_names = ['never', 'drink all day'],
                           filled=True, rounded=True,
                           special_characters=True)
#graph = graphviz.Source(dot_data)
graph = pydotplus.graph_from_dot_data(dot_data)
graph.write_png('tree.png')

X_test = test_set[features[featureStartNumber:featureEndNumber]]
y_test = test_set[features[-1]]
y_pred = tree_clf.predict(X_test)

# https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html
# precision : tp / (tp + fp)  - 참일 때 실제로 참
# recall : tp / (tp + fn)
# f1-score : (precision + recall) / 2
# support : The support is the number of occurrences of each class in y_true.
# https://datascience.stackexchange.com/questions/15989/micro-average-vs-macro-average-performance-in-a-multiclass-classification-settin (micro avg, macro avg)
print(classification_report(y_test, y_pred))
