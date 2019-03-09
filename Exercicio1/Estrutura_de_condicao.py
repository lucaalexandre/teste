####### o Input serve para que o usuario consiga digitar no Terminal

Graduacao = input("sua graduação ? ")

###### a estrutura é IF - ELIF - ELSE

###### o lower tem a funçao de respeitar o código

###### Nunca esquecer que o Python usa o " : " e não o " { } "

if Graduacao.lower() == "tecnologo":
    print("Você é um Tecnólogo")
elif Graduacao.lower() == "bacharel":
    print("Você é um bacharel")
else: print("Não entendi.")



