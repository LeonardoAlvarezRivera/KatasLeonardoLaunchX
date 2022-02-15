def main():
    try:
        imagen = open("/Users/leonardoalvarez/Documents/python/curso microsoft/Módulo 10/config.txt")
        print("se encontro")
    except FileNotFoundError as errFile:
        print("No se puedo encontrar el archivo", errFile)
    except IsADirectoryError:
        print("archivo encontrado pero es un directorio, no se puede leer")
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")

if __name__ == '__main__':
    main()