import streamlit as st
import joblib

# 1. Load the "Brain" we saved in Step 1
model = joblib.load('salary_model.pkl')

# 2. Design the Website UI
st.set_page_config(page_title="AI Salary Predictor", page_icon="💵")
st.title("💼 AI Salary Predictor")
st.write("Enter your experience below to see your predicted salary slip.")

# 3. User Inputs
name = st.text_input("Employee Name")
exp = st.number_input("Years of Experience", min_value=0.0, max_value=50.0, step=0.5)

if st.button("Generate Salary Slip"):
    if name:
        # Prediction Logic
        prediction = model.predict([[exp]])[0]
        tax = prediction * 0.12
        net = prediction * 0.88

        # Display the result in a nice box
        st.success(f"### Salary Slip for {name}")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Gross Salary", f"${prediction:,.2f}")
        with col2:
            st.metric("Net Take-Home", f"${net:,.2f}")
        
        st.info(f"Calculated with a 12% estimated tax (${tax:,.2f})")
    else:
        st.warning("Please enter a name first.")