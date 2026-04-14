lista_livros = []
lista_usuarios = []
import time
def menu ():
    print("\n==SISTEMA== \n")
    print("1--Cadastrar livro")
    print("2--Cadastrar usuário")
    print("3--Pegar livro ")
    print("4--devolver livro")
    print("5--Ver livros do usuário")
    print("0--Sair do sistema")

def cadastrar_livro():

    titulo = input("\nTitulo do livro: ")
    autor = input("Nome do  autor do livro: ")
    ano = int(input("Ano do livro: "))
    
    livro = {
        'titulo': titulo,
        'autor': autor,
        'ano': ano,
        'disponivel': True
    }
    lista_livros.append(livro)

def cadastrar_usuario():
    nome = input("\nNome do usuário: ")
    
    usuario = {
        'nome': nome,
        'lista_livros': []
    }
    lista_usuarios.append(usuario)

def emprestimo():
    nome = input("\nNome do usuário: ")
    titulo = input("Título do livro: ")

    usuario_encontrado = None
    livro_encontrado = None
    
    for usuario in lista_usuarios:
        if nome == usuario ["nome"]:
            usuario_encontrado = usuario
            break
    
    for livro in lista_livros:
         if titulo == livro["titulo"]:
              livro_encontrado = livro
              break
         
    if livro_encontrado and usuario_encontrado:
        if livro_encontrado["disponivel"] == True:
            usuario_encontrado["lista_livros"].append(livro_encontrado)
            livro_encontrado ['disponivel'] = False
            print("\nLivro emprestado com sucesso!")
        else:
            print("Livro indisponível.")
    else:
        print("Usuário ou livro não encontrado.")
        
def devolucao():
    nome = input("\nNome  do usuário: ")
    titulo = input("Titulo do livro: ")

    usuario_encontrado = None
    livro_encontrado = None

    for usuario in lista_usuarios:
        if nome ==usuario['nome']:
            usuario_encontrado = usuario
            break

    for livro in lista_livros:
        if titulo == livro['titulo']:
            livro_encontrado = livro
            break

    if not usuario_encontrado or not livro_encontrado:
        print("Usuário ou livro não encontrado.")
        return                
    
    if  livro_encontrado in usuario_encontrado['lista_livros']:    
        usuario_encontrado['lista_livros'].remove(livro_encontrado)
        livro_encontrado['disponivel'] = True
        print("Livro devolvido com sucesso!")

    else:
        print("Esse usuário não está com esse livro.")
    
def ver_livros():
    nome = input("\nNome do usuário: ")
    usuario_encontrado = None
    for usuario in lista_usuarios:
        if nome == usuario['nome']:
            usuario_encontrado = usuario

    if not usuario_encontrado:
        print("Usuario não foi encontrado.")
        return       
    if not usuario_encontrado['lista_livros']:
        print("Usuário não pussui nenhum livro.")

    else:
        for livro in usuario_encontrado['lista_livros']:
            print(f"Livro: {livro['titulo']} - {livro['autor']} - {livro['ano']}\n")

def fechar_programa():
    for contador in range(3, 0, -1):
        print(f"\nFechando em {contador}...")
        time.sleep(1)
    
    print("Programa encerrado!\n")
    exit()


#---Menu---

while True:
    menu()
    #---Opcoes---

    opcao = input ("\nEscolha uma opção ~~> ")
    match opcao:
            case '1':
                cadastrar_livro()

            case '2':
                cadastrar_usuario()
            
            case '3':
                emprestimo()

            case '4':
                devolucao()

            case '5':
                ver_livros()

            case '0':
                fechar_programa()
            
            case _:
                print("Opção inválida. Tente novamente.")
                continue
