"""
Vault Manager for key derivation and vault lifecycle.
"""
from typing import Optional, Dict
from app.crypto.encryption import derive_vault_key
from app.crypto.keys import generate_salt
from app.vault.vault import Vault

# Cache of unlocked user vaults in server memory
# Alex: In a real production system we wouldn't keep these in plain process memory,
# but for our student project this avoids re-deriving on every click.
_ACTIVE_VAULTS: Dict[int, Vault] = {}

class VaultManager:
    @staticmethod
    def unlock_vault(user_id: int, master_password: str, salt_hex: str) -> Vault:
        salt = bytes.fromhex(salt_hex)
        key = derive_vault_key(master_password, salt)
        vault = Vault(user_id=user_id, key=key)
        _ACTIVE_VAULTS[user_id] = vault
        return vault

    @staticmethod
    def get_unlocked_vault(user_id: int) -> Optional[Vault]:
        return _ACTIVE_VAULTS.get(user_id)

    @staticmethod
    def lock_vault(user_id: int) -> bool:
        vault = _ACTIVE_VAULTS.pop(user_id, None)
        if vault:
            vault.lock()
            return True
        return False
