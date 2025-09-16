#crie um cadastro com senha
while True:
    usuario = input("diga la seu nome caro usuario: ")
    confirmau = input("confirme seu nome: ")
    if confirmau == usuario:
        print("usuario correto")
        break  # Sai do loop se o nome estiver correto
    else:
        print("usuario errado seu sacana")
senha = input("digite sua senha: ")
while True :
    confirma = input("confirme sua senha: ")
    if confirma == senha:
        print("senha correta")
        break  # Sai do loop se a senha estiver correta
    else:
        print("senha errada seu sacana")
        #break  serve sempre para sair do loop