from flask import Flask, render_template
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from .config import config_by_name
from .models.model import UserLogin, Post
from .database import database


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])

    # Set up extensions
    database.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'You need to log in to see the page'

    @login_manager.user_loader
    def load_user(user_id):
        return UserLogin.query.get(int(user_id))

    # Register blueprints
    from . import blueprints

    app.register_blueprint(blueprints.posts)
    app.register_blueprint(blueprints.auth)
    app.register_blueprint(blueprints.poster)

    # Register cli commands
    from .cli import create_all, drop_all

    with app.app_context():
        app.cli.add_command(create_all)
        app.cli.add_command(drop_all)
        # app.cli.add_command(populate)

    @app.route("/")
    def index():
        # user = UserLogin.query.filter_by(username='Bob').first()
        # if user is None:
        #     return "This is where it should go"
        # else:
        #     login_user(user)
        return render_template("index.html")

    @app.route("/profile")
    #@login_required
    def profile():
        #posts = Post.query.filter_by(user_id=current_user.id).all()
        #return render_template("profile.html", posts=posts)
        return render_template("profile.html")

    @app.route("/3d")
    def threeD():
        return render_template("vicentGalleryDemo.html")

    @app.route("/vGallery")
    def gallery():
        return render_template("Gallery.html")
    
    @app.route("/viewerEntrance")
    def viewerEntrance():
        return render_template("viewerEntrance.html")

    return app

