import json
from Api.InstagramApiCassiano import InstagramApiCustom
from Database.Models import User
from Database.UsersDAO import UsersDAO


def create_user(user_data, password):
    new_user = User(user_data['user']['pk'],
                    user_data['user']['username'],
                    user_data['user']['follower_count'],
                    user_data['user']['following_count'],
                    password,
                    user_data['user']['profile_pic_url']
                    )
    return new_user


def insert_or_updade_user(user):
    db = UsersDAO()
    result = UsersDAO().select_by_pk(user.pk)
    if len(result) == 1:
        user_old = result[0]
        user_old.username = user.username
        user_old.password = user.password
        user_old.following_count = user.following_count
        user_old.follower_count = user.follower_count
        db.insert_or_update(user_old)
    else:
        db.insert_or_update(user)


def insert_user(username, password):
    api = InstagramApiCustom(username, password)
    if api.login_account():
        username_come_api = api.LastJson['logged_in_user']['username']
        api.searchUsername(username_come_api)
        user_data = api.LastJson
        user_orm = create_user(user_data, password)
        insert_or_updade_user(user_orm)
        print("Usuário cadastrado/atualizado com sucesso!")
        return True
    else:
        return False
