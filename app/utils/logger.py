"""
Application logging configuration.
"""
import logging
import sys

def setup_logger(name: str = "openvault", level=logging.INFO) -> logging.Logger:
    """Creates a standardized logger for OpenVault."""
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler(sys.stdout)
        fmt = logging.Formatter("[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
        handler.setFormatter(fmt)
        logger.addHandler(handler)
        logger.setLevel(level)
    return logger

logger = setup_logger()
