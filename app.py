import streamlit as st
from datetime import date
from PIL import Image
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# ----------------------------------------------------------
# CONFIGURACIÓN DE LA PÁGINA
# ----------------------------------------------------------

st.set_page_config(
    page_title="Portal Solicitud Perfil SAP",
    page_icon="💼",
    layout="wide"
)

# ----------------------------------------------------------
# COLORES CORPORATIVOS
# ----------------------------------------------------------

AZUL = "#0057B8"
VERDE = "#3BB7A5"
GRIS = "#F5F7FA"

st.markdown(f"""
<style>

.stApp {{
    background-color:{GRIS};
}}

h1 {{
    color:{AZUL};
    font-weight:700;
}}

h2 {{
    color:{AZUL};
}}

h3 {{
    color:{VERDE};
}}

div[data-testid="stForm"] {{
    background:white;
    padding:25px;
    border-radius:12px;
}}

.stButton>button {{

    background:{AZUL};
    color:white;
    font-size:18px;
    height:50px;
    width:100%;
    border-radius:8px;
    border:none;

}}

.stButton>button:hover {{

    background:{VERDE};
    color:white;

}}

.obligatorio{

color:red;
font-weight:bold;

}

</style>

""", unsafe_allow_html=True)

# ----------------------------------------------------------
# LOGO
# ----------------------------------------------------------

logo = Image.open("assets/logo_altim.png")

c1,c2 = st.columns([1,4])

with c1:
    st.image(logo,width=170)

with c2:

    st.title("Portal de Solicitud de Perfiles SAP")

    st.write(
        """
Aplicación corporativa para la solicitud de perfiles SAP.

Todos los campos marcados con * son obligatorios.
"""
    )

st.divider()

# ----------------------------------------------------------
# COMIENZA EL FORMULARIO
# ----------------------------------------------------------

with st.form("SolicitudSAP"):

    st.header("1. Datos del solicitante")

    col1,col2 = st.columns(2)

    with col1:

        nombre = st.text_input(
            "🔴 Nombre y apellidos *"
        )

        cargo = st.text_input(
            "🔴 Cargo *"
        )

    with col2:

        departamento = st.text_input(
            "🔴 Departamento *"
        )

        fecha = st.date_input(
            "Fecha de solicitud",
            value=date.today()
        )

    st.divider()

    st.header("2. Información de la posición")

    puesto = st.text_input(
        "🔴 Nombre completo del puesto *"
    )

    motivo = st.selectbox(

        "🔴 Motivo de la contratación *",

        [

            "Nueva posición",

            "Sustitución",

            "Incremento de equipo",

            "Proyecto específico"

        ]

    )

    vacantes = st.number_input(

        "🔴 Número de vacantes *",

        min_value=1,

        value=1

    )

    st.divider()

    st.header("3. Requisitos Técnicos")

    st.info(
        "Esta sección se añadirá en la Parte 2."
    )

    st.divider()

    # ----------------------------------------------------------
# 4. EXPERIENCIA
# ----------------------------------------------------------

st.header("4. Experiencia requerida")

col1,col2,col3 = st.columns(3)

with col1:

    anos_min = st.number_input(
        "🔴 Años mínimos *",
        0,
        20,
        3
    )

with col2:

    anos_ideal = st.number_input(
        "🔴 Años ideales *",
        0,
        30,
        5
    )

with col3:

    seniority = st.selectbox(

        "🔴 Seniority esperado *",

        [

            "",

            "Junior",

            "Semi Senior",

            "Senior",

            "Lead",

            "Manager"

        ]

    )

experiencia = st.multiselect(

    "🔴 Tipo de experiencia obligatoria *",

    [

        "Implantaciones",

        "Roll Outs",

        "Migraciones ECC → S/4HANA",

        "Greenfield",

        "Brownfield",

        "AMS",

        "Soporte Correctivo",

        "Soporte Evolutivo",

        "Mantenimiento",

        "Preventa",

        "Arquitectura",

        "Integraciones",

        "Upgrade",

        "Hypercare"

    ]

)

experiencia_valorable = st.multiselect(

    "Experiencia valorable (opcional)",

    [

        "Implantaciones",

        "Roll Outs",

        "Greenfield",

        "Brownfield",

        "AMS",

        "Arquitectura",

        "Integraciones",

        "Preventa",

        "Hypercare"

    ]

)

st.divider()

# ----------------------------------------------------------
# 5. FUNCIONES
# ----------------------------------------------------------

