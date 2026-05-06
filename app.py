import streamlit as st

# Configuração da página SDG
st.set_page_config(page_title="QG SDG - Central de Inteligência", layout="wide")

# Estilo para manter o padrão Segredos dos Grandes
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stButton>button { width: 100%; border-radius: 5px; height: 3em; background-color: #2e7d32; color: white; }
    </style>
    """, unsafe_allow_html=True)

# Cabeçalho com o Leão SDG
col_logo, col_titulo = st.columns([1, 8])
with col_logo:
    url_leao = "https://drive.google.com/uc?export=view&id=1WsZ3mG3ijizFSwBhwwyZnK_zRJG4bpeV"
    st.image(url_leao, width=100)

with col_titulo:
    st.title("QG SDG - Central de Inteligência")
    st.subheader("Comandante Reinaldo Sena Rodrigues")

# Menu Lateral de Missões
with st.sidebar:
    st.title("Arsenal de Missões")
    aba = st.radio("Selecione o Módulo:", ["Home", "Organização de Projetos", "Analista de Propostas", "Móveis Planejados (IA)"])

if aba == "Home":
    st.write("### 🏠 Posto de Comando Operacional")
    st.info("Centralizando suas ferramentas para o 99Freelas e gestão individual.")
    st.write("---")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Status", "QG Online", "100%")
    with c2:
        st.metric("Projetos", "Em Organização", "SDG")
    with c3:
        st.metric("Renda", "Meta 99Freelas", "Iniciando")

elif aba == "Organização de Projetos":
    st.write("### 📝 Minha Agenda de Clientes")
    st.text_input("Novo Cliente:")
    st.date_input("Prazo de Entrega:")
    if st.button("Salvar na Base de Dados"):
        st.success("Missão registrada no QG!")

elif aba == "Analista de Propostas":
    st.write("### 🤖 Analista SDG para 99Freelas")
    st.text_area("Cole aqui o que o cliente pediu no site:")
    if st.button("Gerar Estratégia de Venda"):
        st.write("Analisando requisitos e preparando proposta matadora...")

st.write("---")
st.caption("Selo de Qualidade SDG - Segredos dos Grandes © 2026")
