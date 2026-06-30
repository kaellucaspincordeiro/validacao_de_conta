def verificar_senha(senha):

    maiuscula = any(s.isupper() for s in senha)
    minuscula = any(s.islower() for s in senha)
    caractere_especial = any(not s.isalnum() for s in senha)

    return (len(senha) >= 10
            and maiuscula
            and minuscula
            and caractere_especial
           )

