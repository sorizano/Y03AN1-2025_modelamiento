import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 

#Función para autenticación
def check_password():
    def password_entered():
        if st.session_state["password"] == "qwerty123":
            st.session_state["password_correct"] = True
            del st.session_state["password"] #para Seguridad
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        st.text_input(
            "Introduce la contraseña", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        st.error("Contraseña incorrecta")
        return False
    else:
        return True

#verifica la contraseña antes de continuar
if check_password():
    st.title("Visualicación de Datos de ventas y clientes")

    #cargar del archivo CSV
    uploaded_file = st.file_uploader("Sube un archivo CSV", type=["csv"])

    if uploaded_file is not None:
        df= pd.read_csv(uploaded_file)
        st.write("Vista previa del DataFrame", df.head())

        #Selección de gráficos
        st.siderbar.header("Configuración de gráficos")
        chart_type = st.siderbar.selectbox("Selecciona el tipo de gráfico", ["Barras", "Líneas", "Histograma"])

        # Selección de columnas para los ejes
        x_col = st.sidebar.selectbox("Selecciona la columna para el eje X", df.columns)
        y_col = st.sidebar.selectbox("Selecciona la columna para el eje Y", df.columns)

        # Gráfico de barras
        if chart_type == "Barras":
            st.subheader(f"Gráfico de {chart_type}")
            plt.figure(figsize=(10,5))
            plt.bar(df[x_col], df[y_col])
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            st.pyplot(plt)
        
        # Gráfico de líneas
        elif chart_type == "Líneas":
            st.subheader(f"Gráfico de {chart_type}")
            plt.figure(figsize=(10,5))
            plt.plot(df[x_col], df[y_col])
            plt.xlabel(x_col)
            plt.ylabel(y_col)
            st.pyplot(plt)