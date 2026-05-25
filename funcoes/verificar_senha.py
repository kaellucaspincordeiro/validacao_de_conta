def verificar_senha(senha):

    verificacao_senha = (len(senha) >= 10
                        and senha.upper()
                        and senha.lower()
                        and senha.isascii()
                        )

    if verificacao_senha:
        return "Senha cadastrada"
    else:
        return "Senha inválida"

