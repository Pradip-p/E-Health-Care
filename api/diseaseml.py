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
    
    df1 = df['value_1']
    df1 = df1.values.tolist()
    #second value
    df2 = df['value_2']
    df2 = df2.values.tolist()
    #third value
    df3 = df['value_3']
    df3 = df3.values.tolist()
    #4th value
    df4 = df['value_4']
    df4 = df4.values.tolist()
    #5th value
    df5 = df['value_5']
    df5 = df5.values.tolist()
    #6th value
    df6 = df['value_6']
    df6 = df6.values.tolist()
    print(df1,df2,df3,df4,df5,df6)

    #value_1 assign zero or one
    if 'receiving_blood_transfusion' in df1:
        receiving_blood_transfusion = 1
    else:
        receiving_blood_transfusion = 0

    
    if 'red_sore_around_nose' in df1:
        red_sore_around_nose = 1
    else:
        red_sore_around_nose = 0
    
    if 'abnormal_menstruation' in df1:
        abnormal_menstruation = 1
    else:
        abnormal_menstruation = 0
    
    if 'continuous_sneezing' in df1:
        continuous_sneezing = 1 
    else:
        continuous_sneezing = 0

    if 'breathlessness' in df1:
        breathlessness = 1
    else:
        breathlessness = 0

    if 'blackheads' in df1:
        blackheads = 1
    else:
        blackheads = 0

    if 'shivering' in df1:
        shivering = 1
    else:
        shivering = 0

    if 'dizziness' in df1:
        dizziness = 1
    else:
        dizziness = 0
    
    
    # value_2 assign zero or one
    if 'back_pain' in df2:
        back_pain = 1
    else:
        back_pain = 0
    if 'unsteadiness' in df2:
        unsteadiness = 1
    else:
        unsteadiness = 0
        
    if 'yellow_crust_ooze' in df2:
        yellow_crust_ooze = 1
    else:
        yellow_crust_ooze = 0
    if 'muscle_weakness' in df2:
        muscle_weakness = 1
    else:
        muscle_weakness = 0
    if 'loss_of_balance' in df2:
        loss_of_balance = 1
    else:
        loss_of_balance = 0
    if 'chills' in df2:
        chills = 1
    else:
        chills = 0
    if 'ulcers_on_tongue' in df2:
        ulcers_on_tongue = 1
    else:
        ulcers_on_tongue = 0
    if 'stomach_bleeding' in df2:
        stomach_bleeding = 1
    else:
        stomach_bleeding = 0

    #value_3 assign zero or one
    if 'lack_of_concentration' in df3:
        lack_of_concentration = 1
    else:
        lack_of_concentration = 0
    if 'coma' in df3:
        coma = 1
    else:
        coma = 0
        
    if 'neck_pain' in df3:
        neck_pain = 1
    else:
        neck_pain = 0   
    if 'weakness_of_one_body_side' in df3:
        weakness_of_one_body_side = 1
    else:
        weakness_of_one_body_side = 0

    if 'diarrhoea' in df3:
        diarrhoea = 1
    else:
        diarrhoea = 0
    if 'receiving_unsterile_injections' in df3:
        receiving_unsterile_injections = 1
    else:
        receiving_unsterile_injections = 0
    if 'headache' in df3:
        headache = 1
    else:
        headache = 0
    if 'family_history' in df3:
        family_history = 1
    else:
        family_history = 0

    
    #value_4 assign zero or one
    if 'fast_heart_rate' in df4:
        fast_heart_rate = 1
    else:
        fast_heart_rate = 0
    if 'pain_behind_the_eyes' in df4:
        pain_behind_the_eyes = 1
    else:
        pain_behind_the_eyes = 0
        
    if 'sweating' in df4:
        sweating = 1
    else:
        sweating = 0
    if 'mucoid_sputum' in df4:
        mucoid_sputum = 1
    else:
        mucoid_sputum = 0

    if 'spotting_urination' in df4:
        spotting_urination = 1
    else:
        spotting_urination = 0
    if 'sunken_eyes' in df4:
        sunken_eyes = 1
    else:
        sunken_eyes = 0
    if 'dischromic_patches' in df4:
        dischromic_patches = 1
    else:
        dischromic_patches = 0
    if 'nausea' in df4:
        nausea = 1
    else:
        nausea = 0
    
        #value_5 assign zero or one
    if 'dehydration' in df5:
        dehydration = 1
    else:
        dehydration = 0
    if 'loss_of_appetite' in df5:
        loss_of_appetite = 1
    else:
        loss_of_appetite = 0
        
    if 'abdominal_pain' in df5:
        abdominal_pain = 1
    else:
        abdominal_pain = 0
    if 'stomach_pain' in df5:
        stomach_pain = 1
    else:
        stomach_pain = 0 

    if 'yellowish_skin' in df5:
        yellowish_skin = 1
    else:
        yellowish_skin = 0
    if 'altered_sensorium' in df5:
        altered_sensorium = 1
    else:
        altered_sensorium = 0
    if 'chest_pain' in df5:
        chest_pain = 1
    else:
        chest_pain = 0
    if 'muscle_wasting' in df5:
        muscle_wasting = 1
    else:
        muscle_wasting = 0
    
        #value_6 assign zero or one
    if 'vomiting' in df6:
        vomiting = 1
    else:
        vomiting = 0
    if 'mild_fever' in df6:
        mild_fever = 1
    else:
        mild_fever = 0
        
    if 'high_fever' in df6:
        high_fever = 1
    else:
        high_fever = 0
    if 'red_spots_over_body' in df6:
        red_spots_over_body = 1
    else:
        red_spots_over_body = 0

    if 'dark_urine' in df6:
        dark_urine = 1
    else:                       
        dark_urine = 0
    if 'itching' in df6:
        itching = 1
    else:
        itching = 0
    if 'yellowing_of_eyes' in df6:
        yellowing_of_eyes = 1
    else:
        yellowing_of_eyes = 0
    if 'fatigue' in df6:
        fatigue = 1
    else:
        fatigue = 0
    if 'joint_pain' in df6:
        joint_pain = 1
    else:
        joint_pain = 0
    if 'muscle_pain' in df6:
        muscle_pain = 1
    else:
        muscle_pain = 0
    # convert input into dataframe
    #value_1
    data_dict = {}
    data_dict['receiving_blood_transfusion'] = receiving_blood_transfusion
    data_dict['red_sore_around_nose'] = red_sore_around_nose
    data_dict['abnormal_menstruation'] = abnormal_menstruation
    data_dict['continuous_sneezing'] = continuous_sneezing
    data_dict['breathlessness'] = breathlessness
    data_dict['blackheads'] = blackheads
    data_dict['shivering'] = shivering
    data_dict['dizziness'] = dizziness
    #value_2
    data_dict['back_pain'] = back_pain
    data_dict['unsteadiness'] = unsteadiness
    data_dict['yellow_crust_ooze'] = yellow_crust_ooze
    data_dict['muscle_weakness'] = muscle_weakness
    data_dict['loss_of_balance'] = loss_of_balance
    data_dict['chills'] = chills
    data_dict['ulcers_on_tongue'] = ulcers_on_tongue
    data_dict['stomach_bleeding'] = stomach_bleeding
    #value_3
    data_dict['lack_of_concentration'] = lack_of_concentration
    data_dict['coma'] = coma 
    data_dict['neck_pain'] = neck_pain
    data_dict['weakness_of_one_body_side'] = weakness_of_one_body_side
    data_dict['diarrhoea'] = diarrhoea
    data_dict['receiving_unsterile_injections'] = receiving_unsterile_injections
    data_dict['headache'] = headache
    data_dict['family_history'] = family_history
    #value_4
    data_dict['fast_heart_rate'] = fast_heart_rate
    data_dict['pain_behind_the_eyes'] = pain_behind_the_eyes
    data_dict['sweating'] = sweating
    data_dict['mucoid_sputum'] = mucoid_sputum
    data_dict['spotting_urination'] = spotting_urination
    data_dict['sunken_eyes'] = sunken_eyes
    data_dict['dischromic_patches'] = dischromic_patches  
    data_dict['nausea'] = nausea
    #value_5
    data_dict['dehydration'] = dehydration
    data_dict['loss_of_appetite'] = loss_of_appetite
    data_dict['abdominal_pain'] = abdominal_pain
    data_dict['stomach_pain'] = stomach_pain
    data_dict['yellowish_skin'] = yellowish_skin
    data_dict['altered_sensorium'] = altered_sensorium
    data_dict['chest_pain'] = chest_pain
    data_dict['muscle_wasting'] = muscle_wasting
    #value_6
    data_dict['vomiting'] = vomiting
    data_dict['mild_fever'] = mild_fever
    data_dict['high_fever'] = high_fever
    data_dict['red_spots_over_body'] = red_spots_over_body
    data_dict['dark_urine'] = dark_urine
    data_dict['itching'] = itching
    data_dict['fatigue'] = fatigue
    data_dict['yellowing_of_eyes'] = yellowing_of_eyes
    data_dict['joint_pain'] = joint_pain
    data_dict['muscle_pain'] = muscle_pain
    print(data_dict)

    df=pd.DataFrame(data_dict,index=[0])
    return df
  
