import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import StandardScaler
import joblib

datos = pd.read_csv('Sujeto11_Features.csv')
datos = datos.astype(float).fillna(0.0)


X = datos.iloc[:, :-1].values
y = datos.iloc[:, -1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 42)
# print(X_train)
# print(y_train)
# print(X_test)
# print(y_test)

# from sklearn.preprocessing import StandardScaler
# svm = StandardScaler()
# X_train = svm.fit_transform(X_train)
# joblib.dump(svm, 'Sujeto10_sc.pkl')
# X_test = svm.transform(X_test)

print(X_test)

# from sklearn.preprocessing import MinMaxScaler
# scaler = MinMaxScaler(feature_range = (0, 1))
# scaler.fit(X_train)
# joblib.dump(scaler, 'Sujeto11_MM.pkl')
# X_train = scaler.transform(X_train)
# X_test = scaler.transform(X_test)

print(X_test)
from sklearn.svm import SVC
classifier = SVC(kernel = 'linear', random_state = 0)
classifier.fit(X_train, y_train)

# joblib.dump(svm, 'Sujeto10_sc.pkl')
joblib.dump(classifier, 'Sujeto11_ModeloSVM.pkl') # Guardo el modelo.
# print(classifier.predict(PB))

y_pred = classifier.predict(X_test)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))

from sklearn.metrics import confusion_matrix, accuracy_score
cm = confusion_matrix(y_test, y_pred)
print(cm)
accuracy_score(y_test, y_pred)
print(classification_report(y_test, y_pred))

# x  = [3.05485290e-05 ,8.02986342e+00, 3.47483813e+01, 4.01795118e+01, 3.96021112e+01 ,4.24010928e+01 ,4.86856074e+01, 7.23178590e+01 ,1.54897030e+02, 1.23464346e+02 ,5.12137103e-05, 1.34781646e+01, 6.01003923e+01, 8.21221485e+01 ,7.58047731e+01 ,8.24478424e+01, 9.32179037e+01, 1.00063197e+02, 1.32120258e+02, 1.24785644e+02 ,6.46910025e-05, 1.91659128e+01, 9.91671937e+01, 1.24038280e+02 ,1.22189815e+02, 1.12304253e+02 ,1.08029301e+02 ,9.75583110e+01 ,9.61872763e+01, 1.00608096e+02]
# x = np.reshape(x,(1,30), order='F')
# prueba2 = classifier.predict(x)
# print(prueba2)
# x1 = [3.504095970948552e-05, 8.550196844439165, 33.907764295456396, 38.688842508811305, 35.45710989218757, 36.10884742934351, 37.763588104360004, 39.87258883003649, 40.47026982086439, 40.748839671965975, 8.535618390772115e-05, 22.692201576321818, 101.00567712628448, 168.25366282760805, 188.93907965268193, 214.62376050504724, 264.86743175783386, 340.9649272155947, 377.8668516963613, 368.03450270711687, 4.312733502705911e-05, 15.068215068837452, 82.55845459980132, 99.66408079041594, 102.84136062534574, 102.28413705735376, 96.2740712161827, 102.38289381872072, 132.4560824040716, 128.06422443268454]
# x1 = np.reshape(x1,(1,30), order='F')
# prueba2 = classifier.predict(x1)
# print(prueba2)
# x2 = [2.425912595272075e-05, 8.411514829914582, 33.2795820676645, 41.281390438405445, 36.453272284084555, 39.40883027206325, 41.62772050260759, 43.121499130697025, 46.729545724343104, 52.78381393180698, 6.199554410139747e-05, 19.67857713279445, 92.77942214733304, 150.5894791345209, 167.54467411563388, 165.56511323336522, 175.6820259566078, 160.27348482165675, 162.94582659130046, 189.54396292559548, 3.683793200227966e-05, 11.969447760259293, 59.35058740349246, 113.6597395043447, 111.64868327394838, 104.0203360779929, 123.04404022589536, 133.45211994781954, 142.0881503310636, 173.4513712038945]
# x2 = np.reshape(x2,(1,30), order='F')
# prueba2 = classifier.predict(x2)
# print(prueba2)

