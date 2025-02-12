import os
import pickle
import streamlit as st
import streamlit.components
from streamlit_option_menu import option_menu
st.set_page_config(page_title="Disease Outbreak Prediction",layout="wide",page_icon="🧑‍⚕️")
diabetes_model=pickle.load(open(r"D:/Internship_Project/aicte-Prediction-of-disease-Out-Break/PredictionModels/diabetes_model.sav",'rb'))
heart_model=pickle.load(open(r"D:/Internship_Project/aicte-Prediction-of-disease-Out-Break/PredictionModels/heart_model.sav",'rb'))
parkinsons_model=pickle.load(open(r"D:/Internship_Project/aicte-Prediction-of-disease-Out-Break/PredictionModels/parkinsons.sav",'rb'))

with st.sidebar:
    selected= option_menu("Prediction of disease outbreak system",["Diabetes Prediction","Heart Disease Prediction","Parkinson Disease Prediction"],
                          menu_icon='hosital.fill',icons=['activity','heart','person'],default_index=0)
    
if selected=="Diabetes Prediction":
    st.title("Diabetes Prediction using ML")
    col1,col2,col3=st.columns(3)
    with col1:
        Pregnancies=st.text_input("Number of Pregnancies :")
    with col2:
        Glucose=st.text_input("Glucose level :")
    with col3:
        BloodPressure=st.text_input("Blood Pressure value :")
    with col1:
        SkinThickness=st.text_input("Skin Thickness value :")
    with col2:
        Insulin=st.text_input("Insulin level :")
    with col3:
        BMI=st.text_input("BMI Value :")
    with col1:
        DiabetesPedigreeFunction=st.text_input("Diabetes Pedigree Function Value :")
    with col2:
        Age=st.text_input("Age of the person :")
        
    diab_diagnosis=""
    if st.button('Diabetes Test Result'):
        user_input=[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]
        user_input=[float(x) for x in user_input]
        diab_prediction =diabetes_model.predict([user_input])
        if diab_prediction[0]==1:
            diab_diagnosis="The Person is Diabetic"
        else:
             diab_diagnosis="The Person is not Diabetic"
        st.success(diab_diagnosis)

if selected=="Heart Disease Prediction":
    st.title("Heart Disease Prediction using ML")
    col1,col2,col3,col4,col5,col6=st.columns(6)
    with col1:
        age=st.text_input("Age :")
    with col2:
        sex=st.text_input("Sex :")
    with col3:
        cp=st.text_input("CP value :")
    with col4:
        trestbps=st.text_input("Trestbps value :")
    with col5:
        chol=st.text_input("chol value :")
    with col6:
        fbs=st.text_input("fbs Value :")
    with col1:
        restecg=st.text_input("restecg Value :")
    with col2:
        thalach=st.text_input("thalach value :")
    with col3:
        exang=st.text_input("exang value :")
    with col4:
        oldpeak=st.text_input("oldpeak value :")
    with col5:
        slope=st.text_input("slope :")
    with col6:
        ca=st.text_input("ca :")
    with col1:
        thal=st.text_input("thal :")
    
    heart_ds=""
    if st.button('Heart Disease Test Result'):
        user_input=[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        user_input=[float(x) for x in user_input]
        heart_prediction =heart_model.predict([user_input])
        if heart_prediction[0]==1:
            heart_ds="The Person has heart Disease"
        else:
            heart_ds="The Person does not have heart Disease"
        st.success(heart_ds)

if selected=="Parkinson Disease Prediction":
    st.title("Parkinson Disease Prediction using ML")
    col1,col2,col3,col4=st.columns(4)
    with col1:
        MDVP_Fo=st.text_input("MDVP:Fo(Hz) value :")
    with col2:
        MDVP_Fhi=st.text_input("MDVP:Fhi(Hz) value :")
    with col3:
        MDVP_Flo=st.text_input("MDVP:Flo(Hz) value :")
    with col4:
        MDVP_jitter=st.text_input("MDVP:jitter(%) value :")
    with col1:
        MDVP_jitter_abs=st.text_input("MDVP:jitter(abs) values :")
    with col2:
        MDVP_RAP=st.text_input("MDVP:RAP Value :")
    with col3:
        MDVP_PPQ=st.text_input("MDVP:PPQ Value :")
    with col4:
        Jitter_DDP=st.text_input("Jitter:DDP Value :")
    with col1:
        MDVP_Shimmer=st.text_input("MDVP:Shimmer Value:")
    with col2:
        MDVP_Shimmer_dB=st.text_input("MDVP:Shimmer(dB) Value :")
    with col3:
        Shimmer_APQ3=st.text_input("Shimmer:APQ3 Value :")
    with col4:
        Shimmer_APQ5=st.text_input("Shimmer:APQ5 Value :")
    with col1:
        MDVP_APQ=st.text_input("MDVP:APQ Value :")
    with col2:
        Shimmer_DDA=st.text_input("Shimmer:DDA Value :")
    with col3:
        NHR=st.text_input("NHR Value :")
    with col4:
        HNR=st.text_input("HNR Value :")
    with col1:
        RPDE=st.text_input("RPDE Value :")
    with col2:
        DFA=st.text_input("DFA Value :")
    with col3:
        spread1=st.text_input("spread1 Value :")
    with col4:
        spread2=st.text_input("spread2 Value :")
    with col1:
        D2=st.text_input("D2 Value :")
    with col2:
        PPE=st.text_input("PPE Value :")
    
    park_ds=""
    if st.button('Parkinson Disease Test Result'):
        user_input=[MDVP_Fo,MDVP_Fhi,MDVP_Flo,MDVP_jitter,MDVP_jitter_abs,MDVP_RAP,MDVP_PPQ,Jitter_DDP,MDVP_Shimmer,MDVP_Shimmer_dB,Shimmer_APQ3,Shimmer_APQ5,Shimmer_DDA,MDVP_APQ,NHR,HNR,RPDE,DFA,D2,PPE,spread1,spread2]
        user_input=[float(x) for x in user_input]
        parkinson_prediction =parkinsons_model.predict([user_input])
        if parkinson_prediction[0]==1:
            park_ds="The Person has Prkinson Disease"
        else:
            park_ds="The Person does not have Parkinson Disease"
        st.success(park_ds)