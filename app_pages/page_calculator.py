import streamlit as st

def calculator_body():
    """
    Uses beta columns to split page in 3 columns
    Gives col1 and col2 number inputs
    gives col3 an operator selector
    the if statement checks for a 0 division error
    This function defines the layout of the calculator
    """
    st.write("---")
    col1, col2, col3 = st.beta_columns(3)
    with col1:
        num1 = st.number_input(label = "Enter the first integer", step = 1)
    with col2:
        num2 = st.number_input(label = "Enter the second integer", step = 2)
    with col3:
        operator = st.selectbox(
            label = "Select the operator",
            options = ['Add', 'Subtract', 'Multiply', 'Divide'] 
            )
    if st.button('Click here to calculate'):
        if num2 == 0 and operator == 'Divide':
            st.error('Division by 0 is impossible. Enter a non-zero integer')
        else:
            calculator_function(num1, num2, operator)

def calculator_function(num1, num2, operator):
    """
    This function performs the mathematical operations
    """
    if operator == 'Add':
        result = num1 + num2
    elif operator == 'Subtract':
        result = num1 - num2
    elif operator == 'Multiply':
        result = num1 * num2
    elif operator == 'Divide':
        result = num1 / num2
    st.success(f'The result is: **{result}** ')
    
