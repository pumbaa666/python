from ldap3 import Server, Connection, ALL
from datetime import datetime
from flask import flash, redirect, url_for, request, render_template, g
from flask_login import login_user, login_required, logout_user, current_user
from app.mep_dashboard import login_manager, db
from app.mep_dashboard.auth import auth
from app.mep_dashboard.auth.forms import LoginForm
from app.mep_dashboard.auth.models import Users
from app.mep_dashboard.config import Config


@login_manager.user_loader
def load_user(id):
    return Users.query.get(int(id))


@auth.before_request
def get_current_user():
    g.user = current_user


@auth.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        flash('You are already logged in !', category="warning")
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        s = Server(host=Config.ldap_host, port=int(Config.ldap_port), get_info=ALL)
        c = Connection(s, user=form.username.data + Config.ldap_suffix, password=form.password.data)
        if not c.bind():
            flash("Invalid username or password. Please try again.", category="danger")
            return render_template('auth/login.html', form=form)

        user = Users.query.filter_by(username=form.username.data).first()

        if not user:
            #TODO : ldap search for user data such as Team, first_name, last_name and email
            user = Users(username=form.username.data, team_id=1, first_name='', last_name='', date_in=datetime.now(),
                         last_connection=datetime.now(), is_active=1)
            db.session.add(user)
            db.session.commit()
        login_user(user, form.remember_me.data)
        flash("Logged in successfully as {}.".format(user.username), category="success")
        return redirect(request.args.get('next') or url_for('index'))

    if form.errors:
        flash(form.errors, category="danger")

    return render_template("auth/login.html", form=form)


@login_required
@auth.route('/logout')
def logout():
    logout_user()
    flash('You have logged out.', category="success")
    return redirect(url_for('index'))
