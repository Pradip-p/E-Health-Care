import pickle
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score

def pre_processing(X):
    pass

def training():
    df = pd.read_csv("datasets/Diabetes.csv")
    y=df[["Outcome"]]
    df.drop("Outcome", axis="columns", inplace=True)
    X=df

    dummyRow_diabetes=pd.DataFrame(np.zeros(len(X.columns)).reshape(1,len(X.columns)), columns=X.columns)
    dummyRow_diabetes.to_csv('datasets/dummyRow_diabetes.csv', index=False)

    classifier = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)
    classifier.fit(X, y)


    pkl_filename="datasets/pickle_model_diabetes.pkl"
    with open(pkl_filename,'wb') as file:
        pickle.dump(classifier,file)
    y_pred = classifier.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    print(cm)
    print(accuracy_score(y_test, y_pred))

def pred_diabetes(ob):
    d1=ob.to_dict()
    df=pd.DataFrame(d1,index=[0])
    print("*"*8)
    print(df)
    dummyRow_filename="datasets/dummyRow_diabetes.csv"
    df2=pd.read_csv(dummyRow_filename)
    for c1 in df.columns:
        df2[c1]=df[c1]
        print(df2[c1])
    pkl_filename='datasets/pickle_model_diabetes.pkl'
    with open(pkl_filename,'rb') as file:
        classifier=pickle.load(file)
    pred=classifier.predict(df2)
    return pred


if __name__=="__main__":
    training()#df
