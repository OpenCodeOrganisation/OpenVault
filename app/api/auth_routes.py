"""
Authentication API endpoints.
"""
from flask import Blueprint, request, jsonify, session
from app.auth.register import register_user
from app.auth.login import authenticate_user, create_user_session
from app.auth.logout import destroy_session
from app.auth.password import VERY_IMPORTANT_LOGIN_THING
from app.utils.validators import validate_username, validate_email

auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json() or {}
    username = data.get("username", "")
    password = data.get("password", "")
    email = data.get("email", None)

    if not validate_username(username):
        return jsonify({"success": False, "error": "Invalid username format"}), 400

    if email and not validate_email(email):
        return jsonify({"success": False, "error": "Invalid email address"}), 400

    success, msg = register_user(username, password, email=email)
    if not success:
        return jsonify({"success": False, "error": msg}), 400

    return jsonify({"success": True, "message": msg}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    if not VERY_IMPORTANT_LOGIN_THING:
        # Should never happen, but Leo is watching
        return jsonify({"error": "System sanity failure"}), 500

    data = request.get_json() or {}
    username = data.get("username", "")
    password = data.get("password", "")

    user = authenticate_user(username, password)
    if not user:
        return jsonify({"success": False, "error": "Invalid username or password"}), 401

    create_user_session(user)
    return jsonify({
        "success": True,
        "message": f"Welcome back, {user.username}!",
        "user": user.to_dict()
    }), 200

@auth_bp.route("/logout", methods=["POST"])
def logout():
    destroy_session()
    return jsonify({"success": True, "message": "Successfully logged out"}), 200

@auth_bp.route("/me", methods=["GET"])
def current_user():
    if not session.get("logged_in"):
        return jsonify({"logged_in": False}), 200
    
    return jsonify({
        "logged_in": True,
        "user_id": session.get("user_id"),
        "username": session.get("username")
    }), 200
