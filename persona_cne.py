"""
# Archivo: persona_cne.py
# Autor: @oswaldom_code
# Descripción: Clase que me permite manejar las consultas a la web del cne.org.ve y obtener datos de
# ella haciendo un raspado con BeautifulSoup.
"""

import requests
from bs4 import BeautifulSoup


class persona():
    def __init__(self):
        self.nationality = ''
        self.id = ''
        self.__full_name = ''
        self.__state = ''
        self.__municipality = ''
        self.__parish = ''
        self.status = False

############################################################
#   Metodos para acceder a los atributos del objeto persona
############################################################
    def get_nationalidad(self):# Nacionalidad V:Venezolano / E:Extranjero
        return self.nationality

    def get_id(self):# Número de identificación ciudadana (Cédula)
        return self.id

    def get_full_name(self):# Nombre completo de la persona
        return self.__full_name

    def get_state(self):# Estado donde se encuentra registrado para ejercer el voto
        return self.__state

    def get_municipality(self):# Estado donde se encuentra registrado para ejercer el voto
        return self.__municipality

    def get_parish(self):
        return self.__parish

    def get_status(self):
        return self.status
#################################################################################################
#   consulta(self, id_nacionalidad, id_cedula) realiza un requests a cne.gob.ve para raspar los
#   datos correspondientes.
#################################################################################################

    def consulta(self, id_nacionalidad, id_cedula):
        # Construye la url objetivo para el raspado de los datos
        url = "http://www.cne.gob.ve/web/registro_electoral/ce.php?nacionalidad=" + id_nacionalidad.capitalize() \
              + "&cedula=" + id_cedula

        global requests

        response = requests.get(url)

        # Parseamos el HTML
        soup = BeautifulSoup(response.content, "html.parser")

        if response.status_code == 200:

            # Llama a __validar(self, argumento) para validar el contenido del <td> 19 del árbol HTML
            if self.__validar(self, soup.find_all('td')[19].text):
                print('Uff! creo que hay algo mal con este último registro:', id_cedula)

            else:
                # soup.find busca entre las etiquetas de la estructura HTML
                self.__full_name = soup.find_all('td')[13].text
                self.__state = soup.find_all('td')[15].text
                self.__municipality = soup.find_all('td')[17].text
                self.__parish = soup.find_all('td')[19].text
                self.status = True
        else:
            print("Error de conexión: Codigo ", response.status_code)
            self.consulta(self, id_nacionalidad, id_cedula)

############################################################################################################
#   Valida el contenido del <td> 19 del árbol HTML.
#   Según el análisis realizado a la estructura de la web, la etiqueta <td> 19 del árbol, para una búsqueda
#   exitosa nunca deberá contener las cadenas “Objeción: FALLECIDO (3)”, “RECOMENDACIONES” o “\x08” –Vacío-
#
#   En tal caso retorna True, para indicar que algo va mal.
#  ########################################################################################################
    @staticmethod
    def __validar(self, argumento):
        if argumento == "Objeción: FALLECIDO (3)" or argumento == "RECOMENDACIONES" or argumento == "\x08":
            return True
        else:
            return False
