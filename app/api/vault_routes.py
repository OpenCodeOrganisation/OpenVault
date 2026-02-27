"""
Vault REST API routes.
"""
from flask import Blueprint, request, jsonify, session
from app.vault.vault_manager import VaultManager
from app.services.vault_service import VaultService

vault_bp = Blueprint("vault", __name__, url_prefix="/api/vault")

def get_current_vault_service():
    user_id = session.get("user_id")
    if not user_id:
        return None, jsonify({"error": "Unauthorized"}), 401
    
    vault = VaultManager.get_unlocked_vault(user_id)
    if not vault or not vault.is_unlocked:
        return None, jsonify({"error": "Vault is locked. Please authenticate with master password."}), 403
    
    return VaultService(vault._key), None, None

@vault_bp.route("/entries", methods=["GET"])
def list_entries():
    service, err_resp, err_code = get_current_vault_service()
    if err_resp:
        return err_resp, err_code

    user_id = session.get("user_id")
    category = request.args.get("category")
    entries = service.list_entries(user_id)
    
    if category:
        entries = service.filter_entries_by_category(entries, category)

    return jsonify({"entries": [e.to_dict(include_plain=True) for e in entries]}), 200

@vault_bp.route("/entries", methods=["POST"])
def create_entry():
    service, err_resp, err_code = get_current_vault_service()
    if err_resp:
        return err_resp, err_code

    data = request.get_json() or {}
    title = data.get("title", "").strip()
    username = data.get("username", "").strip()
    password = data.get("password", "")
    url = data.get("url", "").strip()
    category = data.get("category", "general").strip()

    if not title or not password:
        return jsonify({"error": "Title and password are required"}), 400

    user_id = session.get("user_id")
    entry_id = service.add_entry(user_id, title, username, password, url=url, category=category)
    return jsonify({"success": True, "entry_id": entry_id}), 201

@vault_bp.route("/entries/<int:entry_id>", methods=["DELETE"])
def delete_entry(entry_id: int):
    service, err_resp, err_code = get_current_vault_service()
    if err_resp:
        return err_resp, err_code

    user_id = session.get("user_id")
    success = service.delete_entry(entry_id, user_id)
    if not success:
        return jsonify({"error": "Entry not found"}), 404

    return jsonify({"success": True}), 200
