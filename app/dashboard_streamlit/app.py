import streamlit as st
import pandas as pd
import joblib

st.title("Classificador de Grãos de Trigo")

# Carregar o modelo
modelo = joblib.load("modelos/modelos_salvos/melhor_modelo.pkl")

# Formulário de entrada
st.subheader("Insira as características do grão:")
area = st.number_input("Área", min_value=0.0)
perimetro = st.number_input("Perímetro", min_value=0.0)
compacidade = st.number_input("Compacidade", min_value=0.0)
comprimento_nucleo = st.number_input("Comprimento do Núcleo", min_value=0.0)
largura_nucleo = st.number_input("Largura do Núcleo", min_value=0.0)
coef_assimetria = st.number_input("Coeficiente de Assimetria", min_value=0.0)
comprimento_sulco = st.number_input("Comprimento do Sulco", min_value=0.0)

if st.button("Classificar"):
    dados = pd.DataFrame([[area, perimetro, compacidade, comprimento_nucleo,
                           largura_nucleo, coef_assimetria, comprimento_sulco]],
                         columns=['area', 'perimetro', 'compacidade', 'comprimento_nucleo',
                                  'largura_nucleo', 'coef_assimetria', 'comprimento_sulco'])
    
    predicao = modelo.predict(dados)[0]
    st.success(f"Classe prevista: {predicao}")
