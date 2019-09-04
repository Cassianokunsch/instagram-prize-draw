import os
import time
from Api.InstagramApiCassiano import InstagramApiCustom
from Utils.Utils import get_user
from Database.GenericDAO import GenericDAO as UserDAO
from Database.FollowersDAO import FollowersDAO
from Database.FollowingsDAO import FollowingsDAO
from Database.Models import Follower, Following


def data_to_delete(data, user_id, type_of_extraction):
    if type_of_extraction == 1:
        db = FollowersDAO()
    else:
        db = FollowingsDAO()

    data_to_mark_to_delete = []
    data_response = []

    for user in data:
        data_response.append(user['pk'])

    result = db.select_by_userid(user_id)
    for user_orm in result:
        if user_orm.pk not in data_response:
            user_orm.delete = '*'
            data_to_mark_to_delete.append(user_orm)

    print("Usuários marcados como deletados >>> " +
          str(len(data_to_mark_to_delete)))
    db.insert_or_update_all(data_to_mark_to_delete)


def data_extract_update(user_id, type_of_extraction, api):
    if type_of_extraction == 1:
        db = FollowersDAO()
    else:
        db = FollowingsDAO()

    count = 0
    result = db.select_by_userid(user_id)
    print("Atualizando " + str(len(result)) + " usuários salvos no banco")
    for user_orm in result:
        api.searchUsername(user_orm.username)
        try:
            user_orm.username = api.LastJson['user']['username']
            user_orm.profile_url = api.LastJson['user']['profile_pic_url']
            user_orm.following_count = api.LastJson['user']['following_count']
            user_orm.follower_count = api.LastJson['user']['follower_count']
            user_orm.is_private = api.LastJson['user']['is_private']
            user_orm.status_refresh = True

            db.insert_or_update(user_orm)
            count += 1
            print("Usuários atualizados..." + str(count) +
                  "/" + str(len(result)), end='\r')
        except Exception as e:
            print("Não foi possível atualizar o usuário: " + user_orm.username)
            print(e)
        time.sleep(1.5)
    
    print("Usuários atualizados..." + str(count) + "/" + str(len(result)))


def data_extract_new(date_to_insert, user_id, type_of_extraction, api):
    if type_of_extraction == 1:
        db = FollowersDAO()
    else:
        db = FollowingsDAO()

    data_in_db = []
    data_not_in_db = []

    result = db.select_by_userid(user_id)
    for user_orm in result:
        data_in_db.append(user_orm.pk)

    for user in date_to_insert:
        if user['pk'] not in data_in_db:
            data_not_in_db.append(user['username'])

    print("\nUsuários que te seguem >>> " + str(len(date_to_insert)))
    print("Usuários salvos no banco >>> " + str(len(data_in_db)))
    print("Usuários novos para extraír >>> " + str(len(data_not_in_db)))
    print("\nExtraindo usuários")

    count = 0
    for username in data_not_in_db:
        api.searchUsername(username)
        try:
            if type_of_extraction == 1:
                new_data = Follower(api.LastJson['user']['pk'],
                                    api.LastJson['user']['username'],
                                    api.LastJson['user']['profile_pic_url'],
                                    api.LastJson['user']['following_count'],
                                    api.LastJson['user']['follower_count'],
                                    api.LastJson['user']['is_private'],
                                    False,
                                    user_id)
            else:
                new_data = Following(api.LastJson['user']['pk'],
                                     api.LastJson['user']['username'],
                                     api.LastJson['user']['profile_pic_url'],
                                     api.LastJson['user']['following_count'],
                                     api.LastJson['user']['follower_count'],
                                     api.LastJson['user']['is_private'],
                                     False,
                                     user_id)
            db.insert_or_update(new_data)
            count += 1
            print("Usuários extraídos..." + str(count) +
                  "/" + str(len(data_not_in_db)), end='\r')
        except Exception as e:
            print("Não foi possível inserir o usuário: " + user_orm.username)
            print(e)
        time.sleep(1.5)

    print("Usuários extraídos..." + str(count) + "/" + str(len(data_not_in_db)))


def start_extract(username, type_of_extraction, option):
    user = get_user(username)
    api = InstagramApiCustom(user.username, user.password)
    api.login_account()
    if type_of_extraction == 1:
        response = api.getTotalFollowers(user.pk)
    elif type_of_extraction == 2:
        response = api.getTotalFollowings(user.pk)
    else:
        print("Opção inválida! Seguidores - 1 / Seguindo - 2")
        exit(0)

    if option == 1:
        data_extract_new(response, user.id, type_of_extraction, api)
    elif option == 2:
        data_extract_update(user.id, type_of_extraction, api)
    elif option == 3:
        data_to_delete(response, user.id, type_of_extraction)
    else:
        print("Opção inválida! Novos - 1 / Atualizar - 2 / Deletar - 3s")
        exit(0)
