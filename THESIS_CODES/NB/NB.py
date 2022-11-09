# # Naive Bayes
#
# # Importing the libraries
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
#
from sklearn.metrics import classification_report, confusion_matrix
# Importing the dataset
import joblib
#
#
# datos = pd.read_csv('Sujeto9_Features.csv')
# datos = datos.astype(float).fillna(0.0)
#
#
# X = datos.iloc[:, :-1].values
# y = datos.iloc[:, -1].values
# # Splitting the dataset into the Training set and Test set
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 42)
# # print(X_train)
# # print(y_train)
# # print(X_test)
# # print(y_test)
#
# # Feature Scaling
# # from sklearn.preprocessing import StandardScaler
# # nb = StandardScaler()
# # X_train = nb.fit_transform(X_train)
# # X_test = nb.transform(X_test)
# # print(X_train)
# # print(X_test)
#
# # Training the Naive Bayes model on the Training set
# from sklearn.naive_bayes import GaussianNB
# clf = GaussianNB()
# clf.fit(X_train, y_train)
#
#
# joblib.dump(clf, 'Sujeto9_ModeloNB.pkl')######################################
# # Predicting the Test set results
# y_pred = clf.predict(X_test)
# print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))
#
# # x =[[-1.27280171e+01 ,-8.98867589e+00,  3.87356139e+00 , 5.70547474e+00,
# #    4.08704516e+00  ,2.41692573e+00  ,3.61338441e-01 ,-4.35368546e-01,
# #   -4.84130618e-01 ,-1.50567967e-01 ,-8.15718338e+00 ,-4.59286031e+00,
# #   -1.05132476e+00 ,-5.81837377e-01 ,-4.34405272e-01 , 4.93540932e-01,
# #    7.70854178e-01 , 1.22912141e-01 ,-4.72121891e-01 , 3.58744805e-02,
# #   -1.00198910e+01 ,-4.98412298e+00 , 3.86601543e-01 , 1.12301724e+00,
# #    5.01341802e-03 , 8.38532237e-02 , 5.31330042e-01 ,-5.36845863e-01,
# #   -9.36168623e-01 ,-6.24851773e-01]]
# # # x = [1.34772922e-05, 3.15845243e+00, 1.64848143e+01 ,1.94478561e+01 ,1.95645351e+01, 1.96898801e+01 ,2.01894248e+01 ,1.96304951e+01, 1.83678327e+01, 2.03295984e+01, 4.94167381e-05 ,1.85308703e+01, 1.02749240e+02 ,1.59729373e+02, 1.87326599e+02, 2.38114453e+02 ,2.51583546e+02 ,2.59257761e+02, 2.64206476e+02 ,2.28155107e+02, 8.08637532e-05, 1.89030467e+01, 8.69968713e+01, 1.14927190e+02 ,1.23223733e+02 ,1.19677147e+02, 1.27712009e+02 ,1.67234970e+02 ,1.30549252e+02, 1.02874547e+02]
# # # x = np.reshape(x,(1,30), order='F')
# # z = clf.predict(x)
# # print("X",z)
#
# # Making the Confusion Matrix
# from sklearn.metrics import confusion_matrix, accuracy_score
# cm = confusion_matrix(y_test, y_pred)
# print(cm)
# accuracy_score(y_test, y_pred)
# # accuracy_score(y_test, y_pred)
# print(classification_report(y_test, y_pred))
# Naive Bayes

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Sujeto8_Features.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

# Feature Scaling
# from sklearn.preprocessing import StandardScaler
# sc = StandardScaler()
# X_train = sc.fit_transform(X_train)
# X_test = sc.transform(X_test)
# print(X_train)
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range = (0, 1))
scaler.fit(X_train)
joblib.dump(scaler, 'Sujeto8_MM.pkl')
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)
# print(X_test)

# Training the Naive Bayes model on the Training set
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
clf.fit(X_train, y_train)

joblib.dump(clf, 'Sujeto8_ModeloNB.pkl')
# Predicting a new result
# print(classifier.predict(sc.transform([[30,87000]])))

# Predicting the Test set results
y_pred = clf.predict(X_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)

# Making the Confusion Matrix
# from sklearn.metrics import confusion_matrix, accuracy_score
# cm = confusion_matrix(y_test, y_pred)
# print(cm)
# accuracy_score(y_test, y_pred)
# accuracy_score(y_test, y_pred)
print(classification_report(y_test, y_pred))
# Visualising the Training set results
# from matplotlib.colors import ListedColormap
# X_set, y_set = sc.inverse_transform(X_train), y_train
# X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 10, stop = X_set[:, 0].max() + 10, step = 0.25),
#                      np.arange(start = X_set[:, 1].min() - 1000, stop = X_set[:, 1].max() + 1000, step = 0.25))
# plt.contourf(X1, X2, classifier.predict(sc.transform(np.array([X1.ravel(), X2.ravel()]).T)).reshape(X1.shape),
#              alpha = 0.75, cmap = ListedColormap(('red', 'green')))
# plt.xlim(X1.min(), X1.max())
# plt.ylim(X2.min(), X2.max())
# for i, j in enumerate(np.unique(y_set)):
#     plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1], c = ListedColormap(('red', 'green'))(i), label = j)
# plt.title('Naive Bayes (Training set)')
# plt.xlabel('Age')
# plt.ylabel('Estimated Salary')
# plt.legend()
# plt.show()
#
# # Visualising the Test set results
# from matplotlib.colors import ListedColormap
# X_set, y_set = sc.inverse_transform(X_test), y_test
# X1, X2 = np.meshgrid(np.arange(start = X_set[:, 0].min() - 10, stop = X_set[:, 0].max() + 10, step = 0.25),
#                      np.arange(start = X_set[:, 1].min() - 1000, stop = X_set[:, 1].max() + 1000, step = 0.25))
# plt.contourf(X1, X2, classifier.predict(sc.transform(np.array([X1.ravel(), X2.ravel()]).T)).reshape(X1.shape),
#              alpha = 0.75, cmap = ListedColormap(('red', 'green')))
# plt.xlim(X1.min(), X1.max())
# plt.ylim(X2.min(), X2.max())
# for i, j in enumerate(np.unique(y_set)):
#     plt.scatter(X_set[y_set == j, 0], X_set[y_set == j, 1], c = ListedColormap(('red', 'green'))(i), label = j)
# plt.title('Naive Bayes (Test set)')
# plt.xlabel('Age')
# plt.ylabel('Estimated Salary')
# plt.legend()
# plt.show()