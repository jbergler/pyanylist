"""Module to define the errors the client API would be returning."""

from __future__ import annotations

__all__ = [
    "MyClientError",
]


class MyClientError(Exception):
    """Example of client error.

    TODO: update it to correspond to your API errors.
    """