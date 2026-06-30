def verificar_email(email):

    dominios = ["@hotmail.com", 
                "@gmail.com",
                "@yahoo.com",
                "@outlook.com"
               ]
    return email.endswith(tuple(dominios))


