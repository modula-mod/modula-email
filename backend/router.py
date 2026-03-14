"""
Email module host bridge.

The first release is host-rendered and uses Modula core APIs for runtime, services,
and automation. This router remains intentionally small until the module gets its
own mailbox data layer.
"""

from fastapi import APIRouter

router = APIRouter()
