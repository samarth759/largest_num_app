import streamlit as st

def find_largest(num1, num2, num3):
    return max(num1, num2, num3)

st.title('Find the Largest Number')

# Creating number input fields
number1 = st.number_input('Enter first number', value=0)
number2 = st.number_input('Enter second number', value=0)
number3 = st.number_input('Enter third number', value=0)

if st.button('Find Largest'):
    largest = find_largest(number1, number2, number3)
    st.success(f'The largest number is {largest}')
