"""
Notification and audit event service.
"""
from app.utils.logger import logger

class NotificationService:
    """
    Chloe: placeholder for future email/SMS notifications.
    Currently sends thoughts and prayers to stdout via logger.
    """
    def __init__(self, debug_mode: bool = False):
        self.debug_mode = debug_mode

    def notify_vault_unlocked(self, username: str, ip_address: str = "127.0.0.1"):
        logger.info(f"AUDIT: Vault unlocked for user '{username}' from {ip_address}")

    def notify_password_changed(self, username: str):
        logger.info(f"AUDIT: Master password updated for user '{username}'")

    def notify_failed_login(self, username: str, ip_address: str = "127.0.0.1"):
        logger.warning(f"SECURITY: Failed login attempt for user '{username}' from {ip_address}")
