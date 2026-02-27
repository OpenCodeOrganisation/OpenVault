"""
User profile API routes.
"""
from flask import Blueprint, jsonify, session
from app.database.users import get_user_by_id

user_bp = Blueprint("users", __name__, url_prefix="/api/users")

@user_bp.route("/profile", methods=["GET"])
def profile():
    user_id = session.get("user_id")
    if not user_id:
        return jsonify({"error": "Not authenticated"}), 401

    user = get_user_by_id(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    return jsonify({"user": user.to_dict()}), 200
