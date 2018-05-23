import numpy as np
import csv
import os
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import cross_val_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline

data_folder = "E:\Study\Python\scikit-learn"
data_filename = os.path.join(data_folder,"ionosphere.data")
estimator = KNeighborsClassifier()

x = np.zeros((351,34), dtype = 'float')
y = np.zeros((351,), dtype = 'bool')

with open(data_filename,'r') as input_file:
    reader = csv.reader(input_file)
    for i, row in enumerate(reader):
        data = [float(datum) for datum in row[:-1]]
        x[i] = data
        y[i] = row[-1]=='g'
    # print(y)

x_train, x_test , y_train, y_test = train_test_split(x, y, random_state = 14)  
estimator.fit(x_train, y_train)
y_predicted = estimator.predict(x_test)
accuracy = np.mean(y_test == y_predicted)*100
print("The accuracy is {0:.01f}%".format(accuracy))

scores = cross_val_score(estimator, x, y, scoring='accuracy')
average_accuracy = np.mean(scores)*100
print("the average accuracy is {:.2f}%".format(average_accuracy))

avg_scores = []
all_scores = []

par_val = list(range(1,21))
for n_neighbors in par_val:
    estimator = KNeighborsClassifier(n_neighbors = n_neighbors)
    scores = cross_val_score(estimator, x, y, scoring='accuracy')
    avg_scores.append(np.mean(scores))
    all_scores.append(scores)

#from matplotlib import pyplot as plt
#plt.plot(par_val, avg_scores,'-o')
#plt.show()

x_broken = np.array(x)
x_broken[:,::2]/=10

broken_scores = cross_val_score(estimator, x_broken, y, scoring = 'accuracy')
broken_avg = np.mean(broken_scores)*100
print("The average accuracy in aletered array is {:.2f}".format(broken_avg))

x_transform = MinMaxScaler().fit_transform(x)
scr_t = cross_val_score(estimator, x_transform, y, scoring = 'accuracy')
avg_t = np.mean(scr_t)*100
print("the average accuracy in the transformed case is {:.2f}%".format(avg_t))







