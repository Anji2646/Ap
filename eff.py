import streamlit as st

def calculate_efficiency(input_power, output_power, losses):
    efficiency = (output_power / input_power) * 100
    return efficiency

st.title("Transformer Efficiency Calculator")

st.write("Enter the values of input power, output power, and losses:")

input_power = st.number_input("Input Power (W)", step=0.1)
output_power = st.number_input("Output Power (W)", step=0.1)
losses = st.number_input("Losses (W)", step=0.1)

if st.button("Calculate Efficiency"):
    efficiency = calculate_efficiency(input_power, output_power, losses)
    st.write(f"Transformer Efficiency: {efficiency:.2f}%")
