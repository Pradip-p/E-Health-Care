import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split
# from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import pickle
import os
from sklearn import preprocessing 

def pre_processing(df):
    # df = df.drop(df.columns[[4, 5, 6,7,8,9,10,11,12,13,14,15,16,17]], axis=1) 
    df['Symptom_1'] = df['Symptom_1'].str.strip()
    df['Symptom_2'] = df['Symptom_2'].str.strip()
    df['Symptom_3'] = df['Symptom_3'].str.strip()
    data={'itching':0, 'skin_rash':1, 'continuous_sneezing':2, 'shivering':3, 'stomach_pain':4,
    'acidity':5, 'vomiting':6, 'indigestion':7, 'muscle_wasting':8, 'patches_in_throat':9,
    'fatigue':10, 'weight_loss':11, 'sunken_eyes':12, 'cough':13, 'headache':14, 'chest_pain':15,
    'back_pain':16, 'weakness_in_limbs':17, 'chills':18, 'joint_pain':19, 'yellowish_skin':20,
    'constipation':21, 'pain_during_bowel_movements':22, 'breathlessness':23, 'cramps':24,
    'weight_gain':25, 'mood_swings':26, 'neck_pain':27, 'muscle_weakness':28, 'stiff_neck':29,
    'pus_filled_pimples':30, 'burning_micturition':31, 'bladder_discomfort':32,
    'high_fever':33}
    print("*"*50)

    data1={'skin_rash':1, 'nodal_skin_eruptions':2, 'shivering':3, 'chills':18, 'acidity':5,
        'ulcers_on_tongue':35, 'vomiting':6, 'yellowish_skin':20,'stomach_pain':4,
        'loss_of_appetite':36, 'indigestion':7, 'patches_in_throat':9, 'high_fever':34,
        'weight_loss':11, 'restlessness':37, 'sunken_eyes':12, 'dehydration':38, 'cough':13,
        'chest_pain':15,'dizziness':39,'headache':14, 'weakness_in_limbs':17,  'neck_pain':27,
        'weakness_of_one_body_side':40 ,'fatigue':10,  'joint_pain':19, 'lethargy':41,
        'nausea':42 ,'abdominal_pain':43, 'pain_during_bowel_movements':22,
        'pain_in_anal_region':44,  'breathlessness':23, 'sweating':45,'cramps':24,
        'bruising':46,'weight_gain':25,'cold_hands_and_feets':47, 'mood_swings':26,
        'anxiety':48,'knee_pain':49,'stiff_neck':29, 'swelling_joints':50,
        'pus_filled_pimples':30, 'blackheads':51 ,'bladder_discomfort':32,
        'foul_smell_of urine':52, 'skin_peeling':53, 'blister':54
        }
    data2={'nodal_skin_eruptions':2, 'dischromic _patches':55 ,'chills':18,
    'watering_from_eyes':56, 'ulcers_on_tongue':35 ,'vomiting':6, 'yellowish_skin':20,
    'nausea':42, 'stomach_pain':4, 'burning_micturition':31, 'abdominal_pain':43,
    'loss_of_appetite':36, 'high_fever':34, 'extra_marital_contacts':57, 'restlessness':37,
    'lethargy':41, 'dehydration':38, 'diarrhoea':58, 'breathlessness':23, 'dizziness':39,
    'loss_of_balance':58, 'headache':14, 'blurred_and_distorted_vision':59, 'neck_pain':27,
    'weakness_of_one_body_side':40, 'altered_sensorium':59, 'fatigue':10, 'weight_loss':11,
    'sweating':45, 'joint_pain':19, 'dark_urine':60, 'swelling_of_stomach':61, 'cough':13,
    'pain_in_anal_region':44, 'bloody_stool':62, 'chest_pain':15, 'bruising':46, 'obesity':63,
    'cold_hands_and_feets':47, 'mood_swings':26, 'anxiety':48, 'knee_pain':49,
    'hip_joint_pain':63, 'swelling_joints':50, 'movement_stiffness':64,
    'spinning_movements':65, 'blackheads':51, 'scurring':66, 'foul_smell_of urine':52,
    'continuous_feel_of_urine':67, 'skin_peeling':53, 'silver_like_dusting':68, 'blister':54,
    'red_sore_around_nose':69}
    print("*"*50)
    df["Symptom_1"].replace(data, inplace=True)
    df["Symptom_2"].replace(data1, inplace=True)
    df["Symptom_3"].replace(data2, inplace=True)
    return df

def training():
    df=pd.read_csv("dataset.csv")
    df=pre_processing(df)
    y=df[["Disease"]]
    df.drop("Disease", axis="columns", inplace=True)
    x=df
    print("#"*50)
    print(x)
    dummyRow=pd.DataFrame(np.zeros(len(x.columns)).reshape(1,len(x.columns)), columns=x.columns)
    dummyRow.to_csv('dummyRow.csv', index=False)
    model=RandomForestClassifier(random_state=2)
    # model=XGBClassifier(max_depth=2,min_child_weight=3, gamma=0,subsample=0.86, reg_alpha=0, n_estimators=125)
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2, random_state=5)
    model.fit(x,y)
    print("#"*50)
    print(model)
    print("#"*50)
    print(model.score(x_test,y_test))
    pkl_filename="pickle_model.pkl"
    with open(pkl_filename,'wb') as file:
        pickle.dump(model,file)
        print(pkl_filename)
    # yp=model.predict(x_test)
    # print("Survived", sum(yp!=0)) 
    # print("not Survived ", sum(yp==0))
    # accuracy_score(y_test,yp)
    # cm=confusion_matrix(y_test, yp)
    # #import seaborn as sn
    # #sn.heatmap(cm,annot=True)
    # print(cm)


def pred(ob):
    d1=ob.to_dict()
    df=pd.DataFrame(d1,index=[0])
    df=pre_processing(df)
    # df.drop("Disease", axis="columns", inplace=True)
    dummyRow_filename="dummyRow.csv"
    df2=pd.read_csv(dummyRow_filename)
    for c1 in df.columns:
        df2[c1]=df[c1]
        print(df2[c1])
    pkl_filename='pickle_model.pkl'
    with open(pkl_filename,'rb') as file:
        model=pickle.load(file)
    pred=model.predict(df2)
    return pred

if __name__=="__main__":
    training()#df



