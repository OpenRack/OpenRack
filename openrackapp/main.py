import functools

from flask import (
    Blueprint,
    flash,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from openrackapp.db import get_db


bp = Blueprint("home", __name__, url_prefix="/")
