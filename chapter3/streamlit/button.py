import streamlit as st

result1 = st.button('BUTTON1')
if result1:
     st.write('clicked')
else:
     st.write('not clicked')

result2 = st.button('BUTTON2')
if result2:
     st.write('clicked')
else:
     st.write('not clicked')