def training():
    data = pd.read_csv("datasets/Training.csv")
    # Import train_test_split function
    from sklearn.model_selection import train_test_split

    X, y = data.iloc[:,:-1], data.iloc[:,-1]

    # Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3) # 70% training and 30% test
    #Import Random Forest Model
    from sklearn.ensemble import RandomForestClassifier

    #Create a Gaussian Classifier
    clf=RandomForestClassifier(n_estimators=100)

    #Train the model using the training sets y_pred=clf.predict(X_test)
    clf.fit(X_train,y_train)

    y_pred=clf.predict(X_test)
    #Import scikit-learn metrics module for accuracy calculation
    from sklearn import metrics
    # Model Accuracy, how often is the classifier correct?
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))



    feature_imp = pd.Series(clf.feature_importances_,index=list(data.columns[:-1])).sort_values(ascending=False).head(50)

    X_reduced, y = data[[
        'receiving_blood_transfusion', 'red_sore_around_nose','abnormal_menstruation', 'continuous_sneezing', 
       'breathlessness','blackheads', 
      'shivering', 
      'dizziness', 
        'back_pain', 
        'unsteadiness',
       'yellow_crust_ooze', 
       'muscle_weakness', 
       'loss_of_balance', 
       'chills',
       'ulcers_on_tongue', 
       'stomach_bleeding', 
       'lack_of_concentration', 
       'coma',
       'neck_pain', 
       'weakness_of_one_body_side', 
       'diarrhoea',
       'receiving_unsterile_injections', 
       'headache', 
       'family_history',
       'fast_heart_rate', 
       'pain_behind_the_eyes', 
       'sweating', 
       'mucoid_sputum',
       'spotting_urination',
        'sunken_eyes', 
        'dischromic_patches',
        'nausea',
       'dehydration',
       'loss_of_appetite', 
       'abdominal_pain', 
       'stomach_pain',
       'yellowish_skin', 
       'altered_sensorium', 
       'chest_pain', 
       'muscle_wasting',
       'vomiting', 
       'mild_fever', 
       'high_fever', 
       'red_spots_over_body',
       'dark_urine',
        'itching', 
        'yellowing_of_eyes', 
        'fatigue', 
        'joint_pain',
       'muscle_pain']], data.iloc[:,-1]

    # Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(X_reduced, y, test_size=0.3) # 70% training and 30% test

    #Create a Gaussian Classifier

    clf2=RandomForestClassifier(n_estimators=100)

    #Train the model using the training sets y_pred=clf.predict(X_test)
    clf2.fit(X_train,y_train)

    y_pred=clf2.predict(X_test)

    # Model Accuracy, how often is the classifier correct?
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
    

    # df=pd.read_csv("dataset.csv")
    # df=pre_processing(df)
    # y=df[["Disease"]]
    # df.drop("Disease", axis="columns", inplace=True)
    # x=df
    # # print("#"*50)
    # # print(x)

    dummyRow=pd.DataFrame(np.zeros(len(X_reduced.columns)).reshape(1,len(X_reduced.columns)), columns=X_reduced.columns)
    dummyRow.to_csv('datasets/dummyRowDisease.csv', index=False)
    # model=RandomForestClassifier(random_state=2)
    # # model=XGBClassifier(max_depth=2,min_child_weight=3, gamma=0,subsample=0.86, reg_alpha=0, n_estimators=125)
    # x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2, random_state=5)
    # model.fit(x,y)
    # print("#"*50)
    # print(model)
    # print("#"*50)
    # print(model.score(x_test,y_test))
    pkl_filename="datasets/pickle_model_disease.pkl"
    with open(pkl_filename,'wb') as file:
        pickle.dump(clf2,file)
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
    print("*"*80)
    df_dict = df.to_dict()
    symptoms = [] 
    for disease_name, value in df_dict.items(): 
        # print(disease_name)
        # print(value[0])
        if value[0]==1:
            symptoms.append(disease_name)


        

    # df.drop("Disease", axis="columns", inplace=True)
    dummyRow_filename="datasets/dummyRowDisease.csv"
    df2=pd.read_csv(dummyRow_filename)
    for c1 in df.columns:	
        # print(c1)
        df2[c1]=df[c1]
        # print(df2[c1])
    pkl_filename='datasets/pickle_model_disease.pkl'
    with open(pkl_filename,'rb') as file:
        model=pickle.load(file)
    pred=model.predict(df2)
    return pred, symptoms

if __name__=="__main__":
    training()#df



