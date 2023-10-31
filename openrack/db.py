import sqlite3

import click
from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE',]
            detect_types=sqlite3.PARSE_DECLTYPES
        )s