# PB_1 = [-3.4851,	1.0402,	-1.8349,	0.42076,	3.0821,	4.2472	,12.648,	39.167,	53.394	,6.2304	,3.9023,	3.833,	13.672,	42.949,	36.985,	25.324,	21.911,	43.825,	54.349,	14.591	,-5.4214,	9.3531,	8.2975,	29.757,	30.243,	37.955,	44.132	,39.958	,41.574,	21.254]
# PB_1 = np.reshape(PB_1,(1,30), order='F')
# prueba_1 = classifier.predict(PB_1)
# print(prueba_1)
#
# PB1 = [2.9257	,-0.62119	,3.8172	,-1.1847,	1.8394	,2.367,	1.9158,	6.4993,	2.0608	,6.9409,	4.0255,	20.434,	65.735,	151.06	,181.66,	186.15,	212.93,	246.02	,229.77,	116.05	,5.1866,	-3.8118,	28.817,	52.646,	77.275,	74.334,	75.497,	123.49	,162.63,	92.064]
# # print(PB)
# PB1 = np.reshape(PB1,(1,30), order='F')
# prueba1 = classifier.predict(PB1)
# print(prueba1)
# PB2 = [[3.77364181e-05 ,1.07732272e+01, 3.89728130e+01 ,4.48269551e+01,
#   4.54248986e+01, 4.99086558e+01, 7.00977488e+01, 1.18713781e+02,
#   1.25445731e+02, 5.07663753e+01, 9.79349900e-05 ,2.42135515e+01,
#   1.06500566e+02, 1.62392123e+02 ,1.35205277e+02, 1.07773352e+02,
#   1.19378582e+02 ,1.35567219e+02, 1.31839187e+02 ,1.11110791e+02,
#   7.81682947e-05, 2.67161471e+01, 1.05514404e+02, 1.10714431e+02,
#   1.07450378e+02, 1.06570861e+02 ,1.18002063e+02, 1.11808119e+02,
#   1.12448173e+02 ,9.53135195e+01]]
# PB2 = np.reshape(PB2,(1,30), order='F')
# prueba2 = classifier.predict(PB2)
# print(prueba2)
#
# PB1 = [2.9650042831103138e-05, 9.991253301693366, 37.67329752701599, 42.57927810626147, 41.3846748713835, 44.03303649989166, 54.24344728781896, 96.99208397126627, 140.3605585562771, 72.72667633819623, 0.00018508814615779534, 47.34937395007468, 174.29878477971275, 185.29185567280493, 144.9643310639709, 135.74478557527516, 138.24518879561847, 141.86926257774402, 169.9187560061942, 146.36686356175406, 5.8401599515809215e-05, 24.18511759030235, 95.77944178148279, 94.9298459920186, 92.15371708393205, 96.11958484460885, 95.26887672199736, 112.84181227942089, 112.98124160668078, 95.05988166250106]
# # PB1 = np.reshape(PB1,(1,30), order='F')
# prueba1 = classifier.predict(PB1)
# print(prueba1)

# PB2 = [[2.51576121e-05, 8.28479003e+00, 3.49276147e+01 ,3.94105838e+01,
#   4.03651693e+01 ,4.41541065e+01, 7.77990621e+01, 1.34553851e+02,
#   8.32300030e+01 ,2.66856101e+01, 7.99652670e-05 ,2.26478775e+01,
#   1.03024775e+02, 1.47578149e+02, 1.24821576e+02, 1.04526508e+02,
#   1.17494324e+02 ,1.41683083e+02, 1.23238438e+02 ,1.11034225e+02,
#   5.48076549e-05 ,1.80223275e+01, 8.64237657e+01 ,1.02286412e+02,
#   9.87877807e+01 ,9.35526360e+01, 1.14865841e+02, 1.21976428e+02,
#   1.09479586e+02 ,9.49590478e+01]]
# PB2 = np.reshape(PB2,(1,30), order='F')
# prueba2 = classifier.predict(PB2)
# print(prueba2)
#
# PB3 = [[2.78530705e-05 ,8.35994814e+00, 3.36299655e+01 ,3.86506079e+01,
#   3.63553566e+01, 3.87952789e+01, 4.12205159e+01 ,4.04942237e+01,
#   4.19687439e+01, 3.78309022e+01, 1.24889574e-04 ,3.59935739e+01,
#   1.86666631e+02 ,2.70603545e+02 ,2.61319237e+02 ,2.98308142e+02,
#   3.33498944e+02, 3.08047803e+02, 2.26724899e+02, 1.91459510e+02,
#   6.46910025e-05 ,2.37834633e+01 ,9.15160730e+01 ,1.12728528e+02,
#   1.17068215e+02 ,1.25855214e+02, 1.46840658e+02, 1.59541130e+02,
#   1.28406258e+02, 9.97235359e+01]]
# PB3 = np.reshape(PB3,(1,30), order='F')
# prueba3 = classifier.predict(PB3)
# print(prueba3)






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
# plt.title('SVM (Training set)')
# plt.xlabel('Age')
# plt.ylabel('Estimated Salary')
# plt.legend()
# plt.show()
#
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
# plt.title('SVM (Test set)')
# plt.xlabel('Age')
# plt.ylabel('Estimated Salary')
# plt.legend()
# plt.show()
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
#
# sc = StandardScaler()
# X_train_array = sc.fit_transform(X_train.values)
# X_train = pd.DataFrame(X_train_array, index=X_train.index, columns=X_train.columns)
# X_test_array = sc.transform(X_test.values)
# X_test = pd.DataFrame(X_test_array, index=X_test.index, columns=X_test.columns)
#
# clf = SVC(kernel='poly')
# clf.fit(X_train, y_train)
#
# joblib.dump(clf, 'modelo_entrenado_Ismael.pkl') # Guardo el modelo.
#
# y_pred = clf.predict(X_test)
#
# # print(X_test)
# print(PB)
#
# # print(confusion_matrix(y_test, y_pred))
# print(classification_report(y_test, y_pred))
# print(y_pred)
# print(X_test)
# print(clf.score(X_test,y_test))