st.header("5. Funciones del puesto")

funciones = st.text_area(

    "🔴 Funciones imprescindibles (mínimo cinco) *",

    height=180,

    placeholder="""

Ejemplo

• Liderar implantaciones SAP CO

• Contacto con negocio

• Diseño funcional

• Configuración del sistema

• Formación a usuarios

"""

)

funciones_valorables = st.text_area(

    "Funciones valorables (opcional)",

    height=120

)

st.divider()

# ----------------------------------------------------------
# 6. IDIOMAS
# ----------------------------------------------------------

st.header("6. Idiomas")

col1,col2 = st.columns(2)

with col1:

    ingles = st.selectbox(

        "🔴 Inglés *",

        [

            "",

            "No requerido",

            "Valorable",

            "Obligatorio"

        ]

    )

with col2:

    nivel_ingles = st.selectbox(

        "🔴 Nivel requerido *",

        [

            "",

            "A1",

            "A2",

            "B1",

            "B2",

            "C1",

            "C2",

            "Nativo"

        ]

    )

otros = st.text_input(

    "Otros idiomas (opcional)"

)

    st.divider()

   # ----------------------------------------------------------
# 7. CONDICIONES DEL PUESTO
# ----------------------------------------------------------

st.header("7. Condiciones del puesto")

col1,col2 = st.columns(2)

with col1:

    ubicacion = st.text_input(
        "🔴 Ubicación *"
    )

    modalidad = st.selectbox(

        "🔴 Modalidad *",

        [

            "",

            "Presencial",

            "Híbrida",

            "Remota"

        ]

    )

    presencialidad = st.text_input(

        "🔴 Días de presencialidad *",

        placeholder="Ejemplo: 2 días"

    )

with col2:

    viajes = st.radio(

        "🔴 Disponibilidad para viajar *",

        [

            "Sí",

            "No"

        ]

    )

    incorporacion = st.date_input(

        "🔴 Fecha prevista incorporación *",

        value=date.today()

    )

    contrato = st.selectbox(

        "🔴 Tipo de contrato *",

        [

            "",

            "Indefinido",

            "Temporal",

            "Freelance",

            "Subcontratación"

        ]

    )

salario = st.text_input(

    "🔴 Banda salarial *",

    placeholder="Ejemplo: 55.000 - 65.000 €"

)

st.divider()

# ----------------------------------------------------------
# PRIORIZACIÓN
# ----------------------------------------------------------

st.header("8. Priorización de requisitos")

prioridad = st.text_area(

    "🔴 Indique qué requisitos son Obligatorios, Muy Valorables y Deseables *",

    height=180,

    placeholder="""

Obligatorio

- SAP CO

- S/4HANA

Muy Valorable

- CO-PA

- Public Cloud

Deseable

- SAC

"""

)

st.divider()

# ----------------------------------------------------------
# DESCARTE
# ----------------------------------------------------------

st.header("9. Requisito de descarte")

descarte = st.text_area(

    "Requisito de descarte (opcional)",

    height=120,

    placeholder="""

Ejemplos

No haber trabajado en S/4HANA

No disponer de inglés B2

No aceptar modalidad híbrida

"""

)

st.divider()

# ----------------------------------------------------------
# OBSERVACIONES
# ----------------------------------------------------------

st.header("10. Observaciones")

observaciones = st.text_area(

    "Observaciones adicionales",

    height=180

)

st.divider()

enviar = st.form_submit_button(

    "📨 Enviar solicitud"

)

    st.divider()

    enviar = st.form_submit_button(
        "Guardar solicitud"
    )

if enviar:

    errores=[]

    if nombre.strip()=="":
        errores.append("Nombre")

    if cargo.strip()=="":
        errores.append("Cargo")

    if departamento.strip()=="":
        errores.append("Departamento")

    if puesto.strip()=="":
        errores.append("Nombre del puesto")
    
    if modulo == "":
    errores.append("Módulo principal SAP")

if len(soluciones) == 0:
    errores.append("Soluciones SAP obligatorias")

if len(tecnologias) == 0:
    errores.append("Tecnologías obligatorias")
    
if seniority == "":
    errores.append("Seniority")

if len(experiencia) == 0:
    errores.append("Experiencia obligatoria")

if funciones.strip() == "":
    errores.append("Funciones imprescindibles")

if ingles == "":
    errores.append("Nivel de inglés")

if nivel_ingles == "":
    errores.append("Nivel requerido")
    if len(errores)>0:
