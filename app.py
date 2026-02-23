import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load saved objects
with open('best_model.pkl', 'rb') as f:
    best_model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('scale_cols.pkl', 'rb') as f:
    scale_cols = pickle.load(f)

with open('feature_cols.pkl', 'rb') as f:
    feature_cols = pickle.load(f)

# Streamlit Inputs
st.title("Titanic Survival Prediction")
pclass = st.selectbox("Passenger Class", [1,2,3])
sex = st.selectbox("Sex (0=female,1=male)", [0,1])
age = st.number_input("Age", 0, 100, 30)
sibsp = st.number_input("Siblings/Spouses aboard", 0, 10, 0)
parch = st.number_input("Parents/Children aboard", 0, 10, 0)
fare = st.number_input("Fare", 0.0, 1000.0, 32.0)
embarked = st.selectbox("Port of Embarkation (0=C,1=Q,2=S)", [0,1,2])
family_size = sibsp + parch + 1

# AgeGroup one-hot selection (as in training)
age_group = st.selectbox("Age Group (Child=0,Teen=1,Adult=2,MidAge=3,Senior=4)", [0,1,2,3,4])
input_data = pd.DataFrame({
    'pclass':[pclass],
    'sex':[sex],
    'age':[age],
    'sibsp':[sibsp],
    'parch':[parch],
    'fare':[fare],
    'FamilySize':[family_size],
    'embarked':[embarked],
    'AgeGroup_Teen':[1 if age_group==1 else 0],
    'AgeGroup_Adult':[1 if age_group==2 else 0],
    'AgeGroup_MidAge':[1 if age_group==3 else 0],
    'AgeGroup_Senior':[1 if age_group==4 else 0]
})

# Log transform fare
input_data['fare'] = np.log1p(input_data['fare'])

# Scale numeric columns
input_data[scale_cols] = scaler.transform(input_data[scale_cols])

# Reindex columns to match training
input_data = input_data.reindex(columns=feature_cols, fill_value=0)

# Prediction
if st.button("Predict Survival"):
    if "keras" in str(type(best_model)):
        pred_prob = best_model.predict(input_data.values)
        prediction = (pred_prob > 0.5).astype(int)
    else:
        prediction = best_model.predict(input_data)

    if prediction[0] == 1:
        st.success("Passenger is likely to Survive 🚢")
    else:
        st.error("Passenger is unlikely to Survive ⚓")
