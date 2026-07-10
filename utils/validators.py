"""
Input validation utilities for CryptoMatrix
Common validation functions
"""

import re


def is_valid_email(email: str) -> bool:
    """
    Validate email address format
    
    Args:
        email: Email string to validate
    
    Returns:
        True if valid, False otherwise
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def is_valid_hex(hex_string: str) -> bool:
    """
    Validate hexadecimal string
    
    Args:
        hex_string: Hex string to validate
    
    Returns:
        True if valid, False otherwise
    """
    try:
        int(hex_string, 16)
        return True
    except ValueError:
        return False


def is_non_empty(value: str) -> bool:
    """
    Check if string is non-empty
    
    Args:
        value: String to check
    
    Returns:
        True if non-empty and not just whitespace
    """
    return bool(value and value.strip())
