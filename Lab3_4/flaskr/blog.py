from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from werkzeug.exceptions import abort
from flaskr.auth import login_required
from flaskr.database import getdatabase
bp = Blueprint("blog", __name__)


@bp.route("/")
def index():
    database = getdatabase()
    posts = database.execute(
        "SELECT p.id, title, body, created, author_id, username"
        " FROM post p JOIN user u ON p.author_id = u.id"
        " ORDER BY created DESC"
    ).fetchall()
    return render_template("blog/index.html", posts=posts)


def get_post(id, check_author=True):
    post = (
        getdatabase()
        .execute(
            "SELECT p.id, title, body, created, author_id, username"
            " FROM post p JOIN user u ON p.author_id = u.id"
            " WHERE p.id = ?",
            (id,),
        )
        .fetchone()
    )
    if post is None:
        abort(404, f"Post id {id} doesn't exist.")
    if check_author and post["author_id"] != g.user["id"]:
        abort(403)

    return post


@bp.route("/create", methods=("GET", "POST"))
@login_required
def create():
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        error = None
        if not title:
            error = "Title is required."
        if error is not None:
            flash(error)
        else:
            database = getdatabase()
            database.execute(
                "INSERT INTO post (title, body, author_id) VALUES (?, ?, ?)",
                (title, body, g.user["id"]),
            )
            database.commit()
            return redirect(url_for("blog.index"))
    return render_template("blog/create.html")


@bp.route("/<int:id>/update", methods=("GET", "POST"))
@login_required
def update(id):
    post = get_post(id)
    if request.method == "POST":
        title = request.form["title"]
        body = request.form["body"]
        error = None
        if not title:
            error = "Title is required."
        if error is not None:
            flash(error)
        else:
            database = getdatabase()
            database.execute(
                "UPDATE post SET title = ?, body = ? WHERE id = ?", (title, body, id)
            )
            database.commit()
            return redirect(url_for("blog.index"))
    return render_template("blog/update.html", post=post)


@bp.route("/<int:id>/delete", methods=("POST",))
@login_required
def delete(id):
    get_post(id)
    database = getdatabase()
    database.execute("DELETE FROM post WHERE id = ?", (id,))
    database.commit()
    return redirect(url_for("blog.index"))
