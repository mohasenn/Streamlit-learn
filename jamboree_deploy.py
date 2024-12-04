import streamlit as st
import pickle as pk
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression


st.set_page_config(page_title= "JAMBOREE", page_icon=":mortar_board:", layout="wide")
st.title("JAMBOREE Admission Chance")
st.subheader("A linear regression case study.")

st.text("This interactive tool will help you to find your admission chance in the international university from your inputs.")


col1, col2 = st.columns(2)

with col1:
   st.image("col_ad.jpg")

with col2:
   cgpa = st.number_input( "CGPA", min_value=0.0, max_value=10.0, step=0.01, format="%.2f", 
                          help="Enter your Cumulative Grade Point Average (CGPA), whoch should be between 0 and 10")

   gre_score = st.number_input("GRE Score", min_value=0, max_value=340, step=1, format="%d",
                              help="Enter your Graduate Record Examination (GRE) score, which should be between 0 and 340.")
   
   toefl_score = st.number_input("TOEFL Score", min_value=0, max_value=120, step=1, format="%d",
                              help="Enter your Test of English as a Foreign Language (TOEFL) score, which should be between 0 and 120.")
   
   u_rating = st.number_input("University Rating", min_value=0, max_value=5, step=1, format="%d", help="Rate the reputation of your university  (0 to 5).")

   r_exp = st.radio("Do you have any research experience?", ["Yes", "No"], index=None)
   r_exp = 1 if r_exp == "Yes" else 0
   
   sop_rating = st.number_input("SOP Strength", min_value=0, max_value=5, step=1, format="%d", help="Rate the strength of your Statement of Purpose (SOP; 0 to 5).")

   lor = st.number_input("LOR Strength", min_value=0, max_value=5, step=1, format="%d", help="Rate the strength of your Letter of Recommendation (LOR; 0 to 5).")


"""
st.write(f"GRE Score: {gre_score}")
st.write(f"TOEFL Score: {toefl_score}")
st.write(f"University Rating: {u_rating}")
st.write(f"SOP Strength: {sop_rating}")
st.write(f"LOR Strength: {lor}")
st.write(f"CGPA: {cgpa}")
st.write(f"Research Experience: {r_exp}")
"""
if st.button("Predict"):
   input_data = np.array([[gre_score, toefl_score, u_rating, sop_rating, lor, cgpa, r_exp]])

   with open('scale_jamboree.pkl', 'rb') as scale_file:
       scaler = pk.load(scale_file)
   scaled_input = scaler.transform(input_data)

   with open('sk_model_jamboree.pkl', 'rb') as file:
       sk_model = pk.load(file)


   pred = sk_model.predict(scaled_input)
   st.write("Your Admission chance is, ", pred*100, "%")