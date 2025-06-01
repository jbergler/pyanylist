"""Common utility functions for the AnyList package."""

from uuid import uuid4


def uuid() -> str:
    """Generate a UUID without hyphens for AnyList API."""
    return str(uuid4()).replace("-", "")
