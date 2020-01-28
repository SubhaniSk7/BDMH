#!/usr/bin/env python
# coding: utf-8

# ### importing

# In[28]:


import pandas as pd
import numpy as np

from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, matthews_corrcoef
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import RandomForestClassifier


# ### Methods

# In[29]:


def printMetrics(y_test,y_pred):
    tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
    print('Accuracy score:', accuracy_score(y_test, y_pred), '\t|\tSpecificity:', tn/(tn+fp),'\nSensitivity:', tp/(tp+fn), '\t|\tMCC:', matthews_corrcoef(y_test, y_pred),'\n')


# In[30]:


def pFeatures(sequence):
    sequence = sequence.strip('\n')
    use_list = ['A','C','D','E','F','G','H','I','K','L','M','N','P','Q','R','S','T','V','W','Y']
    result = []
    for i in use_list:
        x = list(sequence).count(i)/len(sequence)*100
        result.append(x)
    return result


# ### Loading and reading files

# In[31]:


f = open('data/4/pos.txt','r')
lines = f.readlines()
pos = np.array(pFeatures(lines[0]))
if(len(lines)>1):
    for i in range(1,len(lines)):
        pos = np.vstack((pos,np.array(pFeatures(lines[i]))))


# In[32]:


f = open('data/4/neg.txt','r')
lines = f.readlines()
neg = np.array(pFeatures(lines[0]))
if(len(lines)>1):
    for i in range(1,len(lines)):
        neg = np.vstack((neg,np.array(pFeatures(lines[i]))))


# ### pos and neg samples

# In[33]:


pos,neg= np.insert(pos,20,1,axis=1), np.insert(neg,20,0,axis=1)


# In[34]:


data = np.concatenate((pos,neg), axis=0)


# In[35]:


X, y = data[:,0:19], data[:,20]


# ### splitting

# In[36]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=29)


# ## Models

# ### SVM

# In[37]:


print ('\nSVM model Results')
svc_model = SVC(gamma='auto', kernel='linear')
svc_model.fit(X_train, y_train)
printMetrics(y_test, svc_model.predict(X_test))


# ### Artificial Neural Network(ANN)

# In[38]:


print ('\nANN model Results')
mlp_model = MLPClassifier(max_iter=400)
mlp_model.fit(X_train, y_train)
printMetrics(y_test,mlp_model.predict(X_test))


# ### Random Forest

# In[39]:


print ('\nRandom Forest model Results')
rfc = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=0)
rfc.fit(X_train, y_train)
printMetrics(y_test,rfc.predict(X_test))