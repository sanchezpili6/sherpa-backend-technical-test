from flask import Blueprint
from flask import jsonify
from flask import request
from backend.logic.auth import login, logout, get_user_status
from backend.logic.posts import create_post, get_all_posts, get_posts_by_author, get_post, delete_post, update_post
from backend.logic.users import DEFAULT_PROFILE_PIC, create_user, delete_user, update_user, get_user

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/login', methods=['POST'])
def login_user():
    """
    Login a user.
    receives: username, password
    """
    username = request.json['username']
    password = request.json['password']
    return jsonify(login(username, password))


@main_blueprint.route('/logout', methods=['POST'])
def logout_user():
    """
    Logout a user.
    receives: username
    :return:
    """
    username = request.json['username']
    return jsonify(logout(username))


@main_blueprint.route('/user_status', methods=['GET'])
def get_user_status():
    """
    Get the status of a user.
    receives: username
    :return:
    """
    username = request.json['username']
    return jsonify(get_user_status(username))


@main_blueprint.route('/create_user/', methods=['POST'])
def create_user_endpoint():
    """
    Create a new user.
    Only admins can create new admins.
    receives:
        username: str
        password: str
        email: str
        user_type: str
        profile_pic: str
        user_id_creating: int
    """
    username = request.json['username']
    password = request.json['password']
    email = request.json['email']
    user_type = request.json['user_type']
    profile_pic = request.json['profile_pic'].optional(DEFAULT_PROFILE_PIC)
    user_id_creating = request.json['user_id_creating']
    return jsonify(create_user(username, password, email, user_type, profile_pic, user_id_creating))


@main_blueprint.route('/delete_user/', methods=['POST'])
def delete_user_endpoint():
    """
    Delete a user.
    Only admins can delete users.
    receives:
        user_id_to_delete: int
        user_id_deleting: int
    """
    user_id_to_delete = request.json['user_id_to_delete']
    user_id_deleting = request.json['user_id_deleting']
    return jsonify(delete_user(user_id_to_delete, user_id_deleting))


@main_blueprint.route('/update_user/', methods=['POST'])
def update_user_endpoint():
    """
    Update a user.
    Admins can update any user.
    Users can only update themselves.
    receives:
        user_id_updating: int (required)
        user_id_to_update: int (required)
        username: str (optional)
        password: str (optional)
        email: str (optional)
        user_type: str (optional)
        profile_pic: str (optional)
    """
    user_id_updating = request.json['user_id_updating']
    user_id_to_update = request.json['user_id_to_update']
    username = request.json['username'].optional(None)
    password = request.json['password'].optional(None)
    email = request.json['email'].optional(None)
    user_type = request.json['user_type'].optional(None)
    profile_pic = request.json['profile_pic'].optional(None)
    return jsonify(update_user(user_id_updating, user_id_to_update, username, password, email, user_type, profile_pic))


@main_blueprint.route('/get_user/', methods=['GET'])
def get_user_endpoint():
    """
    Get a user.
    Admins can get any user complete data.
    Users can only get themselves complete data and other users incomplete data.
    receives:
        user_id_getting: int
        user_id_getting_from: int
    :return:
        if admin or user is getting themselves::
            {'id': int, 'username': str, 'password': str, 'email': str, 'user_type': str, 'profile_pic': str, 'last_login': str, 'is_logged_in': bool}
        if other user:
            {'id': int, 'username': str, 'email': str, 'profile_pic': str, last_login': str}
    """
    user_id = request.json['user_id']
    user_id_getting = request.json['user_id_getting']
    return jsonify(get_user(user_id, user_id_getting))


@main_blueprint.route('/create_post/', methods=['POST'])
def create_post_endpoint():
    """
    Create a new post.
    receives:
        user_id_creating: int
        title: str
        description: str
        image: str
    """
    user_id_creating = request.json['user_id_creating']
    title = request.json['title']
    post_text = request.json['post_text']
    return jsonify(create_post(user_id_creating, title, post_text))


@main_blueprint.route('/get_all_posts/', methods=['GET'])
def get_all_posts_endpoint():
    """
    Get all posts.
    :return:
        {'posts': [{'id': int, 'user_id': int, 'title': str, 'description': str, 'image': str, 'created_at': str, 'updated_at': str}]}
    """
    user_id_getting = request.json['user_id_getting']
    return jsonify(get_all_posts(user_id_getting))
