import streamlit as st
import joblib
import numpy as np

# Carregar modelo
modelo = joblib.load('modelo_casas.pkl')

# Título
st.title("🏠 Previsão de Preços de Casas")

# Inputs do usuário
area = st.number_input("Área da casa (m²)", min_value=20.0, max_value=1000.0, value=100.0)
quartos = st.number_input("Número de quartos", min_value=1, max_value=10, value=3)
banheiros = st.number_input("Número de banheiros", min_value=1, max_value=5, value=2)
idade = st.number_input("Idade da casa (em anos)", min_value=0, max_value=100, value=10)

# Prever preço
if st.button("Prever Preço"):
    entrada = np.array([[area, quartos, banheiros, idade]])
    preco = modelo.predict(entrada)[0]
    st.success(f"💰 Preço estimado: R$ {preco:,.2f}")
