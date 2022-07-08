from db_utils import run_query


def login(username, password):
    query = f"select id, username, user_password, user_type from users where username = '{username}' and " \
            f"user_password = '{password}' "
    correct_data = run_query(query)
    if correct_data:
        update_login_date_query = f"update users set last_login = now() where username = '{username}'"
        log_user_query = f"update users set is_logged_in = true where username = '{username}'"
        run_query(update_login_date_query)
        run_query(log_user_query)
    return 'Login successful.' if correct_data else 'Login failed.'


def logout(username):
    query = f"update users set is_logged_in = false where username = '{username}'"
    run_query(query)
    return 'Logout successful.'


def get_user_status(username):
    query = f"select is_logged_in from users where username = '{username}'"
    return run_query(query)[0][0]
