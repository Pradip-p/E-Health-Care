
import pickle
import os
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.model_selection import train_test_split


def pre_processing(X):
    sc = StandardScaler()
    X = sc.fit_transform(X)
    return X

    



def training():
    df=pd.read_csv("heart.csv")
    y=df[["target"]]
    df.drop("target", axis="columns", inplace=True)
    X=df
    # X = df.iloc[:, :-1].values
    # y = df.iloc[:, -1].values
    # X=pre_processing(X)


    dummyRow_heart=pd.DataFrame(np.zeros(len(X.columns)).reshape(1,len(X.columns)), columns=X.columns)
    dummyRow_heart.to_csv('dummyRow_heart.csv', index=False)

    classifier = KNeighborsClassifier(n_neighbors = 5, metric = 'minkowski', p = 2)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)
    classifier.fit(X_train, y_train)
    # print(model.score(x_test,y_test))
    pkl_filename="pickle_model_heart.pkl"
    with open(pkl_filename,'wb') as file:
        pickle.dump(classifier,file)
    
    y_pred = classifier.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    print(cm)
    print(accuracy_score(y_test, y_pred))


def pred(ob):
    d1=ob.to_dict()
    df=pd.DataFrame(d1,index=[0])
    # df=pre_processing(df)
    # df.drop("Disease", axis="columns", inplace=True)
    dummyRow_filename="dummyRow_heart.csv"
    df2=pd.read_csv(dummyRow_filename)
    for c1 in df.columns:
        df2[c1]=df[c1]
        print(df2[c1])
    pkl_filename='pickle_model_heart.pkl'
    with open(pkl_filename,'rb') as file:
        classifier=pickle.load(file)
    pred=classifier.predict(df2)
    return pred



if __name__=="__main__":
    training()#df








