from application.user_api import user_api_blueprint
from flask import request, jsonify, make_response
from application.models import User
from flask_login import login_required, login_user, logout_user, current_user
from application import db, login_manager
from passlib.hash import sha256_crypt

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

@login_manager.request_loader
def load_user_from_request(request):
    api_key = request.headers.get('Authorization')
    if api_key:
        api_key = api_key.replace('Basic ', '', 1)
        user = User.query.filter_by(api_key=api_key).first()
        if user:
            return user
    return None

@user_api_blueprint.route('/api/users')
def users():
    """Returns list of all users"""
    data = []
    for user in User.query.all():
        data.append(user.to_json())

    reponse = jsonify(data)
    return reponse

@user_api_blueprint.route('/api/user/register', methods=['POST'])
def register():
    """Registers a new user"""
    existing_email = User.query.filter_by(email=request.form['email']).first()
    existing_username = User.query.filter_by(username=request.form['username']).first()
    if existing_username or existing_email:
        return jsonify({'message': 'Email or Username already exists'})
    else:
        user = User()

        user.firstname = request.form['firstname']
        user.lastname = request.form['lastname']
        user.username = request.form['username']
        user.email = request.form['email']
        user.password = sha256_crypt.hash(str(request.form['password']))
        user.authenticated =True

        db.session.add(user)
        db.session.commit()

        response = jsonify({'message': 'User added', 'result': user.to_json()})
        return response

@user_api_blueprint.route('/api/user/login', methods=['POST'])
def login():
    """Logins in a user"""
    username = request.form['username']
    user = User.query.filter_by(username=username).first()
    if user:
        if sha256_crypt.verify(str(request.form['password']), user.password):
            user.encode_api_key()
            db.session.commit()
            login_user(user)
            return make_response(jsonify({'message': 'Login successful', 'api_key': user.api_key}))
    return make_response(jsonify({'message': 'Not Logged In'}), 401)

@user_api_blueprint.route('/api/user/logout', methods=['POST'])
def logout():
    """Logout logged in user"""
    if current_user.is_authenticated:
        logout_user()
        response = make_response(jsonify({'message': 'You are logged out'}))
    else:
        response = make_response(jsonify({'message': 'You are not logged in'}))
    return response

@user_api_blueprint.route('/api/user/<username>/exists')
def check_username(username):
    """Check if username exists"""
    user = User.query.filter_by(username=username).first()
    if user is not None:
            response = jsonify({'message': True})
    else:
        response = jsonify({'message': 'Cannot find username'}), 404
    return response

@user_api_blueprint.route('/api/user')
def user():
    """Returns current logged in user"""
    if current_user.is_authenticated:
        return make_response(jsonify({'result': current_user.to_json()}))
    return make_response(jsonify({'message': 'You are not logged in'})), 401
