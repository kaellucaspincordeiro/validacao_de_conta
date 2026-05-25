from classe.Email import Email
from classe.Senha import Senha
from funcoes.verificar_email import verificar_email
from funcoes.verificar_senha import verificar_senha
from getpass import getpass

email_guardado = ""
senha_guardada = ""

while True:

    print("""
1) Cadastrar conta
2) Entrar conta
3) Encerrar o programa
""")
    opcao_acesso = input("Escolha uma opção: ")
    
    match opcao_acesso:
        case "1":

            informe_email = input("Digite seu e-mail para cadastro: ")
            informe_senha = getpass("Digite sua senha para cadastro: ")

            email = Email(informe_email)
            senha = Senha(informe_senha)

            cadastrar_email = verificar_email(email.email)
            cadastrar_senha = verificar_senha(senha.senha)

            email_guardado = email.email
            senha_guardada = senha.senha

            print(cadastrar_email)
            print(cadastrar_senha)

        case "2":

            tentativa = 3

            while tentativa > 0:

                email_cadastrado = input("Digite seu e-mail: ")
                senha_cadastrada = getpass("Digite sua senha: ")

                if email_cadastrado == email_guardado and senha_cadastrada == senha_guardada:

                    print("Login realizado com sucesso!")
                    break

                else:
                    tentativa -= 1

            if tentativa == 0:
                print("Sua conta foi bloqueada após 3 tentativas incorretas.")
                break   

        case "3":
            print("Encerrando o sistema.")   
            break


            
    

    

    

