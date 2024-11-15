import streamlit as st
import pandas as pd
import requests

# Título de la aplicación
st.title('Aplicación Web: Datos desde una API REST')

def obtener_datos_api(api_url):
 """Función que realiza la petición a la API y devuelve un
 DataFrame."""
 response = requests.get(api_url)
 if response.status_code == 200:
  data = response.json()
  return pd.DataFrame(data)
 else:
  st.error('Error al obtener los datos de la API')
  return None
  
# URL de la API REST (puedes cambiarla por cualquier API pública que devuelva JSON)
api_url = 'https://jsonplaceholder.typicode.com/posts' 
# Llamar la función para obtener los datos
df = obtener_datos_api(api_url)
# Si hay datos, mostrar el DataFrame, mostrar dataframe con las columnas seleccionadas, permitir filtrado y mostrar gráficos.

if df is not None:
 df = pd.DataFrame(data)
 # Mostrar los primeros registros
 st.write('Datos obtenidos de la API:')
 st.write(df.head())
 # Seleccionar una columna para mostrar en Streamlit
 columnas = st.multiselect('Selecciona las columnas a visualizar',
 df.columns.tolist(), default=df.columns.tolist())
 df_seleccionado = df[columnas]
 # Mostrar el DataFrame con las columnas seleccionadas
 st.write('Datos seleccionados:')
 st.write(df_seleccionado)
 # Filtro por ID
 id_filtro = st.slider('Filtrar por ID (entre 1 y 100)', 1, 100, 50)
 df_filtrado = df[df['id'] <= id_filtro]
 st.write(f'Mostrando datos donde ID <= {id_filtro}:')
 st.write(df_filtrado)
