from flask import Blueprint, render_template, request, url_for, g, flash
from werkzeug.utils import redirect
from .. import db
from ..models import Post
from ..forms import PostForm
from .auth_views import login_required
from datetime import datetime

bp = Blueprint('post', __name__, url_prefix='/post')


@bp.route('/list/')
def _list():
    page = request.args.get('page', type=int, default=1)
    post_list = Post.query.order_by(Post.create_date.desc())
    post_list = post_list.paginate(page, per_page=10)
    return render_template('post/post_list.html', post_list=post_list)


@bp.route('/detail/<int:post_id>/')
def detail(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post/post_detail.html', post=post)


@bp.route('/create/', methods=('GET', 'POST'))
@login_required
def create():
    form = PostForm()
    if request.method == 'POST' and form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, create_date=datetime.now(), user=g.user)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('post/post_form.html', form=form)


@bp.route('/modify/<int:question_id>', methods=('GET', 'POST'))
@login_required
def modify(post_id):
    post = Post.query.get_or_404(post_id)
    if g.user != post.user:
        flash('수정권한이 없습니다.')
        return redirect(url_for('post.detail', post_id=post_id))
    if request.method == 'POST':
        form = PostForm()
        if form.validate_on_submit():
            form.populate_obj(post)
            post.modify_date = datetime.now()
            db.session.commit()
            return redirect(url_for('post.detail', post_id=post_id))
        else:
            form = PostForm(obj=post)
        return render_template('post/post_form.html', form=form)
