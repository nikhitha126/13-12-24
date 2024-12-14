import streamlit as st
st.title("Total ")
sal= st.number_input("total sal")
b1 = st.number_input(" bill1")
b2 = st.number_input(" bill2")
b3 = st.number_input(" bill3")
total=b1+b2+b3
p=(total/sal)*100 if sal>0 else 0
if st.button("Calculate"):
   st.write(f'total: {total}')
   st.write(f'Percentage:{p:.2f}')
