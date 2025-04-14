import streamlit as st
import pandas as pd

st.title("BMI Calculator")

# Slider for weight and height

weight = st.slider("Select your weight (kg)", min_value=1, max_value=200, step=1)
height = st.slider("Select your height (cm)", min_value=50, max_value=250, step=1)

# Detailed BMI Categories
st.write("## BMI Categories and Ranges")
st.write("- **Underweight**: BMI less than 18.5. You may be at risk for malnutrition or other health problems. It is important to consult a healthcare professional for advice on gaining weight in a healthy manner.")
st.write("- **Normal Weight**: BMI between 18.5 and 24.9. This is considered a healthy weight range. Maintaining a balanced diet and regular exercise is key to staying in this range.")
st.write("- **Overweight**: BMI between 25 and 29.9. Being overweight may increase the risk of health problems such as heart disease and type 2 diabetes. A healthy diet and exercise can help manage weight.")
st.write("- **Obese**: BMI 30 or higher. Obesity increases the risk of serious health problems such as high blood pressure, heart disease, stroke, and certain types of cancer. A healthcare provider can help you develop a plan to lose weight safely.")

# Calculate BMI when button is pressed
if st.button("Calculate BMI"):
    height_m = height / 100  # Convert cm to meters
    bmi = weight / (height_m ** 2)
    st.write(f"Your BMI is **{bmi:.2f}**")

    # Optional BMI category display
    if bmi < 18.5:
        st.warning("You are underweight.")
    elif 18.5 <= bmi < 25:
        st.success("You have a normal weight.")
    elif 25 <= bmi < 30:
        st.warning("You are overweight.")
    else:
        st.error("You are obese.")
