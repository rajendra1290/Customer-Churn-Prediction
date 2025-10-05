import streamlit as st
import joblib
import numpy as np

# Load model and scaler
scaler = joblib.load("scaler.pkl")
model = joblib.load("model.pkl")

# Page Config
st.set_page_config(page_title="Churn Prediction", page_icon="📊", layout="centered")

# Sidebar Navigation
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "ℹ️ About Churn"])

# ---------------- HOME PAGE ----------------
if page == "🏠 Home":
    st.markdown("<h1 style='text-align:center; color:#4CAF50;'>💡 Customer Churn Prediction</h1>", unsafe_allow_html=True)
    st.write("👉 Please enter the details below and click **Predict** to check churn possibility.")

    st.divider()

    # Layout with columns
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("🔢 Enter Age (10–100)", min_value=10, max_value=100, value=10)
        tenure = st.number_input("⏳ Enter Tenure in Months (0–130)", min_value=0, max_value=130, value=0)

    with col2:
        monthlycharge = st.number_input("💰 Enter Monthly Charge ($30–150)", min_value=30, max_value=150, value=30)
        gender = st.selectbox("🧑 Gender", ["Select Gender", "Male", "Female"])

    st.divider()

    # Predict Button
    if st.button("🚀 Predict Churn"):
        if age and tenure and monthlycharge and gender != "Select Gender":
            try:
                age = int(age)
                tenure = int(tenure)
                monthlycharge = float(monthlycharge)
                gender_selected = 1 if gender == "Female" else 0

                x = [age, gender_selected, tenure, monthlycharge]
                x_array = scaler.transform([np.array(x)])
                prediction = model.predict(x_array)[0]

                if prediction == 1:
                    st.error("⚠️ The model predicts: **Yes, Customer will Churn**")
                    st.image("https://cdn-icons-png.flaticon.com/512/463/463612.png", width=120)
                    st.snow()
                else:
                    st.success("🎉 The model predicts: **No, Customer will Stay**")
                    st.image("https://cdn-icons-png.flaticon.com/512/3159/3159066.png", width=120)
                    st.snow()
            except:
                st.error("⚠️ Please enter valid numeric values for age, tenure, and monthly charge.")
        else:
            st.warning("⚠️ Please fill all fields before predicting.")
    else:
        st.write("👉 Enter the values and click Predict to see results!")

# ---------------- ABOUT CHURN PAGE ----------------
elif page == "ℹ️ About Churn":
    st.markdown("<h1 style='text-align:center; color:#2196F3;'>ℹ️ What is Customer Churn?</h1>", unsafe_allow_html=True)

    st.write(
        """
        **Customer Churn** means when a customer **stops using a company's product or service**.  
        Companies focus on churn prediction because retaining customers is cheaper and more profitable than finding new ones.
        """
    )

    colA, colB = st.columns(2)
    with colA:
        st.image("https://cdn-icons-png.flaticon.com/512/463/463612.png", width=150)
        st.write("🚪 A user cancels their **Netflix subscription** → Churn")
        st.write("📴 A mobile user switches from **Jio to Airtel** → Churn")
    with colB:
        st.image("https://cdn-icons-png.flaticon.com/512/3159/3159066.png", width=150)
        st.write("🎉 A customer **renews their subscription** → Not Churn")
        st.write("📶 A user stays with the same telecom provider → Not Churn")

    st.success("👉 This app helps predict whether a customer will churn or stay using Machine Learning.")
