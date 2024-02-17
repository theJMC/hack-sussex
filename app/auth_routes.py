from flask import Blueprint, render_template, request, Response
from .auth import page_auth
from .models import User
from uuid import uuid4
from hashlib import sha256
from app import db

auth_routes = Blueprint('auth_routes', __name__)

context = {}


@auth_routes.route('/login')
def login_page():
    return render_template("login.html")


@auth_routes.route('/login', methods=['POST'])
def login():
    email = request.json['email']
    passhash = request.json['passhash']

    user = User.query.filter_by(email=email).first()
    if not user:
        return Response('{"message": "Invalid email or password"}', status=401, mimetype="application/json")
    elif user.password != passhash:
        return Response('{"message": "Invalid email or password"}', status=401, mimetype="application/json")
    else:
        return {"id": str(user.id), "status": 200}


@auth_routes.route('/signup')
def signup_page():
    return render_template("signup.html")


@auth_routes.route('/signup', methods=['POST'])
def signup():
    name = request.json["name"]
    email = request.json["email"]
    passhash = request.json["passhash"]

    user = User.query.filter_by(email=email).first()
    if user:
        return Response('{"message": "Email already registered"}', status=400, mimetype="application/json")
    user_id = uuid4()

    token = sha256(email.encode('utf-8') + passhash.encode('utf-8'))
    db.session.add(User(id=user_id, name=name, email=email, password=passhash, token=token.hexdigest()))
    db.session.commit()
    return {"id": str(user_id), "status": 200}


@auth_routes.route('/logout')
def logout_page():
    return render_template("logout.html")
