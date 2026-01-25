# 🏠 Mumbai House Rent Prediction | EDA + ML + Streamlit Deployment

A complete end-to-end **Machine Learning regression project** to predict **monthly house rent (₹)** in Mumbai using property features like locality, house type, built-up area, furnishing status, and amenities.  
The best-performing model is deployed as a **Streamlit Web App on Streamlit Community Cloud** for real-time predictions.

---

## 📌 Project Overview

House rent in Mumbai varies heavily due to multiple factors such as location, size, furnishing, and facilities.  
This project focuses on:
- Cleaning and preparing the dataset
- Handling outliers for better model performance
- Training multiple regression models
- Evaluating models using **R² Score** and **RMSE**
- Deploying the final model using **Streamlit Cloud**

---

## 🎯 Objective

- Predict monthly rent based on property details  
- Compare multiple ML models and select the best one  
- Provide a simple UI for rent prediction via Streamlit deployment  

---

## 🗂 Dataset

- **Dataset Name:** Mumbai House Rent Dataset  
- **File:** `Mumbai_House_Rent.csv`  
- **Target Variable:** Rent (Monthly Rent in ₹)

---

## ⚙️ Workflow / Steps Performed

### 1️⃣ Data Loading & Inspection
- Checked shape, columns, datatypes
- Verified missing values and duplicates

### 2️⃣ Data Cleaning & Preprocessing
- Removed/handled null values (if any)
- Converted categorical features into numeric using encoding
- Prepared final feature set for model training

### 3️⃣ Outlier Detection & Handling
- Identified extreme values affecting rent prediction
- Handled outliers to reduce noise and improve stability

### 4️⃣ Model Building
Trained and tested multiple regression models:
- **Linear Regression**
- **Decision Tree Regressor**
- **Random Forest Regressor**

### 5️⃣ Model Evaluation
Used:
- **R² Score**
- **RMSE (Root Mean Squared Error)**

---

## 📊 Model Performance (Outputs)

Below are the results captured from the notebook outputs:

### ✅ Linear Regression
- **R² Score:** ~ `0.56`
- **RMSE:** ~ `26908`

### ✅ Decision Tree Regressor
- **R² Score:** ~ `0.56`
- **RMSE:** ~ `26956`

### ✅ Random Forest Regressor (Best Model 🏆)
- **R² Score:** ~ `0.74`
- **RMSE:** ~ `20638`

📌 **Best Model Selected:** **Random Forest Regressor**  
Because it achieved **higher R²** and **lower RMSE**, making predictions more accurate than other models.

---

## 🌐 Streamlit Cloud Deployment

This project is deployed on **Streamlit Community Cloud** to make rent prediction interactive and user-friendly.

### 🔥 Features of the Web App
Users can enter:
- 📍 Locality  
- 🏘 House Type (1RK / 1BHK / 2BHK / 3BHK)  
- 📐 Built-up Area (sq.ft)  
- 🛋 Furnishing Status  
- 🚿 Bathrooms  
- 🌿 Balcony  
- 🚗 Parking  

…and instantly get the **predicted monthly rent (₹)**.

### 🔗 Live Demo
👉 **Streamlit App Link:** https://mumbaihouserentprediction.streamlit.app/

---

## 🧠 Tech Stack Used

- **Python**
- **Pandas / NumPy** (Data Processing)
- **Matplotlib / Seaborn** (EDA & Visualization)
- **Scikit-learn** (Model Training & Evaluation)
- **Streamlit** (Web App Deployment)
- **Pickle** (Model Saving)

---

## 📁 Project Structure

```bash
├── Mumbai_House_Rent.csv           # Dataset
├── HouseRentPredictor.ipynb        # Notebook (EDA + Training + Evaluation)
├── FinalModel.pkl                  # Saved trained model
├── app.py                          # Streamlit app file
├── requirements.txt                # Dependencies
└── README.md                       # Project documentation
```
---

## ▶️ How to Run This Project Locally

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/prathams0ni/Mumbai_House_Rent_Prediction_EDA_ML_Streamlit_Deployment.git
cd Mumbai_House_Rent_Prediction_EDA_ML_Streamlit_Deployment
python -m venv venv
venv\Scripts\activate
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```
---

## ✅ Conclusion

This project successfully demonstrates an end-to-end Machine Learning workflow for predicting **monthly house rent prices in Mumbai**.  
The complete pipeline includes **data cleaning**, **outlier handling**, **feature encoding**, and training multiple regression models such as **Linear Regression**, **Decision Tree**, and **Random Forest**.

Based on model evaluation using **R² Score** and **RMSE**, the **Random Forest Regressor** achieved the best performance and was selected as the final model.  
To make the solution practical and user-friendly, the final trained model was deployed on **Streamlit Community Cloud**, allowing users to input house details and get instant rent predictions in real-time.

https://mumbaihouserentprediction.streamlit.app/

<img width="791" height="836" alt="image" src="https://github.com/user-attachments/assets/3c0e1726-78f2-42df-9960-6e85e8dbf1b2" />
