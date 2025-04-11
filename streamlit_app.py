import streamlit as st
import joblib
import numpy as np

# 모델 불러오기
model = joblib.load("aq_prediction_model.pkl")

# 타이틀
st.title("AQ 예후 예측기")

# 입력 받기
age = st.number_input("나이", min_value=0, max_value=120, value=60)
initial_aq = st.number_input("초기 AQ", min_value=0, max_value=100, value=50)
initial_naming = st.number_input("초기 Naming", min_value=0, max_value=100, value=50)
initial_fluency = st.number_input("초기 Fluency", min_value=0, max_value=100, value=50)
initial_comprehension = st.number_input("초기 Comprehension", min_value=0, max_value=100, value=50)

# 예측 버튼
if st.button("예측하기"):
    input_data = np.array([[age, initial_aq, initial_naming, initial_fluency, initial_comprehension]])
    prediction = model.predict(input_data)
    st.success(f"예측된 최종 AQ 점수는 {prediction[0]:.2f}입니다.")
