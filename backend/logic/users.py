import datetime

from db_utils import run_query
from auth import login, logout, get_user_status

DEFAULT_PROFILE_PIC = 'shorturl.at/OQRV5'


def create_user(username, password, email, user_type, profile_pic=DEFAULT_PROFILE_PIC, last_login=datetime.datetime.now(), user_id_creating=None):
    if user_id_creating is None:
        query = f"""insert into users 
                    (username, user_password, email, user_type, profile_pic, last_login) 
                    values ('{username}', '{password}', '{email}', 'user', '{profile_pic}', '{last_login}')"""
        login(username, password)
        return run_query(query)
    if is_user_admin(user_id_creating):
        admin_query = f"""insert into users 
                    (username, user_password, email, user_type, profile_pic, last_login)) 
                    values ('{username}', '{password}', '{email}', '{user_type}', '{profile_pic}', '{last_login}')"""
        login(username, password)
        return run_query(admin_query)

    return 'You don\'t have permission to create a new user.'


def delete_user(user_id_to_delete, user_id_deleting):
    if is_user_admin(user_id_deleting):
        query = f"""delete from users where id = {user_id_to_delete} and id != {user_id_deleting}"""
        run_query(query)
        return 'User deleted.'
    return 'You don\'t have permission to delete this user.'


def update_user(user_id_updating, user_id_to_update, username, password, email, user_type, profile_pic=DEFAULT_PROFILE_PIC):
    if is_user_admin(user_id_updating):
        admin_query = f"""update users 
                    set username = '{username}', user_password = '{password}', email = '{email}', user_type = '{user_type}', profile_pic = '{profile_pic}' 
                    where id = {user_id_to_update}"""
        run_query(admin_query)
    if user_id_updating == user_id_to_update:
        user_query = f"""update users 
                    set username = '{username}', user_password = '{password}', email = '{email}', profile_pic = '{profile_pic}' 
                    where id = {user_id_to_update}"""
        run_query(user_query)
    return 'You don\'t have permission to update this user.'


def is_user_admin(user_id):
    query = f"select user_type from users where id = {user_id}"
    return 'admin' == run_query(query)[0][0]


def get_user(user_id, user_id_getting):
    if user_id_getting == user_id or is_user_admin(user_id_getting):
        query = f"select * from users where id = {user_id}"
        return run_query(query)
    else:
        normal_user_query = f"select id, username, email, profile_pic, last_login from users where id = {user_id}"
        return run_query(normal_user_query)

