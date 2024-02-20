def leer_archivo(buscar_archivo):
    try:
        with open(buscar_archivo, 'r') as archivo:
            caracter = archivo.read()
        return caracter
    except FileNotFoundError:
        print(f"El archivo '{buscar_archivo}' no fue encontrado.")
        return None
    except Exception as e:
        print(f"Error al leer el archivo '{buscar_archivo}': {e}")
        return None

def generar_token(archivo):
    catalogo_tokens = {}
    for caracter in archivo:
        unicode = ord(caracter)
        catalogo_tokens[caracter] = unicode
    return catalogo_tokens

def mostrar_caracteres(archivo,token):
    for caracter in archivo:
        if caracter == '\n':
            print(f'{token[caracter]}:\t[Enter]\n')
        elif caracter == ' ':
            print(f'{token[caracter]}:\t[SPACE]\n')
        else:
            print(f'{token[caracter]}:\t{caracter}\n')

def registrar_caracteres_unicode(archivo,token):
    with open(archivo_txt, 'w') as output:
        for caracter in archivo:
            if caracter == '\n':
                output.write(f'{token[caracter]}:\t[Enter]\n')
            elif caracter == ' ':
                output.write(f'{token[caracter]}:\t[SPACE]\n')
            else:
                output.write(f'{token[caracter]}:\t{caracter}\n')

# Ejemplo de uso:
archivo = leer_archivo('Nombre.json')
archivo_txt = "diccionario_tokens.txt"
token = generar_token(archivo)
mostrar_caracteres(archivo,token)
registrar_caracteres_unicode(archivo,token)
