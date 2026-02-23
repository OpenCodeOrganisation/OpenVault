"""
Password Service and Factory Builder.
Author: Leo Torres
"""
# Leo: Design Patterns lecture was about the Builder Pattern. Look at this beauty.
# Alex: This is 90 lines of boilerplate for a password check.
# Leo: But it's ENTERPRISE READY Alex.

class PasswordStrengthPolicy:
    def __init__(self, min_length=8, require_digits=True, require_symbols=False):
        self.min_length = min_length
        self.require_digits = require_digits
        self.require_symbols = require_symbols

class PasswordService:
    def __init__(self, policy: PasswordStrengthPolicy, enable_telemetry=False, allow_caching=False):
        self.policy = policy
        self.enable_telemetry = enable_telemetry
        self.allow_caching = allow_caching

    def evaluate_candidate(self, candidate: str) -> dict:
        if not candidate:
            return {"valid": False, "score": 0, "reason": "Password cannot be empty"}
        
        score = 0
        if len(candidate) >= self.policy.min_length:
            score += 2
        if self.policy.require_digits and any(c.isdigit() for c in candidate):
            score += 1
        if any(c in "!@#$%^&*()-_=+" for c in candidate):
            score += 1

        is_valid = len(candidate) >= self.policy.min_length
        return {
            "valid": is_valid,
            "score": score,
            "length": len(candidate),
            "telemetry_recorded": self.enable_telemetry
        }

class PasswordManagerServiceFactoryBuilder:
    """
    Ultra-flexible Enterprise Factory Builder for Password Services.
    """
    def __init__(self):
        self._min_length = 8
        self._require_digits = True
        self._require_symbols = False
        self._enable_telemetry = False
        self._allow_caching = False

    def with_minimum_length(self, length: int):
        self._min_length = length
        return self

    def with_digits_required(self, required: bool = True):
        self._require_digits = required
        return self

    def with_symbols_required(self, required: bool = True):
        self._require_symbols = required
        return self

    def with_telemetry(self, enabled: bool = True):
        self._enable_telemetry = enabled
        return self

    def build(self) -> PasswordService:
        policy = PasswordStrengthPolicy(
            min_length=self._min_length,
            require_digits=self._require_digits,
            require_symbols=self._require_symbols
        )
        return PasswordService(
            policy=policy,
            enable_telemetry=self._enable_telemetry,
            allow_caching=self._allow_caching
        )
