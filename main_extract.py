from Utils.Utils import exist_user
from Extract.InsertUser import insert_user
from Extract.Extract import start_extract
from getpass import getpass


if __name__ == "__main__":
    username = input("Digite o usuário que deseja extrair: ")
    password = getpass("Digite a sua senha: ")

    print("Atualizando/Cadastrando seu usuário...")

    if insert_user(username, password):
        print("\nPrecione CTRL+C para sair a qualquer momento!\n")
        try:
            while True:
                type_of_extraction = int(input("O que deseja extrair (Seguidores - 1 / Seguindo - 2)?: "))
                if type_of_extraction not in (1, 2):
                    print("Opção inválida! Seguidores - 1 / Seguindo - 2")
                    break

                option = int(input("Extrair Novos - 1 / Atualizar - 2 / Deletar - 3: "))
                if option not in (1, 2, 3):
                    print("Opção inválida! Novos - 1 / Atualizar - 2 / Deletar - 3")
                    break

                print("Extraindo de " + username)
                start_extract(username, type_of_extraction, option)
        except KeyboardInterrupt:
            print("\n\nFim da extração!")

    else:
        print('Usuário ou senha inválidos!')
