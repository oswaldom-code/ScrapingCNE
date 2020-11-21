"""
Autor: @OSWALDOM-CODE
DESCRIPCIÓN: Código que hace escraping a la web del Consejo Nacional Electoral de Venezuela
para capturar datos básicos de los ciudadanos registrados dado su número de identidad 
(nombre completo, Centro electoral, Estado, Municipio).
"""

# requiere python3

import requests
from bs4 import BeautifulSoup

# Url destino
url_semilla = "http://www.cne.gob.ve/web/registro_electoral/ce.php?"

# Parámetros a incluir en la url 
nacionalidad = 'V'
cedula = '16132256'

# Url final
url_compuesta = url_semilla + 'nacionalidad=' + nacionalidad + '&' + 'cedula=' + cedula

# Petición
requests = requests.get(url_compuesta)

# Tomamos el requests, lo parseamos a html para obtener un tipo de dato soup
soup = BeautifulSoup(requests.content, "html.parser") 

# status_code 200 es OK, en caso contrario web no disponible he imprimimos mensaje y codigo de error
if requests.status_code == 200:      
    contenList = []

    for contenido  in soup.find_all('td')[10: 24]:# 10:24 los <td> del arbol que nos interesa
        dato = contenido.text
        contenList.append(dato.strip())

    datosPersona = '\nCedula:' + contenList[1] + '\n' + 'Nombre y Apellido: ' + contenList[3]
    datosCentro  =  '\nEsdato:' + contenList[5] + '\n' + 'Municipio: ' + contenList[7]
 
    print(datosPersona + datosCentro)
  
else:
    print("Error de conexión: Código ", requests.status_code)


