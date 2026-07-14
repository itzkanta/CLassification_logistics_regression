import pandas as pd 
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
# print(pd.__version__)

df = pd.read_csv(r'C:\Users\Dell\OneDrive\Desktop\Data_science\classification_with_logistics\iris.csv')

df.head()
df.info()

# data preprocessing

print(df.isnull().sum())

# species

# from sklearn.datasets import load_iris

# iris = load_iris()

# print(iris.target[:5])

# df["species"] = iris.target 

# print(df.head())

# print(df.dtypes)


x = df.drop("species", axis=1)
y = df["species"]

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size = 0.2,
    random_state = 42
)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

model = LogisticRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

print(y_pred)

# for accuracy score
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)

# for precision score
precision = precision_score(y_test, y_pred, average = 'weighted')
print("Precision:",precision)

#for recall score
recall = recall_score(y_test,y_pred, average = 'weighted')
print("Recall:",recall)

#  for confusion matrix
cm = confusion_matrix(y_test,y_pred)
print("Confusion Matrix :\n",cm)

# for classification report
report = classification_report(y_test,y_pred)
print("Classification Report :\n",report)

# comparing with other models
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier()
rf.fit(x_train,y_train)
rf_pred = rf.predict(x_test)
print("Random Forest Accuracy : ",accuracy_score(y_test,rf_pred))

# svm
from sklearn.svm import SVC
svm = SVC()
svm.fit(x_train,y_train)
svm_pred = svm.predict(x_test)
print("SVM Accuracy : ",accuracy_score(y_test,svm_pred))