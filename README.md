streamlit_app.py.

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
    # Link direto do seu Leão no Google Drive
    url_leao = "https://drive.google.com/uc?export=view&id=1WsZ3mG3ijizFSwBhwwyZnK_zRJG4bpeV"
    st.image(url_leao, width=100)

with col_titulo:
    st.title("QG SDG - Central de Inteligência")
    st.subheader("Comandante Reinaldo Sena Rodrigues")

# Menu Lateral de Missões
with st.sidebar:
    st.title("Arsenal de Missões")
    aba = st.radio("Selecione o Módulo:", ["Home", "Móveis Planejados (IA)", "Análise de Mercado (Tubarões)", "Gerador de Conteúdo", "Gestão de Leads"])

if aba == "Home":
    st.write("### 🏠 Bem-vindo ao Posto de Comando")
    st.info("Este é o seu ambiente original onde vamos centralizar todas as suas ferramentas fora da curva.")
    st.write("---")
    
    # Status das Operações
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Missão 1", "Móveis Planejados", "Ativo")
    with c2:
        st.metric("Missão 2", "Super Indicador SDG", "Em Calibração", delta_color="inverse")
    with c3:
        st.metric("Fábrica SDG", "E-books", "70%")

elif aba == "Móveis Planejados (IA)":
    st.write("### 🏗️ Simulador de Móveis & Projetos")
    st.write("Módulo para automação de orçamentos e design.")

elif aba == "Análise de Mercado (Tubarões)":
    st.write("### 🦈 Monitoramento de Fluxo (MT5)")
    st.warning("Preparando artilharia para amanhã: Rastro dos Tubarões.")

elif aba == "Gerador de Conteúdo":
    st.write("### 📚 Fábrica de E-books SDG")
    st.write("Criação de autoridade digital em escala.")

st.write("---")
st.caption("Selo de Qualidade SDG - Segredos dos Grandes © 2026")
