import streamlit as st
import pickle as pk
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
import time

st.set_page_config(page_title= "JAMBOREE", page_icon=":mortar_board:", layout="wide")
st.title("JAMBOREE Admission Chance")
st.subheader("A linear regression case study.")

st.text("This interactive tool will help you to find your admission chance in the international university from your inputs.")
st.text("Some default values are filled in, please enter your details to check your result.")

col1, col2 = st.columns(2)

with col1:
   st.image("col_ad.jpg")

with col2:
   cgpa = st.number_input( "CGPA", min_value=0.0, max_value=10.0, step=0.01, format="%.2f", 
                          help="Enter your Cumulative Grade Point Average (CGPA), which should be between 0 and 10", value = 9.24)

   gre_score = st.number_input("GRE Score", min_value=0, max_value=340, step=1, format="%d",
                              help="Enter your Graduate Record Examination (GRE) score, which should be between 0 and 340.", value=330)
   
   toefl_score = st.number_input("TOEFL Score", min_value=0, max_value=120, step=1, format="%d",
                              help="Enter your Test of English as a Foreign Language (TOEFL) score, which should be between 0 and 120.", value = 114)
   
   u_rating = st.slider("University Rating", min_value=0, max_value=5, step=1, format="%d", help="Rate the reputation of your university  (0 to 5).", value=3)

   r_exp = st.radio("Do you have any research experience?", ["Yes", "No"], index=0)
   r_exp = 1 if r_exp == "Yes" else 0

   lor = st.selectbox("LOR Strength", list(np.arange(0.0,5.5, 0.5)), help="Rate the strength of your Letter of Recommendation (LOR; 0 to 5).", index = 9)


col1, col2 = st.columns(2)
with col1:
   st.write(f"GRE Score: {gre_score}")
   st.write(f"TOEFL Score: {toefl_score}")
   st.write(f"University Rating: {u_rating}")
   st.write(f"LOR Strength: {lor}")
   st.write(f"CGPA: {cgpa}")
   st.write(f"Research Experience: {r_exp}")

with col2:
   if st.button("Predict", type="primary"):
      input_data = np.array([[gre_score, toefl_score, u_rating, 5, lor, cgpa, r_exp]]) # my scaler() needs Statement of proposal rating for transforming, so added 5.

      with open('scale_jamboree.pkl', 'rb') as scale_file:
          scaler = pk.load(scale_file)
      scaled_input = scaler.transform(input_data)
      print(scaled_input)
      scaled_input = scaled_input.reshape(-1,1)
      scaled_input = np.append(scaled_input[:3], scaled_input[4:]).reshape(1,-1)

      with open('sk_model_jamboree.pkl', 'rb') as file:
          sk_model = pk.load(file)

      print(scaled_input)
      with st.spinner('Predicting...'):
         time.sleep(1)

      pred = sk_model.predict(scaled_input)
      if pred<0:
         pred = [0]
      elif pred > 1.00:
         pred = [1.00]
      st.markdown(f"<h2 style='color: #008CBA; font-weight: bold; background-color: yellow;'>  Your Admission chance is: {pred[0]*100:.2f} %</h2>", unsafe_allow_html=True)