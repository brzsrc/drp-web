from flask import Blueprint, request, render_template, redirect, url_for, abort
from flask_login import current_user
from ..database import database
from ..models.model import Post

posts = Blueprint("posts", __name__, url_prefix="/posts")


@posts.route("/", methods=["GET", "POST"])
def all():
    if request.method == "POST":
        database.session.add(Post(
            title=request.form["post_title"],
            image_url=request.form["image_url"],
            description=request.form["post_description"],
            video_url=request.form["video_url"], #
            audio_url=request.form["audio_url"], #
            user_id=current_user.id
        ))
        database.session.commit()
    all_posts = Post.query.all()
    return render_template("posts.html", posts=all_posts)


@posts.route("/<post_id>", methods=["GET", "POST"])
def single(post_id):
    the_post = Post.query.get_or_404(post_id, "Post not found.")
    if the_post:
        if request.method == "POST":
            if request.form["submit_button"] == "delete":
                database.session.delete(the_post)
                database.session.commit()
                return redirect(url_for("posts.all"))
            if request.form["submit_button"] == "put":
                the_post.title = request.form["post_title"]
                the_post.description = request.form["post_description"]
                the_post.image_url = request.form["image_url"]
                the_post.video_url = request.form["video_url"] #
                the_post.audio_url = request.form["audio_url"] #
                the_post.done = "completed" in request.form
                database.session.commit()
        return render_template("post.html", post=the_post)
