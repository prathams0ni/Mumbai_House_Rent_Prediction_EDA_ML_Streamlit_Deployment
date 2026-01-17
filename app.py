import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("FinalModel.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(
    page_title="House Rent Prediction",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 House Rent Prediction App")
st.write("Enter house details to predict monthly rent")


locality_map = {'Andheri': 0, 'Bandra': 1, 'Bhandup': 2, 'Byculla': 3, 'Chembur': 4, 
                'Colaba': 5, 'Dadar': 6, 'Dharavi': 7, 'Fort': 8, 'Ghatkopar': 9, 
                'Girgaon': 10, 'Goregaon': 11, 'Govandi': 12, 'Grant Road': 13, 
                'Jogeshwari': 14, 'Juhu': 15, 'Khar': 16, 'Kurla': 17, 'Lalbaug': 18,
                  'Lokhandwala': 19, 'Mahalakshmi': 20, 'Mahim': 21, 'Malabar Hill': 22, 
                  'Malad': 23, 'Marine Drive': 24, 'Masjid': 25, 'Matunga': 26, 
                  'Mulund': 27, 'Nariman Point': 28, 'Parel': 29, 'Powai': 30, 
                  'Prabhadevi': 31, 'Santacruz': 32, 'Sion': 33, 'Tardeo': 34,
                    'Vidyavihar': 35, 'Vikhroli': 36, 'Vile Parle': 37, 'Wadala': 38, 
                    'Worli': 39}

type_map = {'1 RK Apartment':0,'1 BHK Apartment':1,'2 BHK Apartment':2,'3 BHK Apartment':3}

furnish_map = {'Unfurnished':0,'Semi Furnished':1,'Fully Furnished':2}

# User Inputs
locality = st.selectbox("📍 Locality", list(locality_map.keys()))
house_type = st.selectbox("🏘 House Type", list(type_map.keys()))
area = st.number_input("📐 Built-up Area (sq.ft)", min_value=200, step=50)
furnishing = st.selectbox("🛋 Furnishing", list(furnish_map.keys()))

bathrooms = st.slider("🚿 Bathrooms", 1, 5, 1)
balcony = st.slider("🌿 Balcony", 0, 3, 0)

parking = st.slider("🚗 Parking Available?", 0,6,1)



## Encoding
locality_enc = locality_map[locality]
type_enc = type_map[house_type]
furnish_enc = furnish_map[furnishing]

input_data = np.array([[
    locality_enc,
    type_enc,
    area,
    furnish_enc,
    bathrooms,
    balcony,
    parking
]])

if st.button("💰 Predict Rent"):
    prediction = model.predict(input_data)
    st.success(f"Estimated Monthly Rent: ₹ {int(prediction[0]):,}")