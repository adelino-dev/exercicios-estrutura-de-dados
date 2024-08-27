from getpass import getpass
while True:
    usuario = input("Usuário:")
    senha = getpass("Senha:")

    if usuario == senha:
        print("\n A senha não pode ser igual ao usuário. Digite novamente.\n")

    else:
        print("\n Usuário e senha válidos.")
        break