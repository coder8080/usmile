from .user import User, init_user
from .link import Link, init_link

init_user()
init_link()

__all__ = ["User", "Link"]
