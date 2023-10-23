# Definindo uma lista para armazenar os usuários
usuarios = []

# Função para cadastrar uma pessoa
def cadastrar_pessoa():
    nome = input("Digite o nome da pessoa: ")
    while True:
        idade_str = input("Digite a idade da pessoa: ")
        endereco = input("Digite o endereço da pessoa: ")
        
        try:
            idade = int(idade_str)
            if nome != '' and idade > 0 and endereco != '':
                usuario = {"nome": nome, "idade": idade, "endereco": endereco}
                usuarios.append(usuario)
                print("Pessoa cadastrada com sucesso!")
                break
            else:
                print("Dados inválidos. Certifique-se de que nome, idade e endereço não estão vazios e a idade é maior que zero.")
        except ValueError:
            print("Idade inválida. Certifique-se de que a idade seja um número inteiro válido.")


# Função para pesquisar uma pessoa
def pesquisar_pessoa():
    nome = input("Digite o nome da pessoa que deseja pesquisar: ")
    for usuario in usuarios:
        if usuario["nome"] == nome:
            print(f"Nome: {usuario['nome']}, Idade: {usuario['idade']}, Endereço: {usuario['endereco']}")
            return
    print("Pessoa não encontrada.")

# Função para deletar uma pessoa
def deletar_pessoa():
    nome = input("Digite o nome da pessoa que deseja deletar: ")
    for usuario in usuarios:
        if usuario["nome"] == nome:
            usuarios.remove(usuario)
            print("Pessoa deletada com sucesso!")
            return
    print("Pessoa não encontrada.")

# Loop principal do programa
while True:
    print("\nMenu:")
    print("1. Cadastrar pessoa")
    print("2. Pesquisar pessoa")
    print("3. Deletar pessoa")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        cadastrar_pessoa()
    elif opcao == "2":
        pesquisar_pessoa()
    elif opcao == "3":
        deletar_pessoa()
    elif opcao == "4":
        break
    else:
        print("Opção inválida. Escolha uma opção válida.")
