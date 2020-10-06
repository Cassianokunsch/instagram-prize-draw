import time
import os
from random import randint
from Api.InstagramApiCassiano import InstagramApiCustom
from Utils.Utils import save_comment_did


class AutoComment:
    def __init__(self, username, password, photo, profile_photo):
        self.api = InstagramApiCustom(username, password)
        self.photo = photo
        self.profile_photo = profile_photo

    def start_comment(self, lst_of_comment_to_do, lst_of_comment_made, path):
        for comment in lst_of_comment_to_do:
            if comment not in lst_of_comment_made:
                if self.api.do_comment(comment):
                    lst_of_comment_made.append(comment)
                    print(str(len(lst_of_comment_made)) +
                          " comentários feitos de " + str(len(lst_of_comment_to_do)), end='\r')
                    save_comment_did(path, comment)
                    time.sleep(randint(10, 120))
                else:
                    break

        if len(lst_of_comment_made) == len(lst_of_comment_to_do):
            print("Todos os comentarios foram feitos! Em um total de " +
                  str(len(lst_of_comment_made)) + " comentários.")
        else:
            print("Spam detectado aguardando um dia para voltar a comentar.")
            time.sleep(86400)

    def verify_coditions(self):
        print("\nFazendo login...")
        if self.api.login_account():
            print("Login feito com sucesso")
            if self.api.find_user_id(self.profile_photo):
                print("Perfil da promoção encontrado")
                if self.api.search_photo(self.photo):
                    print("Promoção encontrada")
                    return True
                else:
                    print("Promoção não encontrada!")
                    return False
            else:
                print("Perfil da promoção não encontrado!")
                return False
        else:
            print(
                "Erro no login! Use o programa main_extract.py para atualizar seu usuário!")
            return False
