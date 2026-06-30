from classe.Email import Email
from classe.Senha import Senha
from funcoes.verificar_email import verificar_email
from funcoes.verificar_senha import verificar_senha
from getpass import getpass
from colorama import Fore, Back, Style, init

init()

email_guardado = ""
senha_guardada = ""
bloqueio = False

while True:

    print(Fore.WHITE + """
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
    
            if cadastrar_email and cadastrar_senha:
                print(Fore.LIGHTGREEN_EX + "Conta cadastrada com sucesso")
            else:
                print(Fore.RED + Style.NORMAL + "Conta inválida")

        case "2":

            if email_guardado == "" and senha_guardada == "":
                print(Fore.WHITE + "Nenhuma conta criada. Cadastre a sua conta primeiro.")
                continue

            tentativa = 3

            while tentativa > 0:

                email_cadastrado = input(Fore.WHITE + "Digite seu e-mail: ")
                senha_cadastrada = getpass(Fore.WHITE + "Digite sua senha: ")

                if email_cadastrado == email_guardado and senha_cadastrada == senha_guardada:

                    print(Fore.LIGHTGREEN_EX + "Login realizado com sucesso!")
                    break

                else:
                    tentativa -= 1
                    print(Fore.RED + Style.NORMAL + f"Email ou senha incorreta. Você tem {tentativa} tentativas!")

            if tentativa == 0:
                print(Fore.RED + Style.NORMAL + "Sua conta foi bloqueada após 3 tentativas incorretas.")
                bloqueio = True   
                break

        case "3":
            print(Fore.WHITE + "Encerrando o sistema.")   
            break


            
    

    

    

