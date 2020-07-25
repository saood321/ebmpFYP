import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import pickle
def fun():
    data=pd.read_csv('distances.csv')
    X=data.drop(['Class'],axis=1)
    y=data['Class']
    X_train,X_test,y_train, y_test=train_test_split(X,y,test_size=0.30)
    classifier=svm.SVC(kernel='linear')
    model=classifier.fit(X_train,y_train)
    filename = 'landmarkModel_4.sav'
    pickle.dump(model, open(filename, 'wb'))
    y_pred=classifier.predict(X_test)
    abc=confusion_matrix(y_test,y_pred)
    print("Confusion Matrix")
    print(abc)
    print("Classification Report")
    print(classification_report(y_test,y_pred))
    diagonal_sum = abc.trace()
    sum_of_all_elements = abc.sum()
    print('Accuracy = ',(diagonal_sum / sum_of_all_elements)*100,'%')

fun()