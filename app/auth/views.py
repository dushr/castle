import urllib

from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash

from app.users.models import User
from app.clients.models import Client
from app.users.decorators import requires_login

mod = Blueprint('auth', __name__, url_prefix='/auth')


@mod.route('/authorize/')
@requires_login
def authorize():
    user = g.user
    client_id = request.args.get('client_id')
    client_secret = request.args.get('client_secret')
    client = Client.query.get(client_id)

    param_dict = {
        'success': 0
    }

    if client_secret == client.secret and client in user.clients:
        param_dict = {
            'success': 1,
            'email': user.email,
            'name': user.name
        }

    return redirect("%s?%s" % (client.redirect_url, urllib.urlencode(param_dict)))


@mod.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id'])
