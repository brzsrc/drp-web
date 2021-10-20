import click
from flask.cli import with_appcontext

from .database import database
from .models.model import Post, UserLogin


@click.command("create_all", help="Create all tables in the app's databases")
@with_appcontext
def create_all():
    database.create_all()


@click.command("drop_all", help="Drop all tables in the specified database")
@with_appcontext
def drop_all():
    database.drop_all()

# @click.command("populate", help="Populate the database with initial data")
# @with_appcontext
# def populate():
#     initial_posts = [
#         Post(
#             title="Destroy the Death Start",
#             image_url="imgs/07_003.png",
#             description="Identify and hit with a  perfect shot the only one weak spot on a space ship as big as whole planet while avoiding bad guys. NOTE TO SELF: The targeting system sucks. Use the force."
#         ),
#         Post(
#             title="Train with Yoda",
#             image_url="imgs/07_004.png",
#             description="There is no try; only do.",
#         )
#     ]
#     for post in initial_posts:
#         database.session.add(post)
#     adam = UserLogin(username="Adam")
#     database.session.add(adam)
#     database.session.commit()
