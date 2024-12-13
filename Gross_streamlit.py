import streamlit as st
st.title("Gross salary calculator")
basic=st.number_input("Enter your basic salary")
if st.button("Calculate Gross salary"):
   hra=0
   da=0
   if(basic < 10000):
    hra = basic * (67 / 100)
    da = basic * (73 / 100)
   elif (basic >= 10000 and basic <= 20000):
    hra = basic * (69 / 100)
    da = basic * (76 / 100)
   else:
    hra = basic * (73 / 100)
    da = basic * (89 / 100)
   gs = hra + da + basic
   print(f'gs: {gs}')
   st.write("gross salary",+gs)
