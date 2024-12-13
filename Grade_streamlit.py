import streamlit as st
st.title("Grade")
project= st.number_input("Enter project score")
internal= st.number_input("internal score: ")
external=st.number_input("external score: ")
if st.button("Grade"):
if(project>=50 and internal >=50 and external >= 50):
 total= project*(70/100)+ internal*(10/100) + external*(20/100)
 st.write(f'total:{total}')
 if(total > 90):
  st.write("A grade")
 elif(total>80 and total<=90):
  st.write("B grade")
 else:
  st.write("C grade")
if(external<50):
   st.write(f"failed in external{external}")
if(internal<50):
   st.write(f"failed in internal{internal}")
if(project<50):
   st.write(f"failed in project{project}")