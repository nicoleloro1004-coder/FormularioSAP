import streamlit as st
from datetime import date

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph
)

from reportlab.lib.styles import getSampleStyleSheet

st.set_page_config(
    page_title="Solicitud Perfil SAP",
    page_icon="📋",
    layout="wide"
)

st.title("📋 Formulario de Solicitud de Perfil SAP")

st.markdown("Complete toda la información antes de enviar la solicitud.")

st.header("1. Datos del solicitante")

nombre = st.text_input("Nombre y apellidos")
cargo = st.text_input("Cargo")
departamento = st.text_input("Departamento")
fecha = st.date_input("Fecha de solicitud", value=date.today())

st.header("2. Información de la posición")

puesto = st.text_input("Nombre completo del puesto")

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

st.header("3. Requisitos técnicos")

modulo = st.text_input("Módulo principal SAP")

submodulos = st.text_area("Submódulos obligatorios")

soluciones = st.multiselect(
    "Soluciones SAP obligatorias",
    [
        "SAP ECC",
        "SAP S/4HANA",
        "SAP S/4HANA Public Cloud",
        "SAP S/4HANA Private Cloud",
        "SAP BTP",
        "SAP BW",
        "SAP BW4HANA",
        "SAP SAC",
        "SAP Datasphere",
        "SAP Fiori",
        "SAP CPI"
    ]
)

tecnologias = st.multiselect(
    "Herramientas obligatorias",
    [
        "ABAP",
        "RAP",
        "CDS Views",
        "OData",
        "UI5",
        "Migration Cockpit",
        "Solution Manager",
        "Jira",
        "Azure DevOps",
        "ServiceNow"
    ]
)

st.header("4. Experiencia")

anos_min = st.number_input("Años mínimos", 0,20,3)

anos_ideal = st.number_input("Años ideales",0,30,5)

seniority = st.selectbox(
    "Seniority",
    [
        "Junior",
        "Semi Senior",
        "Senior",
        "Lead",
        "Manager"
    ]
)

experiencia = st.multiselect(
    "Experiencia obligatoria",
    [
        "Implantaciones",
        "Roll Outs",
        "Migraciones ECC-S4",
        "Greenfield",
        "Brownfield",
        "AMS",
        "Soporte Correctivo",
        "Soporte Evolutivo",
        "Mantenimiento",
        "Preventa"
    ]
)

st.header("5. Funciones")

funciones = st.text_area(
    "Funciones imprescindibles (mínimo cinco)"
)

funciones_valorables = st.text_area(
    "Funciones valorables"
)

st.header("6. Idiomas")

ingles = st.selectbox(
    "Nivel Inglés",
    [
        "No requerido",
        "Valorable",
        "Obligatorio"
    ]
)

otros = st.text_input("Otros idiomas")

st.header("7. Condiciones")

ubicacion = st.text_input("Ubicación")

modalidad = st.selectbox(
    "Modalidad",
    [
        "Presencial",
        "Híbrida",
        "Remota"
    ]
)

presencialidad = st.text_input("Días de presencialidad")

viajes = st.radio(
    "Disponibilidad para viajar",
    [
        "Sí",
        "No"
    ]
)

incorporacion = st.date_input("Fecha incorporación")

contrato = st.text_input("Tipo de contrato")

salario = st.text_input("Banda salarial")

st.header("8. Priorización")

prioridad = st.text_area(
    "Indique los requisitos obligatorios, muy valorables y deseables."
)

st.header("9. Requisito de descarte")

descarte = st.text_area(
    "¿Qué requisito descarta automáticamente al candidato?"
)

st.header("10. Observaciones")

observaciones = st.text_area("Observaciones adicionales")

if st.button("Guardar formulario"):

    datos = {
        "Nombre":[nombre],
        "Cargo":[cargo],
        "Departamento":[departamento],
        "Fecha":[fecha],
        "Puesto":[puesto],
        "Motivo":[motivo],
        "Vacantes":[vacantes],
        "Modulo SAP":[modulo],
        "Submodulos":[submodulos],
        "Soluciones":[", ".join(soluciones)],
        "Tecnologías":[", ".join(tecnologias)],
        "Años mínimos":[anos_min],
        "Años ideales":[anos_ideal],
        "Seniority":[seniority],
        "Experiencia":[", ".join(experiencia)],
        "Funciones":[funciones],
        "Funciones valorables":[funciones_valorables],
        "Inglés":[ingles],
        "Otros idiomas":[otros],
        "Ubicación":[ubicacion],
        "Modalidad":[modalidad],
        "Presencialidad":[presencialidad],
        "Viajes":[viajes],
        "Incorporación":[incorporacion],
        "Contrato":[contrato],
        "Salario":[salario],
        "Priorización":[prioridad],
        "Requisito descarte":[descarte],
        "Observaciones":[observaciones]
    }

    df = pd.DataFrame(datos)

    archivo = "Solicitud_SAP.xlsx"

    df.to_excel(archivo,index=False)

    with open(archivo,"rb") as file:
        st.download_button(
            "Descargar Solicitud",
            file,
            archivo
        )

    st.success("Formulario generado correctamente.")
