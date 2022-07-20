class User(db.Model):
    id = db.Column("id", db.Integer, primary_key=True)
    first_name = db.Column("first_name", db.String(100))
    last_name = db.Column("last_name", db.String(100))
    email = db.Column("email", db.String(100))
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    posts = db.relationship("Post", backref="user", lazy=True)
    comments = db.relationship("Comment", backref="user", lazy=True)

    # liked = db.relationship(
    #     'PostLike',
    #     foreign_keys='PostLike.user_id',
    #     backref='user', lazy='dynamic'
    # )

    # def like_post(self, post):
    #     if not self.has_liked_post(post):
    #         like = PostLike(user_id=self.id, post_id=post.id)
    #         db.session.add(like)
    #
    # def unlike_post(self, post):
    #     if self.has_liked_post(post):
    #         PostLike.query.filter_by(
    #             user_id=self.id,
    #             post_id=post.id).delete()
    #
    # def has_liked_post(self, post):
    #     return PostLike.query.filter(
    #         PostLike.user_id == self.id,
    #         PostLike.post_id == post.id).count() > 0
    #
    # class PostLike(db.Model):
    #     __tablename__ = 'post_like'
    #     id = db.Column(db.Integer, primary_key=True)
    #     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #     post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    @app.route('/like/<int:post_id>/<action>')
    @login_required
    def like_action(post_id, action):
        post = Post.query.filter_by(id=post_id).first_or_404()
        if action == 'like':
            current_user.like_post(post)
            db.session.commit()
        if action == 'unlike':
            current_user.unlike_post(post)
            db.session.commit()
        return redirect(request.referrer)