import streamlit as st

# Header and title
st.title("🌍 **Unit Converter App**")
st.markdown("""
### 🚀 Convert Length, Weight, and Time Instantly!

Welcome to the **Unit Converter App**. You can convert between different units of measurement, including:
- **Length** (Kilometers, Miles, Meters)
- **Weight** (Kilograms, Pounds, Grams)
- **Time** (Hours, Minutes, Seconds)

Just select a category, choose the units, and enter a value to get your conversion in real-time. Let's get started! 
""")

# Category selection
category = st.selectbox("🔍 **Select a category**", ["Length", "Weight", "Time"])

# Conversion function
def convert_units(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value * 1.60934
        elif unit == "Meters to Kilometers":
            return value * 0.001
        elif unit == "Kilometers to Meters":
            return value * 1000

    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value * 0.453592
        elif unit == "Grams to Kilograms":
            return value * 0.001
        elif unit == "Kilograms to Grams":
            return value * 1000

    elif category == "Time":
        if unit == "Seconds to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Hours to Minutes":
            return value * 60
        elif unit == "Minutes to Hours":
            return value / 60
        elif unit == "Hours to Seconds":
            return value * 3600
        elif unit == "Seconds to Hours":
            return value / 3600

# Handle category-specific unit selection
if category == "Length":
    unit = st.selectbox("📏 **Select a conversion**", 
                        ["Kilometers to Miles", "Miles to Kilometers", "Meters to Kilometers", "Kilometers to Meters"],
                        help="Choose the length conversion you need.")
elif category == "Weight":
    unit = st.selectbox("⚖ **Select a conversion**", 
                        ["Kilograms to Pounds", "Pounds to Kilograms", "Grams to Kilograms", "Kilograms to Grams"],
                        help="Choose the weight conversion you need.")
elif category == "Time":
    unit = st.selectbox("⏳ **Select a conversion**", 
                        ["Seconds to Minutes", "Minutes to Seconds", "Hours to Minutes", "Minutes to Hours", 
                         "Hours to Seconds", "Seconds to Hours"],
                        help="Choose the time conversion you need.")

# Input field for the user to enter a value
value = st.number_input(f"💡 **Enter value in {unit.split(' to ')[0]}**:", min_value=0.0, step=0.1, help="Enter the numerical value you wish to convert.")

# Conversion trigger button
if st.button("🔄 Convert"):
    if value > 0:
        result = convert_units(category, value, unit)
        # Displaying the result with success message
        st.success(f"✅ **The result is {result:.2f}**")
    else:
        st.error("❌ Please enter a value greater than 0 for conversion.")
        
#  footer
st.markdown("""
---
Developed by **RUBI ABID**
""")
