import streamlit as st 

st.title("🌎 Unit Converter App")

to_meters = {
    "meters": 1.0,
    "kilometers": 1000.0,
    "miles": 1609.34,
    "foot": 0.3048,
    "yard": 0.9144,
}

units = list(to_meters.keys())

st.write("## 📝 Convert between different units of length ")

#  unit to convet from
from_unit = st.selectbox("📏 Select the unit to convert from:", units)

#  unit to convert to 
to_units = st.selectbox("📐 Select the unit to convert to:", units)

# enter the value 
value = st.number_input("📝 Enter the value to convert:",min_value=0.0, value=1.0)

# conversation logic
if st.button("🔁 Convert"):
    # convert the input value to meters 
    value_in_meters = value * to_meters[from_unit]

    
    # convert meters to the target units 
    converted_value = value_in_meters / to_meters[to_units]


    # display the result
    st.success(f"✨ {value} {from_unit} = {converted_value} {to_units} ✨")