if ubicacion.strip()=="":
    errores.append("Ubicación")

if modalidad=="":
    errores.append("Modalidad")

if presencialidad.strip()=="":
    errores.append("Presencialidad")

if contrato=="":
    errores.append("Tipo de contrato")

if salario.strip()=="":
    errores.append("Banda salarial")

if prioridad.strip()=="":
    errores.append("Priorización")
        st.error(
            "Debe completar:\n\n- " +
            "\n- ".join(errores)
        )

else:

    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    contenido = []

    contenido.append(
        Paragraph(
            "<b>SOLICITUD DE PERFIL SAP</b>",
            styles["Title"]
        )
    )

    contenido.append(
        Paragraph("<br/>", styles["BodyText"])
    )

    campos = {

        "Nombre": nombre,
        "Cargo": cargo,
        "Departamento": departamento,
        "Fecha": str(fecha),

        "Puesto": puesto,
        "Motivo": motivo,
        "Vacantes": vacantes,

        "Módulo
        # ----------------------------------------------------------
# 3. REQUISITOS TÉCNICOS
# ----------------------------------------------------------

st.header("3. Requisitos Técnicos")

modulo = st.selectbox(

    "🔴 Módulo principal SAP *",

    [

        "",

        "SAP FI",
        "SAP CO",
        "SAP SD",
        "SAP MM",
        "SAP PP",
        "SAP PM",
        "SAP PS",
        "SAP QM",
        "SAP WM",
        "SAP EWM",
        "SAP TM",
        "SAP GTS",
        "SAP SuccessFactors",
        "SAP Ariba",
        "SAP IBP",
        "SAP Basis",
        "SAP Security",
        "SAP ABAP",
        "SAP BTP",
        "SAP BW",
        "SAP BW/4HANA",
        "SAP SAC",
        "SAP Datasphere",
        "SAP Fiori",
        "SAP CX",
        "SAP CRM",
        "SAP IS-U",
        "SAP Retail"

    ]

)

submodulos = st.text_area(

    "Submódulos (opcional)",

    placeholder="Ejemplo: CO-PA, CO-PC, FI-AA..."

)

modulos_valorables = st.text_area(

    "Módulos/Submódulos valorables (opcional)"

)

st.subheader("Soluciones SAP")

soluciones = st.multiselect(

    "🔴 Soluciones SAP obligatorias *",

    [

        "SAP ECC",

        "SAP S/4HANA",

        "SAP S/4HANA Public Cloud",

        "SAP S/4HANA Private Cloud",

        "SAP BTP",

        "SAP BW",

        "SAP BW/4HANA",

        "SAP SAC",

        "SAP Datasphere",

        "SAP Fiori",

        "SAP Integration Suite (CPI)",

        "SAP Signavio",

        "SAP Build",

        "SAP MDG",

        "SAP Solution Manager"

    ]

)

soluciones_valorables = st.multiselect(

    "Soluciones SAP valorables (opcional)",

    [

        "SAP ECC",

        "SAP S/4HANA",

        "SAP BTP",

        "SAP BW",

        "SAP SAC",

        "SAP Datasphere",

        "SAP Fiori",

        "SAP Signavio",

        "SAP Build",

        "SAP MDG"

    ]

)

st.subheader("Tecnologías")

tecnologias = st.multiselect(

    "🔴 Herramientas/Tecnologías obligatorias *",

    [

        "ABAP",

        "ABAP OO",

        "RAP",

        "CDS Views",

        "AMDP",

        "OData",

        "Gateway",

        "Fiori",

        "Fiori Elements",

        "SAPUI5",

        "UI5",

        "BAPI",

        "RFC",

        "IDOC",

        "ALE",

        "Enhancements",

        "SmartForms",

        "Adobe Forms",

        "Migration Cockpit",

        "LSMW",

        "CPI",

        "PI/PO",

        "BTP",

        "CAP",

        "Business Application Studio",

        "Eclipse ADT",

        "Solution Manager",

        "ChaRM",

        "Jira",

        "Azure DevOps",

        "ServiceNow"

    ]

)

tecnologias_valorables = st.multiselect(

    "Herramientas/Tecnologías valorables (opcional)",

    [

        "ABAP",

        "RAP",

        "CDS Views",

        "OData",

        "SAPUI5",

        "Fiori",

        "CAP",

        "BTP",

        "Jira",

        "Azure DevOps",

        "ServiceNow",

        "Signavio"

    ]

)
