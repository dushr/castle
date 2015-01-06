from functools import wraps

from flask import g, flash, redirect, url_for, request


def requires_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            flash(u'You need to be Signed in for this page.')
            next = "%s?%s" %( request.path, request.query_string)
            return redirect(url_for('users.login', next=next))
        return f(*args, **kwargs)

    return decorated_function
