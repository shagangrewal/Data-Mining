import pandas as pd
import numpy as np
import os
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from scipy.stats import pearsonr
from sklearn.tree import DecisionTreeClassifier
from sklearn.cross_validation import cross_val_score

def multivariate_pearsonr(x,y):
    scores, pvalues = [], []
    for column in range(x.shape[1]): #running each column in the x array on every iteration of the for loop
        cur_scr, cur_pval = pearsonr(x[:,column],y)
        scores.append(abs(cur_scr))
        pvalues.append(cur_pval)
    return (np.array(scores), np.array(pvalues))

data_folder = "E:\Study\Python\Adult"
adult_data = os.path.join(data_folder,"adult.data")

#loading the csv file using pandas
adult = pd.read_csv(adult_data, header=None, names = ["Age", "Work-Class", "fnlwgt","Education", "Education-Num","Marital-Status", "Occupation","Relationship", "Race", "Sex","Capital-gain", "Capital-loss","Hours-per-week", "Native-Country","Earnings-Raw"])

adult.dropna(how = "all", inplace = True)
#print(adult.columns) this tells all the different categories the dataset file contains
#cecking the various columns in the adult file which contains the extracted data

print(adult["Hours-per-week"].describe())

#creating a new feature, longhours, which have all users that work more than 40 hours
adult["Longhours"] = adult["Hours-per-week"]>40

x = adult[["Age", "Education-Num", "Capital-gain", "Capital-loss", "Hours-per-week"]].values
y = (adult["Earnings-Raw"] == ' >50K').values

transformer = SelectKBest(score_func = chi2, k=3)

#evaluating the transformed x, using the chi squarerd evalution method
xt = transformer.fit_transform(x,y)
print(transformer.scores_)

transformer = SelectKBest(score_func = multivariate_pearsonr, k=3)
xp = transformer.fit_transform(x,y)
print(transformer.scores_)

clsf = DecisionTreeClassifier(random_state = 14)
score_chi = cross_val_score(clsf, xt, y, scoring='accuracy')
score_pearsonr = cross_val_score(clsf, xp, y, scoring='accuracy')

print("Chi-squared: {:.2f}% and Pearsonr: {:.2f}%".format(score_chi.mean()*100,score_pearsonr.mean()*100))

