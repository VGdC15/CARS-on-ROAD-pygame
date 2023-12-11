import json

#función para leer datos desde un archivo JSON
def leer_data(archivo: str) -> list:
    try:
        # Utiliza un bloque 'with' para garantizar que el archivo se cierre correctamente después de su uso
        with open(archivo, "r", encoding='utf-8') as file:
            data = json.load(file)  # Convierte el JSON en un diccionario de Python

        # Obtiene la lista de puntuaciones del diccionario o una lista vacía si no hay datos
        list_score = data.get("ranking", [])

    except FileNotFoundError:
        print(f"Error: El archivo '{archivo}' no se encontró.")
        list_score = []  # En caso de que el archivo no se encuentre, devuelve una lista vacía
    except json.JSONDecodeError:
        print(f"Error: No se pudo decodificar el JSON en '{archivo}'.")
        list_score = []  # En caso de que haya un problema al decodificar el JSON, devuelve una lista vacía

    return list_score

# Define una función para guardar datos en un archivo JSON
def guardar_data(ranking: list, nombre, score):
    try:
        # Agrega una nueva entrada al ranking
        ranking.append({"name": nombre, "score": score})

        # Abre el archivo en modo de escritura y escribir el nuevo ranking en formato JSON
        with open("programacion\ejercicios\juego_2\data.json", 'w', encoding='utf-8') as file:
            json.dump({"ranking": ranking}, file, indent=4)

    except FileNotFoundError:
        print("Error: El archivo no se encontró.")
    except json.JSONDecodeError:
        print("Error: No se pudo decodificar el JSON.")
    except Exception:
        print(f"Error inesperado")


def ordenar_puntuacion_descendente(archivo: str, clave: str):
    try:
        # Determina el tipo de archivo basándose en la extensión
        extension = archivo.split('.')[-1].lower()

        if extension == 'json':
            # Lee el archivo JSON
            with open(archivo, 'r', encoding='utf-8') as jsonfile:
                lista_recibida = json.load(jsonfile)

            # Verifica si la clave es válida
            if 'ranking' not in lista_recibida or not lista_recibida['ranking']:
                print("La clave 'ranking' no es válida o la lista está vacía.")
                return lista_recibida

            # Verifica si la clave especificada está presente en al menos un elemento de la lista
            if not all(clave in item for item in lista_recibida['ranking']):
                print(f"La clave '{clave}' no está presente en al menos un elemento de la lista.")
                return lista_recibida

            # Verifica si el valor correspondiente es numérico
            if not all(str(item[clave]).isdigit() or str(item[clave]) == "" for item in lista_recibida['ranking']):
                print(f"El valor correspondiente a la clave '{clave}' no es numérico.")
                return lista_recibida

            # Ordena la lista por la clave especificada de manera descendente
            lista_recibida['ranking'].sort(key=lambda x: int(x[clave]), reverse=True)

        else:
            print(f"Formato de archivo no compatible: {extension}")
            return []

        return lista_recibida

    except FileNotFoundError:
        print(f"El archivo {archivo} no fue encontrado.")
        return []
    except Exception:
        print(f"Se ha producido un error inesperado")
        return []

