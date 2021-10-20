from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from ..models.model import Post
from ..database import database as db

poster = Blueprint("poster", __name__)


@poster.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        img_url = request.form['img_url']
        video_url = request.form['video_url']
        user_id = current_user.id
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            new_post = Post(title=title, description=description, image_url=img_url, video_url=video_url, audio_url=audio_url, user_id=user_id)
            db.session.add(new_post)
            db.session.commit()

            return redirect(url_for('profile'))

    return render_template('poster/create.html')


# def get_post(id, check_author=True):
#     post = get_db().execute(
#         'SELECT p.id, title, body, created, author_id, username'
#         ' FROM post p JOIN user u ON p.author_id = u.id'
#         ' WHERE p.id = ?',
#         (id,)
#     ).fetchone()
#
#     if post is None:
#         abort(404, f"Post id {id} doesn't exist.")
#
#     if check_author and post['author_id'] != g.user['id']:
#         abort(403)
#
#     return post


@poster.route('/<int:post_id>/update', methods=('GET', 'POST'))
@login_required
def update(post_id):
    the_post = Post.query.get_or_404(post_id, "Post not found.")
    if the_post:
        if request.method == 'POST':
            request_title = request.form['title']
            request_description = request.form['description']
            request_image_url = request.form['img_url']
            request_video_url = request.form['video_url']
            request_audio_url = request.form['audio_url']
            error = None
            if not request_title:
                error = 'Title is required.'

            if error is not None:
                flash(error)
            else:
                the_post.title = request_title
                the_post.description = request_description
                the_post.image_url = request_image_url
                the_post.video_url = request_video_url
                the_post.audio_url = request_audio_url
                db.session.commit()
                return redirect(url_for('profile'))

    return render_template('poster/update.html', post=the_post)


@poster.route('/<int:post_id>/delete', methods=('POST',))
@login_required
def delete(post_id):
    the_post = Post.query.get_or_404(post_id, "Post not found.")
    if the_post:
        db.session.delete(the_post)
        db.session.commit()
    return redirect(url_for('profile'))
