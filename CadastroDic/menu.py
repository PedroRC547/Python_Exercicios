escolha = ''
idUsuario = 0
cadastros ={}

while(escolha != '0'):
    idUsuario += 1
    nome = input("Nome: ")
    idade = input("Idade: ")
    altura = input("Altura: ")
    peso = input("Peso: ")
    escolha = input("----------\nAdicionar mais um usuário: (Sim - 1 / Não - 0) ")

    cadastro = {idUsuario : [nome,idade,altura,peso]}
    

    cadastros.update(cadastro)

print(cadastros)