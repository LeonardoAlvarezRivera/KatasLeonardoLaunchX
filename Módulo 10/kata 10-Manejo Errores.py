
def main():
    try:
        imagen = open("config.txt")
    except FileNotFoundError:
        print("No se puedo encontrar el archivo")
    except IsADirectoryError:
        print("archivo encontrado pero es un directorio, no se puede leer")

if __name__ == '__main__':
    main()




