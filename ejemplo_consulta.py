"""
Archivo: ejemplo_consulta.py
Autor: @oswaldom_code
Descripción: Lee un archivo.csv que contiene dos columnas (nacionalidad y cedula) y haciendo uso
de la clase persona_cne.py obtiene el nombre completo de la persona, adicionalmente el estado, municipio
y la parroquia donde se encentra  registrado para ejercer el voto.
"""
import persona_cne as cne
import csv

if __name__ == '__main__':
    # Apertura del archivo
    with open('buscar.csv', newline='', encoding='utf8') as csvfile_entrada:
        reader = csv.DictReader(csvfile_entrada, delimiter=',')  # Create object reader of DirectReader type

        # Se recorre las filas del archivo.csv
        for row in reader:
            persona = cne.persona()  # Create object  persona type
            # Asociación de las variables con los titulos de las columnas
            nacionalidad = row['nacionalidad']
            cedula = row['cedula']

            persona.consulta(nacionalidad, cedula)
            if persona.status:
                print(nacionalidad + cedula + "|" + persona.get_full_name() + "|" + persona.get_state() + "|" +
                      persona.get_municipality())
            else:
                pass

            del persona

        csvfile_entrada.close()
        del csvfile_entrada

