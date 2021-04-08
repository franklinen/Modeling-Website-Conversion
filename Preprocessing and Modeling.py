# PreProcessing
# #### check missing values for each column
df.isnull().sum().sort_values(ascending=False)
df.head()
df['transactions'] = df['transactions'].fillna(0)
df['transactionRevenue'] = df['transactionRevenue'].fillna(0)
df['bounces'] = df['bounces'].fillna(0)
df['timeOnSite'] = df['timeOnSite'].fillna(0)
df['pageviews'].fillna(int(df['pageviews'].mean()), inplace=True)
df.isnull().sum().sort_values(ascending=False)
# Feature engineering
df['conversion'] = np.where(df.transactions > 0, 1, 0)  # create a new column to show if there is conversion from the web visit and session.
df.conversion.value_counts()
df.shape
df = df.drop(['fullVisitorID'], axis=1)  # Drop a column. The index column is not useful in the analysis.column is an index column and is not useful in the analysis
#Mapping of categorical variables
df.deviceCategory = df.deviceCategory.map({'desktop':0,'mobile':1, 'tablet':2})
# Label encode categorical variables
from sklearn.preprocessing import LabelEncoder
lb = LabelEncoder()
df['source'] = lb.fit_transform(df['source'])
df['browser'] = lb.fit_transform(df['browser'])
df['country'] = lb.fit_transform(df['country'])
df['city'] = lb.fit_transform(df['city'])
df['channelGrouping'] = lb.fit_transform(df['channelGrouping'])
df.head(n=5)
#split data into X and Y
X=df.drop(['conversion'],axis=1)
y=df.conversion
#Use Pearson Correlation to drop features from the X independent variables
plt.figure(figsize=(12,10))
cor = X.corr()
sns.heatmap(cor, annot=True, cmap=plt.cm.CMRmap_r)
plt.show()
#with the following function we select highly correlated features and remove the first feature that is correlated with any other feature
def correlation(dataset, threshold):
    col_corr = set()  # Set of all the names of correlated columns
    corr_matrix = dataset.corr()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if abs(corr_matrix.iloc[i, j]) > threshold: # we are interested in absolute coeff value
                colname = corr_matrix.columns[i]  # getting the name of column
                col_corr.add(colname)
    return col_corr

corr_features = correlation(X, 0.70)
len(set(corr_features))

corr_features
X = X.drop(corr_features,axis=1)
#import normalisation package for scaling and sacle the independent variables
sc = StandardScaler()
X = sc.fit_transform(X)
#split train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
X_train.shape, X_test.shape
#import ClassifiersGridSearchCV
LogR = LogisticRegression()
RanR = RandomForestClassifier()
svC = SVC(kernel='rbf')
#train our classifier
LogR.fit(X_train,y_train)
RanR.fit(X_train,y_train)
svC.fit(X_train,y_train)
#predictions for test
y_pred1 = LogR.predict(X_test)
y_pred2 = RanR.predict(X_test)
y_pred3 = svC.predict(X_test)
# Model Evaluation
#check accuracy. Classifier performance on test
print(LogR.score(X_test,y_test))
print(RanR.score(X_test,y_test))
print(svC.score(X_test,y_test))
#import performance measure tools and check confusion matrix
cm1 = confusion_matrix(y_test,y_pred1)
cm2 = confusion_matrix(y_test,y_pred2)
cm3 = confusion_matrix(y_test,y_pred3)

print(classification_report(y_test,y_pred1))
print(classification_report(y_test,y_pred2))
print(classification_report(y_test,y_pred3))
#check Gridsearch for RanR = RandomForest
param_dict= {'n_estimators':range(2,10), 'max_depth':range(1,10)}
model = GridSearchCV(RanR,param_dict)
model.fit(X_train,y_train)

model.score(X_test,y_test)
model.best_params_






