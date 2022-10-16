from flask import render_template, redirect, request, url_for
from flask_login import login_user, logout_user, login_required
from . import auth
from ..models import User
from .forms import LoginForm

@auth.route("/login", methods=["GET", "POST"])
def login():
    
    error_message = ''
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(request.args.get("next") or url_for("main.index"))
        else:
            error_message = "Invalid username or password!"
    
    return render_template("auth/login.html", form=form, error_message=error_message)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))


