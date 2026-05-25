def verificar_email(email):

    dominios = ["@hotmail.com", 
                "@gmail.com",
                "@yahoo.com",
                "@outlook.com"
               ]
    if email.endswith(tuple(dominios)):
        return "E-mail cadastrado"
    else:
        return "E-mail inválido"


