import streamlit as st
from preparation.pipe import model
import pandas as pd

st.title("Оценка бриллианта по параметрам")
st.text(
"""
Оценка стоимости бриллианта по его параметрам:
carat: вес в каратах, 
diametr: диаметр, 
color: цвет, одна из категорий \
['D', 'E', 'F', 'G', 'H', 'I', 'J'], 
clarity: прозрачность, 
\tодна из категорий ['IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2', 'I1']
""")
carat = st.number_input("carat")
diametr = st.number_input("diametr")
color = st.text_input("color", 
                    help="['D', 'E', 'F', 'G', 'H', 'I', 'J']")
clarity = st.text_input("clarity", 
                    help="['IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2', 'I1']")

params = pd.DataFrame({'carat':[carat], 
                        'y':[diametr], 
                        'color':[color], 
                        'clarity':[clarity]})

calculate = st.button("Вычислить цену")
if calculate:
    result = model.predict(params)
    st.subheader("Результат оценки:", divider='rainbow')
    st.text(f'Стоимость вашего бриллианта: {result[0]}')
    