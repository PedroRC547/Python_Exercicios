from shutil import make_archive
from zipfile import ZipFile

while (True):
    escolha = input(
        "1 - Compactar arquivo\n2 - Descompactar arquivo\n3 - Sair\nOpção: ")
    if (escolha == "1"):
        localizacaoArquivoCompactar = input(
            'Caminho do Arquivo a ser compactado: ')
        nomeArquivoCompactar = input(
            'Como deve ficar o nome do arquivo compactado: ')
        make_archive(nomeArquivoCompactar, 'zip', localizacaoArquivoCompactar)
        continue

    elif (escolha == "2"):
        localizacaoArquivoCompactar = input(
            'Caminho do Arquivo a ser descompactado: ')
        arquivoZip = ZipFile(localizacaoArquivoCompactar, 'r')
        arquivoZip.extractall()
        arquivoZip.extractall()

    elif (escolha == "3"):
        break
    else:
        print("Opção invalida, tente novamente")
