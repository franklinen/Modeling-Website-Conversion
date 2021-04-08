# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 11:04:32 2021

@author: MAIN
"""

#Libraries and environment
import os
os.chdir(r'C:\Users\MAIN\Desktop\Data Science intern File')
os.getcwd()

#import packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.interactive(False)
import seaborn as sns
plt.style.use("ggplot")
get_ipython().run_line_magic('matplotlib', 'inline')
from pylab import rcParams


from sklearn.preprocessing import LabelEncoder

from sklearn.preprocessing import StandardScaler

from sklearn.model_selection import train_test_split

#import Classifiers
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV

from sklearn.metrics import accuracy_score, f1_score, confusion_matrix, recall_score, precision_score

from sklearn.metrics import classification_report
