Sistema de Validação de Conta

Neste projeto foi implementado um sistema de validação de conta, no qual o usuário deve cadastrar um e-mail e uma senha. Após o cadastro, o usuário poderá realizar o login utilizando os dados informados.

O projeto utiliza a biblioteca Colorama, uma biblioteca multiplataforma usada para adicionar cores, estilos de formatação e destaque às mensagens exibidas no terminal.

Instalação da biblioteca Colorama

Para instalar a biblioteca Colorama, utilize o seguinte comando no terminal:

py -m pip install colorama

Funcionalidades:

-Validação de e-mail em formato básico, como:
  - usuario@hotmail.com;
  - usuario@gmail.com;
  - usuario@yahoo.com;
  - entre outros.
- Validação de senha contendo:
  - mínimo de 10 caracteres;
  - pelo menos uma letra maiúscula;
  - pelo menos uma letra minúscula;
  - pelo menos um caractere especial.
- Sistema de login com verificação de e-mail e senha cadastrados;
- Limite de até 3 tentativas de login incorretas;
- Encerramento do programa após 3 tentativas inválidas ou após login realizado com sucesso.