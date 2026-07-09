import streamlit as st
from PIL import Image

# Configuración de la página
st.set_page_config(
    page_title="Portal de Solicitud de Perfiles SAP",
    page_icon="💼",
    layout="wide"
)

# Cargar estilos
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Cargar logo
logo = Image.open("assets/logo_altim.png")

# Cabecera
col1, col2 = st.columns([1, 5])

with col1:
    st.image(logo, width=130)

with col2:
    st.title("Portal de Solicitud de Perfiles SAP")
    st.markdown(
        "### Área de Talent Acquisition"
    )

st.divider()

# Barra lateral
with st.sidebar:

    st.image(logo, width=180)

    st.markdown("## Menú")

    st.success("Versión 2.0")

    st.info(
        """
Portal corporativo para la solicitud
de perfiles SAP.
"""
    )

# Mensaje principal
st.info(
"""
Bienvenido.

Desde esta aplicación podrás solicitar perfiles SAP para los diferentes proyectos de Altim.

Todos los campos marcados con * son obligatorios.
"""
)

st.success("La aplicación está correctamente instalada.")
