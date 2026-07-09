import streamlit as st
from datetime import date
from io import BytesIO
from PIL import Image

from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

# --------------------------------------------------
# CONFIGURACIÓN
# --------------------------------------------------

st.set_page_config(
    page_title="Solicitud Perfil SAP",
    page_icon="📋",
    layout="wide"
)

# --------------------------------------------------
# ESTILO
# --------------------------------------------------

st.markdown("""
<style>

.stApp{
    background:#F5F7FA;
}

h1{
    color:#0057B8;
}

h2{
    color:#0057B8;
}

.stButton>button{
    background:#0057B8;
    color:white;
    width:100%;
    height:45px;
    border-radius:8px;
}

.stButton>button:hover{
    background:#3BB7A5;
    color:white;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# LOGO
# --------------------------------------------------

try:
    logo = Image.open("assets/logo_altim.png")

    c1,c2 = st.columns([1,4])

    with c1:
        st.image(logo,width=150)

    with c2:
        st.title("Portal de Solicitud de Perfil SAP")
        st.write("Complete todos los campos obligatorios antes de enviar la solicitud.")

except:
    st.title("Portal de Solicitud de Perfil SAP")

st.divider()

# --------------------------------------------------
# FORMULARIO
# --------------------------------------------------

with st.form("formulario_sap"):

    # ==============================================
    # 1. SOLICITANTE
    # ==============================================

    st.header("1. Datos del solicitante")

    col1,col2 = st.columns(2)

    with col1:

        nombre = st.text_input(
            "Nombre y apellidos *"
        )

        cargo = st.text_input(
            "Cargo *"
        )

    with col2:

        departamento = st.text_input(
            "Departamento *"
        )

        fecha = st.date_input(
            "Fecha",
            value=date.today()
        )

    st.divider()

    # ==============================================
    # 2. POSICIÓN
    # ==============================================

    st.header("2. Información de la posición")

    puesto = st.text_input(
        "Nombre del puesto *"
    )

    motivo = st.selectbox(

        "Motivo de la contratación",

        [

            "Nueva posición",

            "Sustitución",

            "Incremento de equipo",

            "Proyecto específico"

        ]

    )

    vacantes = st.number_input(

        "Número de vacantes",

        min_value=1,

        value=1

    )

    st.divider()

    # ==============================================
    # 3. REQUISITOS SAP
    # ==============================================

    st.header("3. Requisitos técnicos")

    modulo = st.selectbox(

        "Módulo principal SAP *",

        [

            "",

            "FI",

            "CO",

            "MM",

            "SD",

            "PP",

            "PS",

            "PM",

            "QM",

            "EWM",

            "TM",

            "ABAP",

            "Basis",

            "SuccessFactors",

            "Ariba",

            "BTP"

        ]

    )

    submodulos = st.text_area(
        "Submódulos (opcional)"
    )

    modulos_valorables = st.text_area(
        "Módulos valorables (opcional)"
    )

    soluciones = st.multiselect(

        "Soluciones SAP obligatorias *",

        [

            "SAP ECC",

            "SAP S/4HANA",

            "SAP Public Cloud",

            "SAP Private Cloud",

            "SAP BW",

            "SAP SAC",

            "SAP Datasphere",

            "SAP BTP",

            "SAP Fiori"

        ]

    )

    soluciones_valorables = st.multiselect(

        "Soluciones SAP valorables (opcional)",

        [

            "SAP ECC",

            "SAP S/4HANA",

            "SAP BW",

            "SAP SAC",

            "SAP Datasphere"

        ]

    )
        st.subheader("Herramientas y tecnologías")

    tecnologias = st.multiselect(

        "Herramientas obligatorias *",

        [

            "ABAP",
            "ABAP OO",
            "RAP",
            "CDS Views",
            "OData",
            "SAPUI5",
            "Fiori",
            "Migration Cockpit",
            "BTP",
            "CPI",
            "Jira",
            "Azure DevOps",
            "ServiceNow"

        ]

    )

    tecnologias_valorables = st.multiselect(

        "Herramientas valorables (opcional)",

        [

            "ABAP",
            "RAP",
            "CDS Views",
            "OData",
            "SAPUI5",
            "Fiori",
            "BTP",
            "Jira",
            "Azure DevOps",
            "ServiceNow"

        ]

    )

    st.divider()

    # ==============================================
    # 4. EXPERIENCIA
    # ==============================================

    st.header("4. Experiencia")

    col1,col2,col3 = st.columns(3)

    with col1:

        anos_min = st.number_input(
            "Años mínimos *",
            0,
            20,
            3
        )

    with col2:

        anos_ideal = st.number_input(
            "Años ideales *",
            0,
            30,
            5
        )

    with col3:

        seniority = st.selectbox(

            "Seniority *",

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

        "Experiencia obligatoria *",

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

            "Preventa"

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

            "Preventa"

        ]

    )

    st.divider()

    # ==============================================
    # 5. FUNCIONES
    # ==============================================

    st.header("5. Funciones")

    funciones = st.text_area(

        "Funciones imprescindibles *",

        height=170

    )

    funciones_valorables = st.text_area(

        "Funciones valorables (opcional)",

        height=120

    )

    st.divider()

    # ==============================================
    # 6. IDIOMAS
    # ==============================================

    st.header("6. Idiomas")

    col1,col2 = st.columns(2)

    with col1:

        ingles = st.selectbox(

            "Nivel de inglés *",

            [

                "",

                "No requerido",

                "Valorable",

                "Obligatorio"

            ]

        )

    with col2:

        nivel_ingles = st.selectbox(

            "Nivel requerido *",

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
    # ==============================================
    # 7. CONDICIONES DEL PUESTO
    # ==============================================

    st.header("7. Condiciones del puesto")

    col1, col2 = st.columns(2)

    with col1:

        ubicacion = st.text_input(
            "Ubicación *"
        )

        modalidad = st.selectbox(

            "Modalidad *",

            [

                "",

                "Presencial",

                "Híbrida",

                "Remota"

            ]

        )

        presencialidad = st.text_input(

            "Días de presencialidad *"

        )

    with col2:

        viajes = st.radio(

            "Disponibilidad para viajar *",

            [

                "Sí",

                "No"

            ]

        )

        incorporacion = st.date_input(

            "Fecha prevista de incorporación",

            value=date.today()

        )

        contrato = st.selectbox(

            "Tipo de contrato *",

            [

                "",

                "Indefinido",

                "Temporal",

                "Freelance",

                "Subcontratación"

            ]

        )

    salario = st.text_input(

        "Banda salarial *"

    )

    st.divider()

    # ==============================================
    # 8. PRIORIZACIÓN
    # ==============================================

    st.header("8. Priorización de requisitos")

    prioridad = st.text_area(

        "Indique qué requisitos son Obligatorios, Muy Valorables y Deseables *",

        height=180

    )

    st.divider()

    # ==============================================
    # 9. REQUISITO DE DESCARTE
    # ==============================================

    st.header("9. Requisito de descarte")

    descarte = st.text_area(

        "Requisito de descarte (opcional)",

        height=120

    )

    st.divider()

    # ==============================================
    # 10. OBSERVACIONES
    # ==============================================

    st.header("10. Observaciones")

    observaciones = st.text_area(

        "Observaciones adicionales",

        height=150

    )

    st.divider()

    # ==============================================
    # BOTÓN
    # ==============================================

    enviar = st.form_submit_button(

        "📨 Enviar solicitud"

    )

# ==================================================
# VALIDACIÓN
# ==================================================

if enviar:

    errores = []

    if nombre.strip() == "":
        errores.append("Nombre y apellidos")

    if cargo.strip() == "":
        errores.append("Cargo")

    if departamento.strip() == "":
        errores.append("Departamento")

    if puesto.strip() == "":
        errores.append("Nombre del puesto")

    if modulo == "":
        errores.append("Módulo principal SAP")

    if len(soluciones) == 0:
        errores.append("Soluciones SAP obligatorias")

    if len(tecnologias) == 0:
        errores.append("Herramientas obligatorias")

    if seniority == "":
        errores.append("Seniority")

    if len(experiencia) == 0:
        errores.append("Experiencia obligatoria")

    if funciones.strip() == "":
        errores.append("Funciones imprescindibles")

    if ingles == "":
        errores.append("Inglés")

    if nivel_ingles == "":
        errores.append("Nivel de inglés")

    if ubicacion.strip() == "":
        errores.append("Ubicación")

    if modalidad == "":
        errores.append("Modalidad")

    if presencialidad.strip() == "":
        errores.append("Presencialidad")

    if contrato == "":
        errores.append("Tipo de contrato")

    if salario.strip() == "":
        errores.append("Banda salarial")

    if prioridad.strip() == "":
        errores.append("Priorización")

    if errores:

        st.error(
            "Debe completar los siguientes campos:\n\n- " +
            "\n- ".join(errores)
        )

    else:

        st.success("✅ Formulario validado correctamente.")
        # ==============================================
        # GENERACIÓN DEL PDF
        # ==============================================

        buffer = BytesIO()

        doc = SimpleDocTemplate(buffer)

        styles = getSampleStyleSheet()

        elementos = []

        elementos.append(
            Paragraph(
                "<b><font size='18'>SOLICITUD DE PERFIL SAP</font></b>",
                styles["Title"]
            )
        )

        elementos.append(
            Paragraph("<br/><br/>", styles["BodyText"])
        )

        datos = [

            ("DATOS DEL SOLICITANTE", None),

            ("Nombre", nombre),
            ("Cargo", cargo),
            ("Departamento", departamento),
            ("Fecha", str(fecha)),

            ("INFORMACIÓN DE LA POSICIÓN", None),

            ("Puesto", puesto),
            ("Motivo", motivo),
            ("Vacantes", str(vacantes)),

            ("REQUISITOS TÉCNICOS", None),

            ("Módulo principal", modulo),
            ("Submódulos", submodulos),
            ("Módulos valorables", modulos_valorables),
            ("Soluciones obligatorias", ", ".join(soluciones)),
            ("Soluciones valorables", ", ".join(soluciones_valorables)),
            ("Tecnologías obligatorias", ", ".join(tecnologias)),
            ("Tecnologías valorables", ", ".join(tecnologias_valorables)),

            ("EXPERIENCIA", None),

            ("Años mínimos", str(anos_min)),
            ("Años ideales", str(anos_ideal)),
            ("Seniority", seniority),
            ("Experiencia obligatoria", ", ".join(experiencia)),
            ("Experiencia valorable", ", ".join(experiencia_valorable)),

            ("FUNCIONES", None),

            ("Funciones imprescindibles", funciones),
            ("Funciones valorables", funciones_valorables),

            ("IDIOMAS", None),

            ("Inglés", ingles),
            ("Nivel requerido", nivel_ingles),
            ("Otros idiomas", otros),

            ("CONDICIONES", None),

            ("Ubicación", ubicacion),
            ("Modalidad", modalidad),
            ("Presencialidad", presencialidad),
            ("Disponibilidad para viajar", viajes),
            ("Fecha incorporación", str(incorporacion)),
            ("Tipo de contrato", contrato),
            ("Banda salarial", salario),

            ("PRIORIZACIÓN", None),

            ("Priorización", prioridad),

            ("REQUISITO DE DESCARTE", None),

            ("Descarte", descarte),

            ("OBSERVACIONES", None),

            ("Observaciones", observaciones)

        ]

        for titulo, valor in datos:

            if valor is None:

                elementos.append(
                    Paragraph("<br/>", styles["BodyText"])
                )

                elementos.append(
                    Paragraph(
                        f"<b><font size='14'>{titulo}</font></b>",
                        styles["Heading2"]
                    )
                )

            else:

                texto = valor if str(valor).strip() != "" else "-"

                elementos.append(
                    Paragraph(
                        f"<b>{titulo}:</b> {texto}",
                        styles["BodyText"]
                    )
                )

        doc.build(elementos)

        pdf = buffer.getvalue()

        buffer.close()

        st.download_button(

            label="📄 Descargar Solicitud en PDF",

            data=pdf,

            file_name="Solicitud_Perfil_SAP.pdf",

            mime="application/pdf"

        )

        st.success(
            "La solicitud se ha generado correctamente."
        )
    
