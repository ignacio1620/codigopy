import streamlit as st
import pandas as pd
import requests

# Título de la aplicación
st.title('Aplicación Web: Datos desde una API REST')
# URL de la API REST (puedes cambiarla por cualquier API pública que devuelva JSON)
api_url = 'https://jsonplaceholder.typicode.com/posts'
# Realizar la petición a la API
response = requests.get(api_url)
# Verificar que la respuesta sea exitosa (código 200)
if response.status_code == 200:
 # Convertir los datos JSON en un DataFrame de Pandas
 data = response.json()
 df = pd.DataFrame(data)
 # Mostrar los primeros registros
 st.write('Datos obtenidos de la API:')
 st.write(df.head())
else:
 st.error('Error al obtener los datos de la API')
