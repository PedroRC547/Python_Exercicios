from shutil import make_archive
localizacaoArquivoCompactar = input('Caminho do Arquivo a ser compactado: ')
nomeArquivoCompactar = input('Como deve ficar o nome do arquivo compactado: ')
make_archive(nomeArquivoCompactar, 'zip', localizacaoArquivoCompactar)
