from leitorarquivo import LeitorArquivo

def main():
    leitor = LeitorArquivo("data.txt")
    listaValores = leitor.getValores()
    print(listaValores)

    main()
